"""
Platypus-based layout engine.
Uses ReportLab Frame objects for proper text flow and column management.
Custom flowables record their bounding boxes when drawn.
"""

import io
import os
import tempfile

from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame,
    Paragraph, Spacer, HRFlowable, FrameBreak, PageBreak,
    KeepTogether, KeepInFrame, NextPageTemplate,
    Flowable, Table as _RLTable, TableStyle,
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader

from reportlab.pdfgen import canvas as _rc
from config import (
    PAGE_W, PAGE_H, MARGIN_T, MARGIN_B, MARGIN_L, MARGIN_R,
    GUTTER,
)

COL_W  = (PAGE_W - MARGIN_L - MARGIN_R - GUTTER) / 2
FULL_W = PAGE_W - MARGIN_L - MARGIN_R
BODY_H = PAGE_H - MARGIN_T - MARGIN_B

# Shared measurement canvas (no output, just for .wrapOn())
_MEAS_CANVAS = _rc.Canvas(io.BytesIO(), pagesize=(PAGE_W, PAGE_H))

def _measure_height(items, width):
    """Sum the wrapped heights of a list of Platypus flowables."""
    total = 0
    for item in items:
        _, h = item.wrapOn(_MEAS_CANVAS, width, PAGE_H)
        total += h
    return total

# ── Paragraph styles ──────────────────────────────────────────────────────────
ST = {
    'jname': ParagraphStyle(
        'jname', fontName='Times-Italic', fontSize=7.5,
        leading=9, alignment=TA_CENTER,
        textColor=colors.HexColor('#555555'), spaceAfter=1,
    ),
    'doi': ParagraphStyle(
        'doi', fontName='Times-Roman', fontSize=7,
        leading=8.5, alignment=TA_CENTER,
        textColor=colors.HexColor('#666666'), spaceAfter=3,
    ),
    'title': ParagraphStyle(
        'title', fontName='Times-Bold', fontSize=15,
        leading=19, alignment=TA_CENTER, spaceAfter=5,
    ),
    'authors': ParagraphStyle(
        'authors', fontName='Times-Roman', fontSize=9,
        leading=11, alignment=TA_CENTER, spaceAfter=2,
    ),
    'affil': ParagraphStyle(
        'affil', fontName='Times-Italic', fontSize=7.5,
        leading=9.5, alignment=TA_CENTER,
        textColor=colors.HexColor('#444444'), spaceAfter=2,
    ),
    'dates': ParagraphStyle(
        'dates', fontName='Times-Italic', fontSize=7.5,
        leading=9, alignment=TA_CENTER,
        textColor=colors.HexColor('#666666'), spaceAfter=3,
    ),
    'abs_label': ParagraphStyle(
        'abs_label', fontName='Times-Bold', fontSize=8.5,
        leading=10, spaceAfter=2,
    ),
    'abstract': ParagraphStyle(
        'abstract', fontName='Times-Roman', fontSize=8.5,
        leading=11, alignment=TA_JUSTIFY, spaceAfter=3,
    ),
    'keywords': ParagraphStyle(
        'keywords', fontName='Times-Roman', fontSize=8,
        leading=10, spaceAfter=0,
    ),
    'section': ParagraphStyle(
        'section', fontName='Times-Bold', fontSize=9.5,
        leading=12, spaceBefore=8, spaceAfter=3,
    ),
    'body': ParagraphStyle(
        'body', fontName='Times-Roman', fontSize=9,
        leading=12, alignment=TA_JUSTIFY, spaceAfter=4,
        firstLineIndent=10,
    ),
    'caption': ParagraphStyle(
        'caption', fontName='Times-Italic', fontSize=7.5,
        leading=9.5, alignment=TA_JUSTIFY, spaceAfter=4,
    ),
    'tbl_caption': ParagraphStyle(
        'tbl_caption', fontName='Times-Italic', fontSize=7.5,
        leading=9.5, spaceAfter=2,
    ),
    'ref_head': ParagraphStyle(
        'ref_head', fontName='Times-Bold', fontSize=9.5,
        leading=12, spaceBefore=8, spaceAfter=3,
    ),
    'ref': ParagraphStyle(
        'ref', fontName='Times-Roman', fontSize=7.5,
        leading=9.5, alignment=TA_JUSTIFY, spaceAfter=2,
        leftIndent=10, firstLineIndent=-10,
    ),
}

