# REE Pipeline — Master Orchestrator
**Pipeline:** REE Figure Extraction  
**Phase:** Master  
**Input:** Single PDF, single image, or folder of PDFs/images  
**Output:** Single combined JSON + optional combined HTML report

---

## Task

You are the master orchestrator for the REE Figure Extraction pipeline. Given an input path and extract type, run the full pipeline end to end — detect, classify, extract — and save all outputs into a single combined JSON file per paper. Handles single files and batch folders.

---

## Inputs required from user

1. **Input path** — path to a single PDF, single image, or a folder containing PDFs/images
2. **Extract type** — `plots`, `tables`, or `all`
3. **Output folder** — where to save all outputs
4. **Report** — `yes` or `no` (default: `yes`) — whether to generate combined HTML report
5. **Validate** — `yes` or `no` (default: `no`) — whether to run validation (requires ground truth)

The skills folder is always: the same folder as this orchestrate.md file.

---

## STEP 1 — Detect input type

Check the input path:
- **Single `.pdf`** → PDF input, run detection first (go to Step 2)
- **Single image** (`.png`, `.jpg`, `.jpeg`, `.tiff`) → single image input, skip detection (go to Step 4)
- **Folder** → batch mode: collect all PDFs and images in the folder, process each one sequentially through Steps 2–6. Create a subfolder per file: `OUTPUT_FOLDER/FILENAME/`. After all files done, print combined batch summary.

---

## STEP 2 — Detect figures (PDF only, if extract type is `plots` or `all`)

Read and follow the instructions in `detect.md`.

Apply to the input PDF with:
- Output folder: `OUTPUT_FOLDER/detected/figures/`
- Zoom: **2x**

Record the list of detected figure PNGs from the detection summary JSON.

---

## STEP 3 — Detect tables (PDF only, if extract type is `tables` or `all`)

Read and follow the instructions in `detect_tables.md`.

Apply to the input PDF with:
- Output folder: `OUTPUT_FOLDER/detected/tables/`
- Zoom: **2x**

Record the list of detected table PNGs from the detection summary JSON.

---

## STEP 4 — Process all figures

### 4a — Classify all figures
For each figure PNG, read and follow `classify.md`. Record all classifier outputs in memory. Route any figure classified as `table` to the tables list for Step 5.

### 4b — Extract all figures
For each figure, read and follow `extract.md`, jumping to the matching section:

| chart_type | Section in extract.md |
|---|---|
| `scatter`, `scatter_line` | Section A |
| `bar_plain`, `bar_grouped`, `bar_stacked` | Section B |
| `line`, `line_multiaxis`, `spectra` | Section C |
| `contour_filled`, `contour_line`, `contour_overlaid` | Section D |
| `box_plot`, `pie`, `radar` | Section E |
| `heatmap` | Section F |
| `multipanel` | Section G |
| `unknown` | Section H |

Pass classifier `is_mixed`, `is_multipanel`, `panels`, `special_additions` flags to extractor.
**Hold all extracted data in memory — do not write individual JSON files.**

### 4c — Validate (only if `Validate: yes`)
For each figure, read and follow `validate_charts.md`. Hold results in memory.

---

## STEP 5 — Process all tables

For each table PNG (from Step 3 or classified as `table` in Step 4):
Read and follow `table.md`. **Hold results in memory — do not write individual files.**

---

## STEP 6 — Save all outputs in one batch

Write a **single Python script** that saves everything at once — no separate scripts per figure.

### 6a — Combined JSON
`OUTPUT_FOLDER/PAPER_NAME_extracted.json`

```json
{
  "source": "<PDF filename>",
  "extract_type": "<plots | tables | all>",
  "total_figures": <integer>,
  "total_tables": <integer>,
  "figures": [
    {
      "filename": "<string>",
      "page": <integer>,
      "chart_type": "<label>",
      "confidence": "<HIGH | MEDIUM | LOW>",
      "data": { ... }
    }
  ],
  "tables": [
    {
      "filename": "<string>",
      "page": <integer>,
      "confidence": "<HIGH | MEDIUM | LOW>",
      "data": { ... }
    }
  ],
  "failed": [
    {"filename": "<string>", "reason": "<string>"}
  ]
}
```

### 6b — Combined HTML report (only if `Report: yes`)
Read and follow `summarise.md` to generate one single scrollable HTML report:
`OUTPUT_FOLDER/PAPER_NAME_report.html`

Shows all figures and tables — each with original image left, extracted data right.

### 6c — Run summary
`OUTPUT_FOLDER/run_summary.json`

---

## STEP 7 — Print completion message

Single file:
```
==================================================
REE PIPELINE — RUN COMPLETE
==================================================
Input:            FILENAME
Extract type:     all
Report:           yes/no
--------------------------------------------------
Figures detected: X
Tables detected:  X
Failed:           X
--------------------------------------------------
Output: OUTPUT_FOLDER/PAPER_NAME_extracted.json
==================================================
```

Batch folder:
```
==================================================
REE PIPELINE — BATCH RUN COMPLETE
==================================================
Input folder:     FOLDER_PATH
Files processed:  X
--------------------------------------------------
Total figures:    X
Total tables:     X
Total failed:     X
--------------------------------------------------
Outputs saved to: OUTPUT_FOLDER/
==================================================
```

---

## Critical Rules

- **Write one Python script for all saving in Step 6** — never one script per figure
- **Hold all extracted data in memory** until Step 6 — write files once at the end
- **Default: HTML report yes, validation no** — skip validation unless explicitly set to `yes`
- **Zoom 1.5x for all PDF rendering** — not 2x
- Never stop on errors — log in `failed` and continue
- Always pass classifier flags to extractor — never re-detect
- For multipanel figures, each panel is a separate entry under `figures` in the combined JSON
- For single image input, skip Steps 2 and 3
- For `extract_type = plots`, skip Steps 3 and 5
- For `extract_type = tables`, skip Steps 2 and 4
- For batch mode, create subfolder per input file: `OUTPUT_FOLDER/FILENAME/`
- Always save combined JSON before ending the session
