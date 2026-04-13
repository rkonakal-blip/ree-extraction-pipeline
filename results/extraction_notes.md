# Extraction Notes — REE Recovery Paper

**Paper:** Recent Advances in Rare Earth Element Recovery: Liquid-Liquid Extraction and Magnetophoretic Separation  
**PDF:** `recent-advances-in-rare-earth-element-recovery-liquid-liquid-extraction-and-magnetophoretic-separation.pdf`  
**Run date:** 2026-04-08  
**Extract type:** all  
**Total pages:** 16  

---

## Detection Summary

| Type | Count | Folder |
|---|---|---|
| Figures detected | 11 | `detected/figures/` |
| Tables detected | 1 | `detected/tables/` |
| Zoom used | 1.5× | — |
| Padding (figures) | 20 px | — |
| Padding (tables) | 25 px | — |

---

## Figure Index

| # | File | Page | Chart Type | Confidence | Notes |
|---|---|---|---|---|---|
| 1 | page1_figure1.png | 1 | `unknown` | LOW | Process schematic — Traditional LLE vs Modified LLE variants |
| 2 | page2_figure2.png | 2 | `pie` | HIGH | REE import sources into U.S. — 5 slices, China dominant at 72% |
| 3 | page2_figure3.png | 2 | `bar_grouped` | MEDIUM | REO compositions (wt%) for 4 mines × 15 REE elements; broken Y-axis |
| 4 | page3_figure4.png | 3 | `unknown` | LOW | Molecular structure diagrams for 8 LLE ligands |
| 5 | page3_figure5.png | 3 | `bar_grouped` | MEDIUM | Publications per year (2010–2024) across 3 solvent extraction categories |
| 6a | page5_figure6.png — Panel a | 5 | `scatter_line` | LOW | %E vs concentration — decreasing trend |
| 6b | page5_figure6.png — Panel b | 5 | `scatter_line` | LOW | %E vs concentration — increasing trend |
| 6c | page5_figure6.png — Panel c | 5 | `scatter_line` | LOW | %E vs concentration — rising from low baseline |
| 6d | page5_figure6.png — Panel d | 5 | `scatter_line` | LOW | %E vs concentration — high-start declining |
| 7 | page6_figure7.png | 6 | `bar_grouped` | MEDIUM | Ionic liquid (C₄MIMCl vs C₂MIMCl) effect on %E; error bars present |
| 8 | page8_figure8.png | 8 | `line` | MEDIUM | Binary phase diagram for ChCl + urea DES system; includes photo strip |
| 9a | page9_figure9.png — Panel A | 9 | `scatter_line` | MEDIUM | log D_Ln vs REE — TODGA/TBP and TODGA/DCE |
| 9b | page9_figure9.png — Panel B | 9 | `scatter_line` | MEDIUM | log D_Ln vs REE — TODGA/TBP/IL and TODGA/TBP/nonane |
| 9c | page9_figure9.png — Panel C | 9 | `scatter_line` | MEDIUM | log D_Ln vs REE — TODGA/IL/DCE and TODGA/IL |
| 10 | page9_figure10.png | 9 | `bar_grouped` | MEDIUM | Separation factors Lu/La, Lu/Sm, Lu/Tb — log-scale Y-axis |
| 11a | page11_figure11.png — Panel a | 11 | `unknown` | MEDIUM | TRL arrow diagram — estimated TRL levels per technology |
| 11b | page11_figure11.png — Panel b | 11 | `heatmap` | LOW | Categorical env./economic ratings for 5 technologies × 4 metrics |

---

## Table Index

| # | File | Page | Status | Notes |
|---|---|---|---|---|
| 1 | `..._page1_table2.png` | 1 | Skipped | Article metadata (submission dates + journal cover), not a data table |

---

## Confidence Summary

| Confidence | Count | Items |
|---|---|---|
| HIGH | 2 | Fig 2 (pie), Table 1 (skip) |
| MEDIUM | 9 | Figs 3, 5, 7, 8, 9a, 9b, 9c, 10, 11a |
| LOW | 7 | Figs 1, 4, 6a, 6b, 6c, 6d, 11b |

---

## Extraction Decisions & Caveats

### Figures 1 and 4 — `unknown`
Both are non-quantitative. Fig 1 is a conceptual process diagram; Fig 4 shows chemical structures. No data extractable.

### Figure 3 — Broken Y-axis
The REO composition chart has a discontinuous Y-axis: the main scale covers 0–50 wt% for major REE (La, Ce, Nd), while minor REE (Sm through Y) fall below 0.4 wt%. Values for heavy REE are MEDIUM confidence due to the compressed lower scale range.

### Figure 6 — Multipanel (4 panels, LOW confidence)
The source PNG is 461×336 px (rendered at 1.5× from PDF). Each of the 4 sub-panels is approximately 230×168 px — insufficient to read exact axis labels or series labels. X-axis variable identity could not be confirmed from the image. Values are approximate and should be treated as structural trend estimates only.

### Figure 8 — Phase diagram with embedded photos
Panel (a) of Figure 7 in the paper. The upper portion of the image contains photographs of test tube samples; the phase diagram is in the lower portion. Temperature and composition axis ranges are estimated. The eutectic point (E) coordinates are approximate.

### Figures 9a/9b/9c — log D_Ln series
The three panels of Figure 8(a) in the paper. Y-axis is log scale ranging from −1 to 5. Values read by visual interpolation between gridlines. Trend direction (monotonically increasing from light to heavy REE) is confirmed HIGH confidence; individual point values are MEDIUM.

### Figure 10 — Log-scale separation factors
Figure 8(b) in the paper. Y-axis spans 0.1–1000 on a log scale. Values estimated by log interpolation. TODGA/TBP/IL system shows highest Lu/La separation factor (~1200), consistent with the paper's key finding.

### Figure 11b — Heatmap ratings (LOW confidence)
Colors represent qualitative ratings (best=1/blue → worst=4/red). Exact color mapping was estimated visually at low image resolution. These values are categorical estimates and should not be treated as quantitative data.

---

## Output Files

| File | Description |
|---|---|
| `..._extracted.json` | Combined extraction JSON — all figures + tables |
| `..._report.html` | Scrollable HTML report — images + data side by side |
| `run_summary.json` | Run metadata and confidence breakdown |
| `extraction_notes.md` | This file |
| `pipeline_flow.md` | Full pipeline execution trace |
| `detected/figures/` | 11 cropped figure PNGs |
| `detected/tables/` | 1 cropped table PNG |
| `detected/figures/detection_summary.json` | Figure detection metadata |
| `detected/tables/..._table_summary.json` | Table detection metadata |
