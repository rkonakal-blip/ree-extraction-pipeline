# REE Extraction Pipeline — Agent Architecture Reference

**Project:** REE Extraction Pipeline  
**Author:** Rithika  
**Last updated:** March 2026  
**Purpose:** Reference document for the full agent architecture — classifier agents, extractor agents, and validator agent.

---

## 1. Overview

The pipeline takes a scientific figure image as input and outputs structured JSON containing the extracted data. It consists of three layers:

1. **Classifier layer** — identifies what type of plot the image is
2. **Extractor layer** — extracts data values specific to that plot type
3. **Validator layer** — checks output quality and flags issues

Each agent is a separate Python script. Agents communicate by passing JSON between them. No agent does more than one job.

---

## 2. Directory Structure

All agent scripts live under `scripts/`:

```
scripts/
├── classification/
│   ├── classifier_stage1.py        ← Coarse classifier (5 families)
│   ├── classifier_stage2a.py       ← Bar sub-classifier
│   ├── classifier_stage2b.py       ← Scatter sub-classifier
│   └── classifier_stage2c.py       ← Other sub-classifier
│
├── extraction/
│   ├── extractor_plain_bar.py
│   ├── extractor_grouped_bar.py
│   ├── extractor_stacked_bar.py
│   ├── extractor_scatter.py
│   ├── extractor_scatter_trendlines.py
│   ├── extractor_line_chart.py
│   ├── extractor_box_plot.py
│   ├── extractor_contour_map.py
│   ├── extractor_pie_chart.py
│   └── extractor_table.py
│
├── validation/
│   └── validator.py
│
├── evaluation/
│   ├── evaluate_accuracy.py        ← Computes MAE, RMSE, MAPE, R²
│   └── generate_report.py          ← Produces summary metrics table
│
└── pipeline.py                     ← Master script — runs full pipeline end to end
```

---

## 3. Classifier Layer

### Why two stages?

A single classifier distinguishing all 10 plot types at once is unreliable. Stage 1 handles visually obvious differences (bars vs dots vs boxes). Stage 2 handles subtle differences within a family (plain vs grouped vs stacked bars require closer inspection). Each classifier only ever chooses between 3–5 options.

This also makes errors traceable — if classification fails, you know whether Stage 1 or Stage 2 was responsible.

---

### Stage 1 — Coarse Classifier

**File:** `scripts/classification/classifier_stage1.py`  
**Input:** Image file path  
**Output:** JSON with coarse classification label  

**Labels it outputs:**

| Label | Meaning | Routes to |
|---|---|---|
| `bar_chart` | Any kind of bar chart | Stage 2A |
| `scatter_plot` | Scatter plot with or without trend lines | Stage 2B |
| `line_chart` | Line chart | Direct → line extractor |
| `box_plot` | Box plot | Direct → box extractor |
| `other` | Contour map, pie chart, or table | Stage 2C |

**Output format:**
```json
{
  "stage": 1,
  "label": "bar_chart",
  "confidence": 0.94,
  "image_path": "path/to/image.png"
}
```

---

### Stage 2A — Bar Sub-Classifier

**File:** `scripts/classification/classifier_stage2a.py`  
**Triggered when:** Stage 1 outputs `bar_chart`  
**Input:** Image file path  
**Output:** JSON with fine-grained bar chart label  

**Labels it outputs:**

| Label | Meaning |
|---|---|
| `plain_bar` | Single series, one bar per category |
| `grouped_bar` | Multiple series side by side per category |
| `stacked_bar` | Multiple series stacked within each bar |

**Key visual distinction cues in prompt:**
- Plain bar: one color, one bar per x-tick
- Grouped bar: multiple bars side by side per x-tick, legend present
- Stacked bar: bars divided into colored segments, always sum to total

**Output format:**
```json
{
  "stage": "2A",
  "label": "grouped_bar",
  "confidence": 0.91,
  "image_path": "path/to/image.png"
}
```

---

### Stage 2B — Scatter Sub-Classifier

**File:** `scripts/classification/classifier_stage2b.py`  
**Triggered when:** Stage 1 outputs `scatter_plot`  
**Input:** Image file path  
**Output:** JSON with scatter plot label  

**Labels it outputs:**

| Label | Meaning |
|---|---|
| `scatter_simple` | Points only, no fitted lines |
| `scatter_trendlines` | Points with one or more fitted trend lines |

**Key visual distinction cue in prompt:**
- Does the plot contain smooth continuous lines passing through/near the point cloud? If yes → trendlines.

