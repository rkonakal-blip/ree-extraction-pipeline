"""
Generates a single synthetic REE paper PDF + ground-truth JSON.
"""

import json
import os
import random
import numpy as np

from config import (
    PAGES_OPTIONS, PAGES_WEIGHTS,
    FIGURES_RANGE, TABLES_RANGE,
    LAYOUT_OPTIONS, LAYOUT_WEIGHTS,
    FIGURE_CLASSES, CLASS_WEIGHTS_LIST,
    DPI_OPTIONS, DPI_WEIGHTS,
    WIDTH_RANGE, ASPECT_RANGE,
    MULTIPANEL_PROB, PANEL_COUNT_RANGE, IS_VECTOR_PROB,
    CAPTION_STYLES, CAPTION_WEIGHTS,
    REE_ELEMENTS, REE_WORD_BANK,
    REE_BODY_TEMPLATES, PAPER_SECTIONS,
    JOURNAL_NAMES, AFFILIATIONS_LIST,
    REF_TEMPLATES, REF_JOURNALS, REF_TITLES,
    PAGE_W, PAGE_H, MARGIN_L, MARGIN_R, MARGIN_T, MARGIN_B,
    GUTTER,
)
from figure_generator import generate_figure
from caption_generator import generate_caption
from table_generator import generate_table_data
from layout_engine import LayoutEngine, COL_W, FULL_W

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'synthetic_dataset')


# ── Text generation helpers ───────────────────────────────────────────────────

def _ree(n=1):
    return random.sample(REE_ELEMENTS, n)


def _ree_sentence():
    tpl  = random.choice(REE_BODY_TEMPLATES)
    ree  = random.choice(REE_ELEMENTS)
    ree2 = random.choice([e for e in REE_ELEMENTS if e != ree])
    return tpl.format(
        ree    = ree,
        ree2   = ree2,
        prop   = random.choice(["selectivity", "efficiency", "recovery", "purity"]),
        method = random.choice(["solvent extraction", "precipitation",
                                "adsorption", "ion exchange"]),
        tech   = random.choice(["XRD", "FTIR", "SEM", "TEM", "ICP-MS"]),
        solvent= random.choice(["D2EHPA", "Cyanex 272", "TBP", "EHEHPA"]),
        ph     = random.uniform(1.5, 5.5),
        ph_min = random.uniform(1.0, 2.5),
        ph_max = random.uniform(4.5, 6.5),
        ph_opt = random.uniform(3.0, 5.0),
        temp   = random.uniform(25, 80),
        val    = random.uniform(60, 99),
        conc   = random.uniform(0.5, 4.0),
        size   = random.uniform(50, 500),
        r2     = random.uniform(0.95, 0.999),
        ratio  = random.choice(["1:1", "2:1", "1:2", "3:1"]),
        time   = random.uniform(10, 90),
        sf     = random.uniform(2, 20),
    )


def _paragraph(min_s=2, max_s=5):
    return ' '.join(_ree_sentence() for _ in range(random.randint(min_s, max_s)))


def _abstract():
    """Generate an abstract of 200–250 words."""
    sentences = []
    word_count = 0
    while word_count < 200:
        s = _ree_sentence()
        sentences.append(s)
        word_count += len(s.split())
    # If we overshot 250, trim whole sentences from the end
    while word_count > 250 and len(sentences) > 1:
        removed = sentences.pop()
        word_count -= len(removed.split())
    return ' '.join(sentences)


def _keywords():
    words = random.sample(REE_WORD_BANK, random.randint(4, 6))
    return '; '.join(w.lower() for w in words)


def _fake_title():
    rees   = random.sample(REE_ELEMENTS, random.randint(2, 3))
    verbs  = ["Extraction", "Separation", "Recovery",
              "Selective Extraction", "Synergistic Extraction"]
    mths   = ["Solvent Extraction", "D2EHPA", "Cyanex 272",
              "Liquid-Liquid Extraction", "Ion Exchange"]
    return (f"{random.choice(verbs)} of {', '.join(rees)} from Aqueous Solution "
            f"by {random.choice(mths)}")