# ── Table cell style ──────────────────────────────────────────────────────────
_TBL_STYLE = TableStyle([
    ('BACKGROUND',     (0, 0), (-1, 0),  colors.HexColor('#D6E4F0')),
    ('FONTNAME',       (0, 0), (-1, 0),  'Helvetica-Bold'),
    ('FONTNAME',       (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE',       (0, 0), (-1, -1), 7),
    ('GRID',           (0, 0), (-1, -1), 0.3, colors.HexColor('#AAAAAA')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')]),
    ('TOPPADDING',     (0, 0), (-1, -1), 2),
    ('BOTTOMPADDING',  (0, 0), (-1, -1), 2),
    ('LEFTPADDING',    (0, 0), (-1, -1), 3),
    ('RIGHTPADDING',   (0, 0), (-1, -1), 3),
    ('VALIGN',         (0, 0), (-1, -1), 'MIDDLE'),
    ('ALIGN',          (0, 0), (-1, -1), 'CENTER'),
    ('LINEBELOW',      (0, 0), (-1, 0),  0.6, colors.HexColor('#5588BB')),
    ('LINEABOVE',      (0, 0), (-1, 0),  0.6, colors.HexColor('#5588BB')),
    ('LINEBELOW',      (0, -1), (-1, -1), 0.6, colors.HexColor('#5588BB')),
])

# ── Page decoration callback ──────────────────────────────────────────────────
def _decorate(canvas, doc):
    canvas.saveState()
    pn = canvas.getPageNumber()
    if pn == 1:
        canvas.setFont('Helvetica', 6)
        canvas.setFillColorRGB(0.5, 0.5, 0.5)
        canvas.drawCentredString(
            PAGE_W / 2, PAGE_H - MARGIN_T + 12,
            getattr(doc, '_jline', ''),
        )
        canvas.setStrokeColorRGB(0.3, 0.3, 0.3)
        canvas.setLineWidth(0.5)
        canvas.line(MARGIN_L, PAGE_H - MARGIN_T + 8, PAGE_W - MARGIN_R, PAGE_H - MARGIN_T + 8)
    else:
        short = getattr(doc, '_short', '')
        canvas.setFont('Helvetica', 7)
        canvas.setFillColorRGB(0.35, 0.35, 0.35)
        canvas.drawString(MARGIN_L, PAGE_H - MARGIN_T + 8, short)
        canvas.drawRightString(PAGE_W - MARGIN_R, PAGE_H - MARGIN_T + 8, str(pn))
        canvas.setStrokeColorRGB(0.55, 0.55, 0.55)
        canvas.setLineWidth(0.4)
        canvas.line(MARGIN_L, PAGE_H - MARGIN_T + 4, PAGE_W - MARGIN_R, PAGE_H - MARGIN_T + 4)
    # Page number bottom-center
    canvas.setFont('Times-Roman', 8)
    canvas.setFillColorRGB(0, 0, 0)
    canvas.drawCentredString(PAGE_W / 2, MARGIN_B - 18, str(pn))
    canvas.restoreState()

# ── Page templates ────────────────────────────────────────────────────────────
def _make_templates(layout, header_h):
    """Build page templates using the measured header height."""
    body_h_p1 = PAGE_H - MARGIN_T - MARGIN_B - header_h

    f_hdr = Frame(
        MARGIN_L, PAGE_H - MARGIN_T - header_h,
        FULL_W, header_h,
        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        id='header',
    )
    if layout == 'double':
        f_l1 = Frame(MARGIN_L, MARGIN_B, COL_W, body_h_p1,
                     leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='L1')
        f_r1 = Frame(MARGIN_L + COL_W + GUTTER, MARGIN_B, COL_W, body_h_p1,
                     leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='R1')
        f_l  = Frame(MARGIN_L, MARGIN_B, COL_W, BODY_H,
                     leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='L')
        f_r  = Frame(MARGIN_L + COL_W + GUTTER, MARGIN_B, COL_W, BODY_H,
                     leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='R')
        f_wide = Frame(MARGIN_L, MARGIN_B, FULL_W, BODY_H,
                       leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='Wide')
        t1    = PageTemplate(id='First',  frames=[f_hdr, f_l1, f_r1], onPage=_decorate)
        t2    = PageTemplate(id='TwoCol', frames=[f_l, f_r],           onPage=_decorate)
        t_wide = PageTemplate(id='Wide',  frames=[f_wide],             onPage=_decorate)
        return [t1, t2, t_wide]
    else:
        f_b1 = Frame(MARGIN_L, MARGIN_B, FULL_W, body_h_p1,
                     leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='B1')
        f_b  = Frame(MARGIN_L, MARGIN_B, FULL_W, BODY_H,
                     leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='B')
        t1 = PageTemplate(id='First',  frames=[f_hdr, f_b1], onPage=_decorate)
        t2 = PageTemplate(id='OneCol', frames=[f_b],           onPage=_decorate)
        return [t1, t2]

# ── Custom flowables ──────────────────────────────────────────────────────────
class FigureFlowable(Flowable):
    def __init__(self, img_buf, w_pts, h_pts, is_vector, fig_id, bboxes, meta):
        super().__init__()
        self.img_buf   = img_buf
        self.width     = w_pts
        self.height    = h_pts
        self.is_vector = is_vector
        self.fig_id    = fig_id
        self.bboxes    = bboxes
        self.meta      = meta
        self.hAlign    = 'CENTER'

    def wrap(self, avail_w, avail_h):
        if self.width > avail_w:
            scale = avail_w / self.width
            self.width  *= scale
            self.height *= scale
        return self.width, self.height

    def draw(self):
        if self.is_vector:
            try:
                from svglib.svglib import svg2rlg
                from reportlab.graphics import renderPDF
                self.img_buf.seek(0)
                with tempfile.NamedTemporaryFile(suffix='.svg', delete=False) as tmp:
                    tmp.write(self.img_buf.read())
                    tmp_path = tmp.name
                try:
                    drw = svg2rlg(tmp_path)
                finally:
                    os.unlink(tmp_path)
                if drw:
                    sx = self.width  / drw.width
                    sy = self.height / drw.height
                    drw.width, drw.height = self.width, self.height
                    drw.transform = (sx, 0, 0, sy, 0, 0)
                    renderPDF.draw(drw, self.canv, 0, 0)
                    return
            except Exception:
                pass
        self.img_buf.seek(0)
        self.canv.drawImage(
            ImageReader(self.img_buf), 0, 0,
            width=self.width, height=self.height,
            preserveAspectRatio=True, mask='auto',
        )

    def drawOn(self, canvas, x, y, _sW=0):
        ax = x
        if _sW:
            if self.hAlign in ('CENTER', 'CENTRE'):
                ax = x + 0.5 * _sW
            elif self.hAlign == 'RIGHT':
                ax = x + _sW
        page = canvas.getPageNumber()
        # bbox: top-left origin, y axis downward
        bbox = [
            round(ax, 2),
            round(PAGE_H - y - self.height, 2),
            round(ax + self.width, 2),
            round(PAGE_H - y, 2),
        ]
        self.bboxes.append({'kind': 'figure', 'id': self.fig_id,
                            'page': page, 'bbox': bbox, **self.meta})
        super().drawOn(canvas, x, y, _sW)


class BboxTable(_RLTable):
    def __init__(self, data, tbl_id, bboxes, meta, **kwargs):
        super().__init__(data, **kwargs)
        self.tbl_id = tbl_id
        self.bboxes = bboxes
        self.meta   = meta

    def drawOn(self, canvas, x, y, _sW=0):
        w = getattr(self, '_width',  0) or self.width
        h = getattr(self, '_height', 0) or self.height
        page = canvas.getPageNumber()
        bbox = [round(x, 2), round(PAGE_H - y - h, 2),
                round(x + w, 2), round(PAGE_H - y, 2)]
        self.bboxes.append({'kind': 'table', 'id': self.tbl_id,
                            'page': page, 'bbox': bbox, **self.meta})
        super().drawOn(canvas, x, y, _sW)


# ── Layout engine ─────────────────────────────────────────────────────────────
class LayoutEngine:
    def __init__(self, layout):
        self.layout  = layout          # "single" or "double"
        self.buf     = io.BytesIO()
        self.bboxes  = []
        self.story   = []
        self._sec_n  = 0
        self._short  = ''
        self._jline  = ''

    # ── Header (page 1 only) ──────────────────────────────────────────────────
    def set_journal_header(self, journal_name, doi, received, accepted):
        self._jline = f'{journal_name}  \u2022  DOI: {doi}  \u2022  Received {received}  \u2022  Accepted {accepted}'

    def add_header_block(self, journal_name, doi, received, accepted,
                         title, authors, affiliations,
                         abstract, keywords):
        self._short = title[:55] + ('\u2026' if len(title) > 55 else '')

        header_content = [
            Paragraph(journal_name.upper(), ST['jname']),
            Paragraph(
                f'DOI: {doi}\u2002|\u2002Received: {received}\u2002|\u2002Accepted: {accepted}',
                ST['doi'],
            ),
            HRFlowable(width='100%', thickness=0.8,
                       color=colors.HexColor('#222222'), spaceAfter=5),
            Paragraph(title, ST['title']),
            Paragraph(authors, ST['authors']),
            Paragraph(affiliations, ST['affil']),
            Spacer(1, 4),
            HRFlowable(width='100%', thickness=0.35,
                       color=colors.grey, spaceAfter=3),
            Paragraph('<b>Abstract</b>', ST['abs_label']),
            Paragraph(abstract, ST['abstract']),
            Paragraph(f'<b>Keywords:</b> {keywords}', ST['keywords']),
            HRFlowable(width='100%', thickness=0.35,
                       color=colors.grey, spaceAfter=4),
        ]

        # Measure actual content height; add 14pt padding below
        measured = _measure_height(header_content, FULL_W) + 14
        # Leave at least 200pt for the body columns on page 1
        max_hdr = PAGE_H - MARGIN_T - MARGIN_B - 200
        self._header_h = min(measured, max_hdr)

        self.story.append(
            KeepInFrame(FULL_W, self._header_h, header_content, mode='shrink')
        )
        self.story.append(FrameBreak())
        self.story.append(
            NextPageTemplate('TwoCol' if self.layout == 'double' else 'OneCol')
        )

    # ── Body elements ─────────────────────────────────────────────────────────
    def add_section_heading(self, text):
        self._sec_n += 1
        self.story.append(Paragraph(f'{self._sec_n}. {text}', ST['section']))

    def add_paragraph(self, text):
        self.story.append(Paragraph(text, ST['body']))

    # ── Figure ────────────────────────────────────────────────────────────────
    def add_figure(self, fig_id, img_buf, is_vector, width_pts, height_pts,
                   caption_style, caption_text, dpi, width_inches, height_inches):
        meta = {
            'caption_style': caption_style,
            'caption_text':  caption_text,
            'dpi':           dpi,
            'width_inches':  width_inches,
            'height_inches': height_inches,
        }
        fig_fl = FigureFlowable(
            img_buf, width_pts, height_pts, is_vector,
            fig_id, self.bboxes, meta,
        )
        self.story.append(Spacer(1, 6))
        if caption_text:
            cap_para = Paragraph(caption_text, ST['caption'])
            self.story.append(KeepTogether([fig_fl, Spacer(1, 2), cap_para]))
        else:
            self.story.append(fig_fl)
        self.story.append(Spacer(1, 6))

    # ── Table ─────────────────────────────────────────────────────────────────
    def add_table(self, tbl_id, data, orientation, content_type, caption=''):
        is_wide = (orientation == 'across_2_col' and self.layout == 'double')
        col_w   = FULL_W if (orientation == 'across_2_col' or self.layout == 'single') else COL_W
        n_cols  = len(data[0])
        cell_w  = col_w / n_cols

        tbl = BboxTable(
            data, tbl_id, self.bboxes,
            {'content_type': content_type, 'orientation': orientation},
            colWidths=[cell_w] * n_cols,
            repeatRows=1,
        )
        tbl.setStyle(_TBL_STYLE)

        cap_items = []
        if caption:
            cap_items.append(Paragraph(caption, ST['tbl_caption']))

        if is_wide:
            # Switch to full-width page for the table, return to two-column after
            self.story.append(NextPageTemplate('Wide'))
            self.story.append(PageBreak())
            self.story.append(Spacer(1, 4))
            if cap_items:
                self.story.append(KeepTogether(cap_items + [tbl]))
            else:
                self.story.append(tbl)
            self.story.append(Spacer(1, 6))
            # Next page will revert to two-column (no extra PageBreak — let content flow)
            self.story.append(NextPageTemplate('TwoCol'))
        else:
            self.story.append(Spacer(1, 4))
            if cap_items:
                self.story.append(KeepTogether(cap_items + [tbl]))
            else:
                self.story.append(tbl)
            self.story.append(Spacer(1, 6))

    # ── References ────────────────────────────────────────────────────────────
    def add_references(self, refs):
        self.story.append(Paragraph('References', ST['ref_head']))
        for i, ref in enumerate(refs, 1):
            self.story.append(Paragraph(f'[{i}]\u2002{ref}', ST['ref']))

    # ── Build ─────────────────────────────────────────────────────────────────
    def build(self):
        header_h = getattr(self, '_header_h', BODY_H * 0.4)
        doc = BaseDocTemplate(
            self.buf,
            pagesize=(PAGE_W, PAGE_H),
            pageTemplates=_make_templates(self.layout, header_h),
            leftMargin=MARGIN_L, rightMargin=MARGIN_R,
            topMargin=MARGIN_T,  bottomMargin=MARGIN_B,
        )
        doc._short = self._short
        doc._jline = self._jline
        doc.build(self.story)
        self.page_count = doc.page
        self.buf.seek(0)
        return self.buf.read()