**Output format:**
```json
{
  "stage": "2B",
  "label": "scatter_trendlines",
  "confidence": 0.88,
  "image_path": "path/to/image.png"
}
```

---

### Stage 2C — Other Sub-Classifier

**File:** `scripts/classification/classifier_stage2c.py`  
**Triggered when:** Stage 1 outputs `other`  
**Input:** Image file path  
**Output:** JSON with fine-grained label  

**Labels it outputs:**

| Label | Meaning |
|---|---|
| `contour_map` | 2D color gradient or contour lines showing a response surface |
| `pie_chart` | Circular chart divided into slices |
| `table` | Grid of rows and columns with text/numeric values |

**Output format:**
```json
{
  "stage": "2C",
  "label": "contour_map",
  "confidence": 0.97,
  "image_path": "path/to/image.png"
}
```

---

## 4. Routing Logic

After Stage 1 and Stage 2 complete, the final label maps to an extractor as follows:

| Final label | Extractor script |
|---|---|
| `plain_bar` | `extractor_plain_bar.py` |
| `grouped_bar` | `extractor_grouped_bar.py` |
| `stacked_bar` | `extractor_stacked_bar.py` |
| `scatter_simple` | `extractor_scatter.py` |
| `scatter_trendlines` | `extractor_scatter_trendlines.py` |
| `line_chart` | `extractor_line_chart.py` |
| `box_plot` | `extractor_box_plot.py` |
| `contour_map` | `extractor_contour_map.py` |
| `pie_chart` | `extractor_pie_chart.py` |
| `table` | `extractor_table.py` |

---

## 5. Extractor Layer

Each extractor receives an image and outputs a structured JSON with extracted values. All extractors share the same outer JSON envelope so the validator and evaluation scripts do not need to know which extractor was used.

### Shared output envelope (all extractors)

```json
{
  "plot_type": "grouped_bar",
  "image_path": "path/to/image.png",
  "title": "extracted chart title",
  "x_label": "extracted x-axis label",
  "y_label": "extracted y-axis label",
  "data": { ... },
  "metadata": {
    "extractor_version": "1.0",
    "confidence": 0.87,
    "notes": "any extraction notes or warnings"
  }
}
```

The `data` field varies by plot type — see individual extractor descriptions below.

---

### extractor_plain_bar.py

**Data field:**
```json
"data": {
  "bars": [
    {"label": "pH 1.5", "value": 45.3, "error": 2.1},
    {"label": "pH 2.0", "value": 67.8, "error": null}
  ]
}
```

---

### extractor_grouped_bar.py

**Data field:**
```json
"data": {
  "series": ["D2EHPA", "Cyanex 272", "PC88A"],
  "groups": [
    {
      "label": "pH 1.5",
      "bars": [
        {"series": "D2EHPA", "value": 45.3, "error": null},
        {"series": "Cyanex 272", "value": 38.1, "error": null},
        {"series": "PC88A", "value": 52.7, "error": null}
      ]
    }
  ]
}
```

---

### extractor_stacked_bar.py

**Data field:**
```json
"data": {
  "segments": ["Organic phase", "Aqueous phase", "Interfacial"],
  "bars": [
    {
      "label": "pH 1.5",
      "segments": [
        {"name": "Organic phase", "value": 45.3, "cumulative_bottom": 0.0},
        {"name": "Aqueous phase", "value": 38.1, "cumulative_bottom": 45.3},
        {"name": "Interfacial", "value": 16.6, "cumulative_bottom": 83.4}
      ]
    }
  ]
}
```

---

### extractor_scatter.py

**Data field:**
```json
"data": {
  "series": [
    {
      "name": "D2EHPA",
      "points": [
        {"x": 1.5, "y": 45.3},
        {"x": 2.0, "y": 67.8}
      ]
    }
  ]
}
```

---

### extractor_scatter_trendlines.py

**Data field:**
```json
"data": {
  "series": [
    {
      "name": "D2EHPA",
      "points": [{"x": 1.5, "y": 45.3}],
      "trend_type": "linear",
      "trend_coefficients": [12.4, 23.1],
      "r_squared": 0.96
    }
  ]
}
```

---

### extractor_line_chart.py

**Data field:**
```json
"data": {
  "series": [
    {
      "name": "D2EHPA",
      "points": [{"x": 1.5, "y": 45.3}, {"x": 2.0, "y": 67.8}]
    }
  ]
}
```

---

### extractor_box_plot.py