def _fake_authors():
    firsts = ["J.", "M.", "X.", "L.", "H.", "Y.", "K.", "A.", "R.", "S.", "T.", "W."]
    lasts  = ["Zhang", "Li", "Wang", "Liu", "Chen", "Kumar", "Smith", "Park",
              "Tanaka", "Garcia", "Nguyen", "Kim", "M\u00fcller", "Patel", "Brown"]
    n = random.randint(3, 5)
    return ', '.join(f'{random.choice(firsts)} {random.choice(lasts)}' for _ in range(n))


def _fake_affil():
    return random.choice(AFFILIATIONS_LIST)


def _fake_doi():
    return f'10.1016/j.{random.choice(["hydromet","seppur","cej","jrare"])}.{random.randint(2018,2024)}.{random.randint(100000,999999)}'


def _fake_dates():
    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    year  = random.randint(2020, 2024)
    rm    = random.randint(1, 10)
    am    = rm + random.randint(1, 3)
    if am > 12:
        am = 12
    return (f"{random.randint(1,28)} {month_names[rm-1]} {year}",
            f"{random.randint(1,28)} {month_names[am-1]} {year}")


def _fake_ref(n):
    refs = []
    surnames = ["Zhang", "Li", "Wang", "Chen", "Liu", "Kumar", "Smith",
                "Park", "Tanaka", "Garcia", "Brown", "Kim", "Nguyen", "Patel"]
    for _ in range(n):
        tpl  = random.choice(REF_TEMPLATES)
        ree  = random.choice(REE_ELEMENTS)
        ree2 = random.choice([e for e in REE_ELEMENTS if e != ree])
        title_tpl = random.choice(REF_TITLES)
        title = title_tpl.format(ree=ree, ree2=ree2)
        year  = random.randint(2015, 2024)
        refs.append(tpl.format(
            a1    = random.choice(surnames) + ', ' + random.choice("ABCDEFGHJKLMN") + '.',
            a2    = random.choice(surnames) + ', ' + random.choice("ABCDEFGHJKLMN") + '.',
            a3    = random.choice(surnames) + ', ' + random.choice("ABCDEFGHJKLMN") + '.',
            a4    = random.choice(surnames) + ', ' + random.choice("ABCDEFGHJKLMN") + '.',
            title = title.capitalize(),
            journal = random.choice(REF_JOURNALS),
            year  = year,
            vol   = random.randint(100, 350),
            issue = random.randint(1, 12),
            start = random.randint(100, 500),
            end   = random.randint(501, 600),
            abbr  = random.choice(["hydromet","seppur","cej","jrare","mineng"]),
            num   = random.randint(10000, 99999),
        ))
    return refs


def _section_body(section_name):
    ree  = random.choice(REE_ELEMENTS)
    ree2 = random.choice([e for e in REE_ELEMENTS if e != ree])
    tpl_info = {
        "solvent":   random.choice(["D2EHPA", "Cyanex 272", "TBP"]),
        "supplier":  random.choice(["Sigma-Aldrich", "Merck", "Alfa Aesar"]),
        "ph_min":    1.0,
        "ph_max":    6.0,
        "val":       random.uniform(80, 99),
        "ph_opt":    random.uniform(3.0, 5.0),
        "ree":       ree,
        "ree2":      ree2,
        "grant":     f'{random.randint(5,9)}{random.randint(1000,9999)}{"".join(random.choices("ABCDE",k=3))}',
    }
    for name, template in PAPER_SECTIONS:
        if name == section_name:
            try:
                return template.format(**tpl_info)
            except KeyError:
                return template
    return _paragraph()


# ── Main generator ────────────────────────────────────────────────────────────

