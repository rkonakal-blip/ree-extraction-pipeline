# REE Pipeline — Full Execution Flow

**Pipeline:** REE Figure Extraction  
**Run date:** 2026-04-08  
**Input:** Single PDF  
**Extract type:** all  
**Report:** yes | **Validate:** no  

---

## Overview

```
PDF
 │
 ├─── detect.md ──────────────────► detected/figures/  (11 PNGs)
 │                                   detection_summary.json
 │
 ├─── detect_tables.md ──────────► detected/tables/   (1 PNG)
 │                                   *_table_summary.json
 │
 ├─── classify.md  (×11 figures) ─► chart_type + confidence + flags
 │
 ├─── extract.md   (×11 figures) ─► structured data (held in memory)
 │
 ├─── table.md     (×1 table)   ──► skipped — pure metadata
 │
 └─── summarise.md ──────────────► *_extracted.json
                                    *_report.html
                                    run_summary.json
```

---

## Step-by-Step Execution

### STEP 1 — Input Detection
| Field | Value |
|---|---|
| Input path | `Desktop/Research Work/recent-advances-...pdf` |
| Input type | Single PDF |
| Route | → Steps 2 + 3 (figure + table detection) |

---

### STEP 2 — Figure Detection (`detect.md`)

**Skill:** `detect.md`  
**Script:** PyMuPDF `fitz` — scans every page for image blocks (type=1)  
**Filter:** width ≥ 100 px AND height ≥ 100 px  
**Zoom:** 1.5×  
**Padding:** 20 px  
**Output folder:** `results/detected/figures/`

| File | Page | Width (px) | Height (px) |
|---|---|---|---|
| page1_figure1.png | 1 | 358 | 192 |
| page2_figure2.png | 2 | 298 | 211 |
| page2_figure3.png | 2 | 256 | 196 |
| page3_figure4.png | 3 | 537 | 534 |
| page3_figure5.png | 3 | 267 | 205 |
| page5_figure6.png | 5 | 691 | 504 |
| page6_figure7.png | 6 | 208 | 202 |
| page8_figure8.png | 8 | 358 | 376 |
| page9_figure9.png | 9 | 558 | 196 |
| page9_figure10.png | 9 | 540 | 241 |
| page11_figure11.png | 11 | 564 | 235 |

**Total detected:** 11 figures  
**Summary saved:** `detected/figures/detection_summary.json`

---

### STEP 3 — Table Detection (`detect_tables.md`)

**Skill:** `detect_tables.md`  
**Script:** PyMuPDF `page.find_tables()` — uses built-in table structure finder  
**Filter:** width ≥ 80 px AND height ≥ 40 px  
**Zoom:** 1.5×  
**Padding:** 25 px  
**Output folder:** `results/detected/tables/`

| File | Page | Width (px) | Height (px) |
|---|---|---|---|
| `..._page1_table2.png` | 1 | 361 | 88 |

**Total detected:** 1 table  
**Note:** Only 1 table region found. This was article submission metadata, not a data table (skipped in Step 5).  
**Summary saved:** `detected/tables/..._table_summary.json`

---

### STEP 4 — Figure Classification + Extraction

Each of the 11 figure PNGs was visually classified using `classify.md`, then data was extracted using the matching section of `extract.md`. All results held in memory.

#### 4a — Classification (`classify.md`)

Reasoning protocol per figure: panels → chart structure → axes → overlays → legend → domain cues.

| Figure | Classifier Output | Routing |
|---|---|---|
| page1_figure1.png | `unknown` LOW | Section H → skip |
| page2_figure2.png | `pie` HIGH | Section E |
| page2_figure3.png | `bar_grouped` MEDIUM | Section B |
| page3_figure4.png | `unknown` LOW | Section H → skip |
| page3_figure5.png | `bar_grouped` MEDIUM | Section B |
| page5_figure6.png | `multipanel` HIGH → 4× `scatter_line` LOW | Section G → Section A |
| page6_figure7.png | `bar_grouped` MEDIUM | Section B |
| page8_figure8.png | `line` MEDIUM | Section C |
| page9_figure9.png | `multipanel` HIGH → 3× `scatter_line` MEDIUM | Section G → Section A |
| page9_figure10.png | `bar_grouped` MEDIUM | Section B |
| page11_figure11.png | `multipanel` → `unknown` MEDIUM + `heatmap` LOW | Section G → H + F |

No figure was rerouted to the tables list by the classifier.

#### 4b — Extraction (`extract.md`) by section

**Section A — Scatter/scatter_line** (7 panel entries: fig 6 ×4, fig 9 ×3)
- Extracted: series name, marker, color, (x, y) points per series
- X-axis: concentration (mol/L) for fig 6; REE element sequence for fig 9
- Y-axis: %E for fig 6; log D_Ln for fig 9

**Section B — Bar grouped** (4 figures: figs 3, 5, 7, 10)
- Extracted: category labels, value-axis metadata, per-series bar values
- Fig 3: 15 REE categories × 4 mine series; broken Y-axis noted
- Fig 5: 15 years × 3 publication-type series
- Fig 7: 2 IL groups × 2 conditions; error bars recorded
- Fig 10: 6 solvent systems × 3 separation-factor series; log scale

**Section C — Line** (1 figure: fig 8)
- Extracted: 2 solubility curve series (ChCl side + urea side)
- Phase diagram with eutectic point; T vs concentration

**Section E — Other: Pie** (1 figure: fig 2)
- Extracted: 5 slices with labels and percentages; sum = 100%

**Section F — Heatmap** (1 panel: fig 11b)
- Extracted: 5×4 matrix of qualitative ratings (1–4 scale)

