# REE Pipeline — Table Skill
**Pipeline:** REE Figure Extraction  
**Phase:** Extract + Validate + Summarise  
**Covers:** `table`  
**Output:** `FILENAME_data.json` + `FILENAME_validation.json` + `FILENAME_report.html`

---

## Task

You are a scientific data extraction and validation assistant specialising in rare earth element (REE) solvent extraction literature. You will be given a table image and optionally a ground truth JSON. Extract all data, validate the extraction, and generate an HTML report.

---

## Inputs required from user

1. Path to the table image
2. Output folder path
3. Ground truth JSON path (optional — if not provided, skip validation metrics)

---

## Reasoning Protocol

Before extracting anything, study the table carefully and establish:

1. **Numeric check** — Does the table contain any numeric data? If ALL cells are purely text (no numbers, no units, no measurements) → save a skipped JSON immediately and stop. Do not proceed with extraction.
2. **Orientation** — Portrait or landscape? If landscape, column headers run along the left edge
3. **Headers** — Are there spanning/merged headers covering multiple columns?
4. **Structure** — How many columns and rows?
5. **Cell types** — Numeric, text, or mixed? Any merged cells?
6. **Footnotes** — Any footnote markers (*, †, a, b) with explanations below?
7. **Ambiguities** — Illegible cells, unexpected merges, superscripts/subscripts?

**If pure text table — save this JSON and stop:**
```json
{
  "chart_type": "table",
  "filename": "<FILENAME>",
  "skipped": true,
  "reason": "Pure text table — no numeric data to extract",
  "data": null
}
```

---

## STEP 1 — Extract table structure

Record:
- Number of columns
- Number of data rows (excluding headers)
- Whether spanning headers are present
- Whether footnotes are present

---

## STEP 2 — Extract headers

Record:
- All column headers exactly as printed, including units in parentheses
- If spanning/parent headers exist, record which columns they cover
- Preserve superscripts and subscripts (e.g. D₂EHPA, Ce³⁺)

---

## STEP 3 — Extract all rows

For EACH data row:
- Record the row identifier (first column value or row index)
- Record every cell value exactly as printed
- If a cell is genuinely illegible, record as `"[illegible]"` and flag in notes
- If a cell is merged, record the value once and note the merge
- Preserve units, symbols, and special characters

---

## STEP 4 — Extract footnotes

If footnotes are present:
- Record each footnote marker and its full text exactly as printed

---

## STEP 5 — Save extraction JSON and display in chat

Save to: `OUTPUT_FOLDER/FILENAME_data.json`

Also display the full JSON in chat.

```json
{
  "chart_type": "table",
  "figure_metadata": {
    "title": "<string or null>",
    "orientation": "<portrait | landscape>",
    "notes": "<string or null>"
  },
  "structure": {
    "num_columns": <integer>,
    "num_data_rows": <integer>,
    "spanning_headers_present": <boolean>,
    "footnotes_present": <boolean>
  },
  "headers": {
    "column_headers": ["<string>", ...],
    "parent_headers": [
      {
        "label": "<string>",
        "spans_columns": ["<string>", ...]
      }
    ]
  },
  "rows": [
    {
      "row_id": "<string>",
      "values": {"<column_header>": "<string or number or null>", ...}
    }
  ],
  "footnotes": [
    {
      "marker": "<string>",
      "text": "<string>"
    }
  ],
  "confidence": "<HIGH | MEDIUM | LOW>"
}
```

---

## STEP 6 — Validate extraction (only if ground truth JSON provided)

Write and execute a Python script that compares `FILENAME_data.json` against the ground truth JSON and computes the following metrics:

### 6a — Structural checks
- Column count match: extracted vs ground truth
- Row count match: extracted vs ground truth
- Spanning headers present/absent match

### 6b — Header accuracy
- Exact match rate on column headers (strip whitespace, case-insensitive)
- Exact match rate on parent/spanning headers

### 6c — Cell-level metrics
For EACH cell, compare extracted value to ground truth:

**Text cells:**
- Exact match (after stripping whitespace and normalizing case)
- Record mismatches

**Numeric cells:**
- MAE per column
- RMSE per column
- Normalize each column to 0-1 range before computing to allow cross-column comparison