def generate_paper(paper_id: str, allow_across_2_pages: bool = False):
    layout    = random.choices(LAYOUT_OPTIONS, weights=LAYOUT_WEIGHTS, k=1)[0]
    n_pages   = int(np.random.choice(PAGES_OPTIONS, p=PAGES_WEIGHTS))
    n_figs    = random.randint(*FIGURES_RANGE)
    n_tables  = random.randint(*TABLES_RANGE)

    col_w_pts = COL_W if layout == 'double' else FULL_W

    # ── Figure specs ──────────────────────────────────────────────────────────
    fig_specs = []
    for i in range(1, n_figs + 1):
        fig_type      = random.choices(FIGURE_CLASSES, weights=CLASS_WEIGHTS_LIST, k=1)[0]
        dpi           = random.choices(DPI_OPTIONS, weights=DPI_WEIGHTS, k=1)[0]
        w_in          = random.uniform(*WIDTH_RANGE)
        aspect        = random.uniform(*ASPECT_RANGE)
        h_in          = w_in / aspect
        is_multipanel = random.random() < MULTIPANEL_PROB
        panel_count   = random.randint(*PANEL_COUNT_RANGE) if is_multipanel else 1
        is_vector     = random.random() < IS_VECTOR_PROB
        cap_style, cap_text = generate_caption(i)

        # Clamp display size to column width
        w_pts = min(w_in * 72.0, col_w_pts)
        h_pts = w_pts / (w_in / h_in)

        fig_specs.append({
            'figure_id':     i,
            'figure_type':   fig_type,
            'is_multipanel': is_multipanel,
            'panel_count':   panel_count,
            'is_vector':     is_vector,
            'dpi':           dpi,
            'width_inches':  round(w_pts / 72, 3),
            'height_inches': round(h_pts / 72, 3),
            'width_pts':     w_pts,
            'height_pts':    h_pts,
            'caption_style': cap_style,
            'caption_text':  cap_text,
        })

    # ── Table specs ───────────────────────────────────────────────────────────
    tbl_specs = []
    for i in range(1, n_tables + 1):
        data, ct, orient = generate_table_data(
            allow_across_2_pages=allow_across_2_pages
        )
        tbl_specs.append({
            'table_id':    i,
            'content_type': ct,
            'orientation':  orient,
            'data':         data,
        })

    # ── Build story ───────────────────────────────────────────────────────────
    engine = LayoutEngine(layout)

    title    = _fake_title()
    authors  = _fake_authors()
    affil    = _fake_affil()
    abstract = _abstract()
    keywords = _keywords()
    doi      = _fake_doi()
    journal  = random.choice(JOURNAL_NAMES)
    received, accepted = _fake_dates()

    engine.set_journal_header(journal, doi, received, accepted)
    engine.add_header_block(
        journal, doi, received, accepted,
        title, authors, affil, abstract, keywords,
    )

    # Standard journal sections
    SECTION_NAMES = [
        "Introduction",
        "Materials and Methods",
        "Results and Discussion",
        "Conclusions",
        "Acknowledgements",
    ]

    # Distribute figures and tables across sections (weight toward middle sections)
    section_weights = [1, 2, 4, 1, 0.5]
    fig_sections  = random.choices(range(len(SECTION_NAMES)), weights=section_weights, k=n_figs)
    tbl_sections  = random.choices(range(len(SECTION_NAMES)), weights=section_weights, k=n_tables)

    fig_queue  = {s: [] for s in range(len(SECTION_NAMES))}
    tbl_queue  = {s: [] for s in range(len(SECTION_NAMES))}
    for fi, sec in zip(fig_specs, fig_sections):
        fig_queue[sec].append(fi)
    for ti, sec in zip(tbl_specs, tbl_sections):
        tbl_queue[sec].append(ti)

    for sec_idx, sec_name in enumerate(SECTION_NAMES):
        engine.add_section_heading(sec_name)

        # 2–4 opening paragraphs per section (ensures columns are full)
        for _ in range(random.randint(2, 4)):
            engine.add_paragraph(_paragraph(min_s=3, max_s=6))

        # Interleave figures, tables, and extra paragraphs
        items_in_sec = (
            [('fig', f) for f in fig_queue[sec_idx]] +
            [('tbl', t) for t in tbl_queue[sec_idx]]
        )
        random.shuffle(items_in_sec)

        # 2–4 body paragraphs scattered around figures/tables
        n_paras = random.randint(2, 4)
        positions = sorted(random.sample(
            range(len(items_in_sec) + n_paras),
            min(n_paras, len(items_in_sec) + n_paras),
        ))
        full_queue = list(items_in_sec)
        for offset, pos in enumerate(positions):
            full_queue.insert(pos + offset, ('para', None))

        for kind, item in full_queue:
            if kind == 'para':
                engine.add_paragraph(_paragraph())
            elif kind == 'fig':
                fs = item
                gen_w = max(fs['width_pts'] / 72.0, 2.5)
                gen_h = max(fs['height_pts'] / 72.0, 2.0)
                img_buf, data_gt = generate_figure(
                    fs['figure_type'], gen_w, gen_h,
                    fs['dpi'], fs['is_vector'],
                    fs['is_multipanel'], fs['panel_count'],
                )
                fs['data_gt'] = data_gt
                engine.add_figure(
                    fig_id        = fs['figure_id'],
                    img_buf       = img_buf,
                    is_vector     = fs['is_vector'],
                    width_pts     = fs['width_pts'],
                    height_pts    = fs['height_pts'],
                    caption_style = fs['caption_style'],
                    caption_text  = fs['caption_text'],
                    dpi           = fs['dpi'],
                    width_inches  = fs['width_inches'],
                    height_inches = fs['height_inches'],
                )
            elif kind == 'tbl':
                ts = item
                tbl_caption = (
                    f"Table {ts['table_id']}. "
                    + ' '.join(random.choices(REE_WORD_BANK, k=random.randint(4, 9)))
                    + '.'
                )
                engine.add_table(
                    tbl_id       = ts['table_id'],
                    data         = ts['data'],
                    orientation  = ts['orientation'],
                    content_type = ts['content_type'],
                    caption      = tbl_caption,
                )

    # References
    refs = _fake_ref(random.randint(15, 30))
    engine.add_references(refs)

    pdf_bytes    = engine.build()
    actual_pages = engine.page_count

    # ── Write PDF ─────────────────────────────────────────────────────────────
    pdf_path = os.path.join(OUTPUT_DIR, 'pdfs', f'{paper_id}.pdf')
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    with open(pdf_path, 'wb') as f:
        f.write(pdf_bytes)

    # ── Assemble GT JSON ──────────────────────────────────────────────────────
    bbox_map = {(r['kind'], r['id']): r for r in engine.bboxes}

    gt_figures = []
    for fs in fig_specs:
        rec = bbox_map.get(('figure', fs['figure_id']), {})
        gt_figures.append({
            'figure_id':       fs['figure_id'],
            'figure_type':     fs['figure_type'],
            'is_multipanel':   fs['is_multipanel'],
            'panel_count':     fs['panel_count'],
            'page':            rec.get('page', -1),
            'bbox':            rec.get('bbox', [0, 0, 0, 0]),
            'caption_style':   fs['caption_style'],
            'caption_text':    fs['caption_text'],
            'caption_position': 'below',
            'dpi':             fs['dpi'],
            'width_inches':    fs['width_inches'],
            'height_inches':   fs['height_inches'],
            'is_vector':       fs['is_vector'],
            'data_gt':         fs.get('data_gt'),
        })

    gt_tables = []
    for ts in tbl_specs:
        rec = bbox_map.get(('table', ts['table_id']), {})
        gt_tables.append({
            'table_id':    ts['table_id'],
            'content_type': ts['content_type'],
            'orientation':  ts['orientation'],
            'page':         rec.get('page', -1),
            'bbox':         rec.get('bbox', [0, 0, 0, 0]),
            'data':         ts['data'],
        })

    gt = {
        'paper_id': paper_id,
        'pages':    actual_pages,
        'layout':   layout,
        'figures':  gt_figures,
        'tables':   gt_tables,
    }

    gt_path = os.path.join(OUTPUT_DIR, 'ground_truth', f'{paper_id}_gt.json')
    os.makedirs(os.path.dirname(gt_path), exist_ok=True)
    with open(gt_path, 'w', encoding='utf-8') as f:
        json.dump(gt, f, indent=2, ensure_ascii=False)

    print(f'[{paper_id}] layout={layout} | pages={actual_pages} | '
          f'figs={len(gt_figures)} | tables={len(gt_tables)}')
    return gt