**Section G — Multipanel** (2 figures: figs 6, 11)
- Each panel extracted independently using the panel's own section
- Fig 6 → 4 panels (all Section A)
- Fig 9 → 3 panels (all Section A)
- Fig 11 → 2 panels (Section H + Section F)

**Section H — Unknown** (3 entries: figs 1, 4, 11a)
- No data extracted; notes recorded describing figure content

#### 4c — Validation
Skipped (Validate: no).

---

### STEP 5 — Table Extraction (`table.md`)

**1 table detected** → applied reasoning protocol from `table.md`:

| Check | Result |
|---|---|
| Numeric data present? | No — only dates and text |
| Orientation | Portrait |
| Structure | 2-row, 2-column key–value list |
| Content | Received/Revised/Accepted/Published dates + journal cover image |
| Decision | **Skipped** — pure text/metadata table |

Skipped JSON recorded:
```json
{
  "skipped": true,
  "reason": "Article submission metadata — not a data table"
}
```

---

### STEP 6 — Save All Outputs (`save_outputs.py`)

Single Python script written and executed. All data written in one batch.

#### 6a — Combined JSON
**File:** `..._extracted.json`

```
total_figures : 17   (11 source images → 17 entries after multipanel expansion)
total_tables  : 1    (skipped)
failed        : 0
```

Structure per figure entry:
```json
{
  "filename": "pageN_figureN.png",
  "page": N,
  "panel": "a",          // present only for multipanel panels
  "chart_type": "...",
  "confidence": "...",
  "data": { ... }        // full extracted JSON per extract.md schema
}
```

#### 6b — HTML Report (`summarise.md`)
**File:** `..._report.html`

- Sticky navigation bar with links to every figure/table section
- Each section: original image (base64) left | extracted data table right
- Confidence badges: green (HIGH) / orange (MEDIUM) / red (LOW)
- Chart-type badges colour-coded by type
- Heatmap cells colour-coded 1=green → 4=red
- Fully offline — no external dependencies, all images base64-encoded
- Responsive: stacks to single column on narrow screens

#### 6c — Run Summary
**File:** `run_summary.json`

```json
{
  "run_timestamp": "2026-04-08T...",
  "input": "..._pdf",
  "extract_type": "all",
  "report": true,
  "validate": false,
  "total_figures": 17,
  "total_tables": 1,
  "total_failed": 0,
  "confidence_breakdown": {"HIGH": 2, "MEDIUM": 9, "LOW": 7}
}
```

---

### STEP 7 — Documentation (this file + extraction_notes.md)

**File:** `pipeline_flow.md` — this document  
**File:** `extraction_notes.md` — per-figure caveats and decisions

---

## Skill → Output Mapping

| Skill | Input | Output |
|---|---|---|
| `detect.md` | PDF | 11 figure PNGs + `detection_summary.json` |
| `detect_tables.md` | PDF | 1 table PNG + `*_table_summary.json` |
| `classify.md` | Figure PNG | `chart_type`, `confidence`, `is_multipanel`, `panels`, flags |
| `extract.md` § A | Scatter/line PNG + classifier flags | Series + (x,y) points JSON |
| `extract.md` § B | Bar PNG + classifier flags | Series + bar values JSON |
| `extract.md` § C | Line PNG + classifier flags | Series + line points JSON |
| `extract.md` § E | Pie PNG + classifier flags | Slice labels + percentages JSON |
| `extract.md` § F | Heatmap PNG + classifier flags | Matrix + color-scale JSON |
| `extract.md` § G | Multipanel PNG + panel list | Per-panel JSONs |
| `extract.md` § H | Unknown PNG | Minimal skip JSON |
| `table.md` | Table PNG | Extraction + skip JSON |
| `summarise.md` | Combined JSON + PNGs | Scrollable HTML report |
| `orchestrate.md` | PDF + params | Coordinates all of the above |

---

## Statistics

| Metric | Value |
|---|---|
| PDF pages | 16 |
| Source figures (PNG) | 11 |
| Output figure entries (after panel expansion) | 17 |
| Multipanel source figures | 3 (figs 6, 9, 11) |
| Total panels extracted | 9 (4 + 3 + 2) |
| Tables detected | 1 |
| Tables skipped | 1 |
| Failed extractions | 0 |
| Confidence — HIGH | 2 |
| Confidence — MEDIUM | 9 |
| Confidence — LOW | 7 |
| Chart types extracted | pie, bar_grouped, scatter_line, line, heatmap, unknown |
| Chart types not seen | bar_plain, bar_stacked, contour_*, box_plot, radar, spectra, line_multiaxis |
| Validate run | No |
| Report generated | Yes |

---

## Key Scientific Content Extracted

| Figure | Scientific Significance |
|---|---|
| Fig 2 (pie) | China supplies 72% of U.S. REE imports — supply chain vulnerability |
| Fig 3 (bar_grouped) | REO composition comparison across 4 global mine deposits |
| Fig 5 (bar_grouped) | Non-aqueous solvent extraction is the dominant research category (155 pubs/yr by 2024) |
| Fig 6 (multipanel) | %E behavior under varying ionic concentration — key extraction optimization data |
| Fig 7 (bar_grouped) | C₄MIMCl outperforms C₂MIMCl in second condition (%E: 35% vs 6%) |
| Fig 8 (line) | ChCl + urea DES forms a eutectic enabling room-temp extraction |
| Figs 9a–c (scatter_line) | TODGA/TBP/IL achieves highest log D_Ln values (up to ~4.5 for heavy REE) |
| Fig 10 (bar_grouped) | TODGA/TBP/IL gives highest Lu/La separation factor (~1200) — best heavy REE selectivity |
| Fig 11a (TRL) | T-LLE at TRL 9; MS at TRL 3 — gap highlights commercialization opportunity |
| Fig 11b (heatmap) | MS scores best on water/hazardous waste; worst on material cost |