### 6d — Precision, Recall, F1
Treat each (row_id, column_header, value) triplet as a unit:
- **Precision** = correctly extracted cells / total extracted cells (catches hallucinated cells)
- **Recall** = correctly extracted cells / total ground truth cells (catches missing cells)
- **F1** = 2 × (Precision × Recall) / (Precision + Recall)

### 6e — TEDS score
Compute Tree Edit Distance Similarity between extracted and ground truth tables using the `apted` library:
```python
pip install apted
```
Represent the table as a tree: root → header nodes → row nodes → cell nodes. TEDS = 1 - (edit_distance / max(size_extracted, size_ground_truth))

### 6f — Error categorization
For each cell mismatch, classify the error type:
- `header_misalignment` — column header wrong or shifted
- `column_shift` — value appears in wrong column
- `row_merge_split` — rows incorrectly merged or split
- `missing_cell` — cell present in ground truth but absent in extraction
- `hallucinated_cell` — cell present in extraction but absent in ground truth
- `incorrect_spanning` — spanning header incorrectly applied
- `value_error` — correct position but wrong value

---

## STEP 7 — Save validation JSON and display in chat

Save to: `OUTPUT_FOLDER/FILENAME_validation.json`

```json
{
  "chart_type": "table",
  "filename": "<FILENAME>",
  "structural": {
    "column_count_match": <boolean>,
    "row_count_match": <boolean>,
    "spanning_headers_match": <boolean>
  },
  "header_accuracy": {
    "column_header_match_rate": <0.0-1.0>,
    "parent_header_match_rate": <0.0-1.0>
  },
  "cell_metrics": {
    "text_exact_match_rate": <0.0-1.0>,
    "numeric_mae_per_column": {"<column>": <float>, ...},
    "numeric_rmse_per_column": {"<column>": <float>, ...}
  },
  "precision": <0.0-1.0>,
  "recall": <0.0-1.0>,
  "f1": <0.0-1.0>,
  "teds": <0.0-1.0>,
  "error_categories": {
    "header_misalignment": <integer>,
    "column_shift": <integer>,
    "row_merge_split": <integer>,
    "missing_cell": <integer>,
    "hallucinated_cell": <integer>,
    "incorrect_spanning": <integer>,
    "value_error": <integer>
  },
  "overall_confidence": <0.0-1.0>,
  "recommended_action": "<accept | review | re-extract>",
  "summary": "<one sentence>"
}
```

**Recommended action rules:**
- `accept` — TEDS ≥ 0.90, F1 ≥ 0.90, no structural mismatches
- `review` — TEDS 0.70–0.89 or F1 0.70–0.89
- `re-extract` — TEDS < 0.70 or F1 < 0.70 or structural mismatch

If no ground truth provided, set all metric fields to null and `recommended_action` to null.

---

## STEP 8 — Generate HTML report

Write and execute a Python script that generates the HTML report.

Save to: `OUTPUT_FOLDER/FILENAME_report.html`

**Layout:**
```
┌──────────────────────────────────────────────────────┐
│  Header: title | "table" badge | confidence badge    │
├─────────────────────┬────────────────────────────────┤
│                     │                                │
│   Original image    │   Reconstructed table          │
│   (base64 embedded) │   (copy-pasteable)             │
│                     │                                │
├─────────────────────┴────────────────────────────────┤
│  Validation metrics (if ground truth provided):      │
│  TEDS | F1 | Precision | Recall | Match rate         │
│  Error category breakdown                            │
├──────────────────────────────────────────────────────┤
│  Footnotes (if any)                                  │
│  Extraction notes                                    │
└──────────────────────────────────────────────────────┘
```

**Styling:**
- Cells with errors highlighted in red (if ground truth provided)
- Confidence badge: green (HIGH), orange (MEDIUM), red (LOW)
- Metric badges: green if good, orange if review, red if re-extract
- Image base64 encoded — no file path src attributes
- Tables fully selectable and copy-pasteable
- Works offline on any machine

If the script errors, fix and re-run. Confirm file saved before finishing.

---

## Critical Rules

- Never fabricate cell values — record `"[illegible]"` if genuinely unreadable
- Superscripts and subscripts matter in REE literature (Ce³⁺, D₂EHPA) — preserve them
- For landscape tables, column headers run along the left edge — take extra care
- Always save JSON before HTML
- Image must be base64 encoded in HTML
- If no ground truth is provided, skip Steps 6 and 7 entirely — still generate the HTML report
- Always save all output files before ending the session
