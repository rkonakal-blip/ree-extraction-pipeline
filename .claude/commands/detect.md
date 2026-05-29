# Figure and Table Detection

## Purpose
First stage of the REE extraction pipeline. Parses one or multiple 
PDFs and detects all figures, plots, and tables. Saves cropped 
snapshots and metadata for each detected element. Outputs are passed 
to the Classify stage (figures) and Table stage (tables) unless the 
user requests a modular approach.

## Input
- Single PDF file or multiple PDF files
- Provided by the user at runtime

## Output Structure
For each PDF, a subfolder is created under results/detected_figs_tables/:

results/detected_figs_tables/
└── [pdf_name]/
    ├── figures/                      ← cropped figure/plot PNGs
    ├── tables/                       ← cropped table snapshots
    ├── figures_detection_summary.json
    └── tables_detection_summary.json

## Steps

### For each PDF provided:

#### STEP 1 — Table Detection (Claude Native)
Use Claude's native PDF reading tool to parse the PDF page by page.
- Identify all table regions on each page
- For each table found:
  - Crop and save as a PNG snapshot to [pdf_name]/tables/
  - Filename format: [pdf_name]_page[N]_table[M].png
  - Record title (if present above the table), caption (if present 
    below), page number, bounding box, and resolution
- Save tables_detection_summary.json to [pdf_name]/

#### STEP 2 — Figure and Plot Detection (PyMuPDF)
Call detect_figures.py to detect all image blocks in the PDF.
- Script handles: cropping, padding, minimum size filtering, 
  saving to [pdf_name]/figures/
- Filename format: [pdf_name]_page[N]_figure[M].png
- Record title (if present), caption (if present), page number, 
  bounding box, width, height, and resolution
- Save figures_detection_summary.json to [pdf_name]/

#### STEP 3 — Print completion summary to chat
Print for each PDF:
DETECTION COMPLETE — [pdf_name]

Tables detected: X Figures detected: X Saved to: results/detected_figs_tables/[pdf_name]/

Next: Figures → /classify Tables → /table

## Output JSON Format

### figures_detection_summary.json
```json
{
  "pdf": "syn_001.pdf",
  "total_pages": 10,
  "total_figures_detected": 5,
  "figures": [
    {
      "filename": "syn_001_page2_figure1.png",
      "page": 2,
      "title": "Figure 1. Extraction efficiency vs pH",
      "caption": "Effect of pH on Nd extraction using D2EHPA",
      "bbox": [x0, y0, x1, y1],
      "width_px": 600,
      "height_px": 400,
      "resolution_dpi": 150
    }
  ]
}
```

### tables_detection_summary.json
```json
{
  "pdf": "syn_001.pdf",
  "total_pages": 10,
  "total_tables_detected": 3,
  "tables": [
    {
      "filename": "syn_001_page3_table1.png",
      "page": 3,
      "title": "Table 1. Distribution coefficients",
      "caption": "D values for Ce, La, Nd at varying pH",
      "bbox": [x0, y0, x1, y1],
      "width_px": 500,
      "height_px": 300,
      "resolution_dpi": 150
    }
  ]
}
```

## Rules
- Always process tables before figures
- Use Claude's native PDF reading for tables **only**
- Use detect_figures.py (PyMuPDF) for figures and plots **only**
- Never extract table content at this stage, snapshots and 
  metadata only
- Never overwrite existing files, append counter if filename exists
- Never install packages without asking
- All outputs go to results/detected_figs_tables/ only
- If processing multiple PDFs, complete all steps for one PDF 
  before moving to the next(no skipping any step)
- If detect_figures.py errors, report the error and ask before 
  attempting a fix

## Edge Cases — Flag These in Output
- Vector graphics figures may not be detected by PyMuPDF — 
  flag in summary if page count seems low
- Complex or borderless tables may be missed — flag if page 
  has dense text with no detected table
- Multi-page figures will be cropped as separate images — 
  flag with is_multipage: true if suspected
- Titles and captions extracted on best-effort basis — 
  flag as null if not found, never guess

## Next Step
- Figures → pass each PNG to /classify
- Tables → pass each PNG to /table