**Data field:**
```json
"data": {
  "boxes": [
    {
      "group_label": "pH 1.5",
      "series_label": null,
      "stats": {
        "minimum": 38.2,
        "q1": 44.1,
        "median": 51.3,
        "q3": 58.7,
        "maximum": 64.9,
        "outliers": [72.3, 31.1]
      }
    }
  ]
}
```

---

### extractor_contour_map.py

**Data field:**
```json
"data": {
  "x_range": [1.0, 4.0],
  "y_range": [0.1, 2.0],
  "z_range": [20.0, 95.0],
  "colorbar_label": "Extraction Efficiency (%)",
  "contour_levels": [20, 30, 40, 50, 60, 70, 80, 90],
  "optimal_point": {"x": 2.8, "y": 1.2, "z": 94.3}
}
```

---

### extractor_pie_chart.py

**Data field:**
```json
"data": {
  "slices": [
    {"label": "La", "percentage": 28.4},
    {"label": "Ce", "percentage": 35.2},
    {"label": "Nd", "percentage": 21.7},
    {"label": "Pr", "percentage": 9.3},
    {"label": "Others", "percentage": 5.4}
  ],
  "total": 100.0
}
```

---

### extractor_table.py

**Data field:**
```json
"data": {
  "headers": ["pH", "Extraction (%)", "D value"],
  "rows": [
    ["1.5", "45.3", "0.83"],
    ["2.0", "67.8", "2.11"]
  ]
}
```

---

## 6. Validator Agent

**File:** `scripts/validation/validator.py`  
**Input:** JSON output from any extractor  
**Output:** Validated JSON with a `validation` block appended  

The validator checks:
- All required fields are present in the output envelope
- Numeric values fall within realistic REE extraction ranges
- Percentages sum correctly (stacked bars, pie charts)
- No null values in critical fields (title, x_label, y_label)
- Confidence score from the extractor is above threshold (default 0.7)

**Validation output block appended to extractor JSON:**
```json
"validation": {
  "passed": true,
  "confidence_ok": true,
  "issues": [],
  "flagged": false
}
```

If `flagged: true`, the pipeline logs the image for manual review rather than passing it to the evaluation script.

---

## 7. Master Pipeline Script

**File:** `scripts/pipeline.py`  
**Purpose:** Runs the full pipeline end to end for a single image or a folder of images.

**Usage:**
```bash
# Single image
python scripts/pipeline.py --input benchmark/bar_charts/plain/barplot1.png

# Full folder
python scripts/pipeline.py --input benchmark/bar_charts/plain/ --output results/plain_bar/
```

**What it does:**
1. Calls Stage 1 classifier
2. Calls Stage 2 sub-classifier if needed
3. Routes to correct extractor
4. Runs validator on output
5. Saves result JSON to `results/` folder
6. Logs any flagged images to `results/flagged.log`

---

## 8. Evaluation Scripts

**File:** `scripts/evaluation/evaluate_accuracy.py`  
**Purpose:** Compares extracted JSON against ground truth MD files and computes accuracy metrics.

**Metrics computed per plot type:**
- MAE — Mean Absolute Error
- RMSE — Root Mean Square Error
- MAPE — Mean Absolute Percentage Error
- R² — Coefficient of determination

**File:** `scripts/evaluation/generate_report.py`  
**Purpose:** Produces a summary table across all plot types showing accuracy metrics side by side. Output is saved to `results/evaluation_summary.csv`.

---

## 9. Build Order

When coding, build in this order:

1. `classifier_stage1.py` — test against all benchmark images before moving on
2. `classifier_stage2a.py`, `2b.py`, `2c.py`
3. `extractor_plain_bar.py` — simplest extractor, good starting point
4. `extractor_grouped_bar.py`, `extractor_stacked_bar.py`
5. `extractor_scatter.py`, `extractor_scatter_trendlines.py`
6. `extractor_line_chart.py`, `extractor_box_plot.py`
7. `extractor_contour_map.py`, `extractor_pie_chart.py`, `extractor_table.py`
8. `validator.py`
9. `pipeline.py`
10. `evaluate_accuracy.py`, `generate_report.py`

---

## 10. Technology Stack

| Component | Technology |
|---|---|
| Language | Python 3.10+ |
| Claude API | `anthropic` Python SDK |
| Image handling | `Pillow` (PIL) |
| JSON validation | `pydantic` |
| Evaluation metrics | `numpy`, `scikit-learn` |
| Output format | JSON |

---

*This document is the reference architecture for the REE Extraction Pipeline. Update it as the design evolves.*
