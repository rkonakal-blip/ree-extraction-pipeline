# Figure and Plot Data Extraction

## Purpose
Third stage of the REE extraction pipeline for figures and plots.
Given a cropped figure image and the classifier output JSON, extract
all underlying data and save as structured JSON. Do not classify —
extraction only.

## Input

### Modular Mode (called directly via /extract without /orchestrate)
When /extract is called directly, this is a modular run.
- Ask the user for:
  1. Path to the figure image (PNG)
  2. Chart type label directly — do not look for a classifier JSON
  3. Output folder path — if not provided, save to results/ by default
- Supported labels: bar_plain, bar_grouped, bar_stacked, scatter,
  scatter_line, line, line_multiaxis, spectra, contour_filled,
  contour_line, contour_overlaid, box_plot, pie, radar, heatmap,
  multipanel, unknown

### Pipeline Mode (called via /orchestrate)
When /extract is called as part of the pipeline:
- Input image: results/detected_figs_tables/[pdf_name]/figures/[filename].png
- Classifier JSON: results/detected_figs_tables/[pdf_name]/[filename]_classified.json
- Read chart_type from classifier JSON — do not ask the user
- Output: results/detected_figs_tables/[pdf_name]/[filename]_extracted.json

## How to Use This File
1. Read the classifier output JSON fully before doing anything else
2. Run ALL pre-extraction checks in order — do not skip any
3. Only after all checks are complete, jump to the matching section
4. Follow only that section's instructions
5. Save output and print to chat

## Output Save
Save to: `results/detected_figs_tables/[pdf_name]/[filename]_extracted.json`
Print full JSON to chat after saving.

---

## PRE-EXTRACTION CHECKS — Run ALL of These Before Any Section

These checks apply to EVERY figure regardless of chart type,
including multipanel. Do not skip any check for any reason.

### Check 1 — Multipanel Flag
Read the classifier output JSON.
- Note the value of `is_multipanel`
- If `is_multipanel: true` → note this for later, still complete
  Checks 2, 3, and 4 fully before doing anything else
- If `is_multipanel: false` → continue to Check 2
- Do NOT jump to Section G yet — complete all checks first
- The multipanel flag only determines which section to run, not
  whether the pre-extraction checks apply

### Check 2 — Resolution
Examine the image carefully before extracting anything.
- If the image is clearly low resolution (blurry text, pixelated
  axes, unreadable tick labels, indistinguishable markers) →
  set `"resolution_flag": true` in output JSON
  add a note in `figure_metadata.notes` describing what is unclear
- If the image is clear and readable → set `"resolution_flag": false`
- Still attempt extraction regardless of resolution — never skip
  extraction solely due to low resolution
- Flag every value that had to be approximated due to low resolution
  with `"approximated": true` at the point level

### Check 3 — Context
Before reading any data, read the figure for context:
1. Read the figure title if present — record in `figure_metadata.title`
2. Read the figure caption if present — record in `figure_metadata.caption`
3. Identify the REE context:
   - Which elements are being studied? (Ce, La, Nd, Pr, Sm, Eu...)
   - What are the process variables? (pH, temperature, concentration...)
   - What extraction system? (D2EHPA, Cyanex, TBP...)
   - What is being measured? (D value, extraction efficiency, 
     separation factor...)
4. Record any relevant context in `figure_metadata.notes`
5. Use this context to guide axis label interpretation and
   sanity checking of extracted values

### Check 4 — Routing
After completing Checks 1, 2, and 3:
- If `is_multipanel: true` → go to Section G
- Otherwise, read `chart_type` from classifier JSON and go to
  the matching section:
  - `scatter` or `scatter_line` → Section A
  - `bar_plain`, `bar_grouped`, `bar_stacked` → Section B
  - `line`, `line_multiaxis`, `spectra` → Section C
  - `contour_filled`, `contour_line`, `contour_overlaid` → Section D
  - `box_plot`, `pie`, `radar` → Section E
  - `heatmap` → Section F
  - `multipanel` → Section G
  - `unknown` → Section H

### Check 5 — Confidence (run AFTER extraction is complete)
After extracting all data, assign a confidence score:
- `confidence` — float between 0.0 and 1.0
- `confidence_level`:
  - HIGH if >= 0.85 — all data clearly readable, no ambiguity
  - MEDIUM if 0.60–0.84 — mostly readable, minor ambiguity
  - LOW if below 0.60 — significant uncertainty, many approximations
- If LOW → add `"flag": "low confidence — recommend human review"`
  to the output JSON

---

## SECTION A — Scatter (`scatter`, `scatter_line`)

### Reasoning Protocol
1. **Series** — How many distinct data series? Identify by marker
   shape, colour, legend
2. **Axes** — X and Y labels, units, scale (linear/log), range
3. **Mixed type** — Are trendlines overlaid? Check `is_mixed` flag
4. **Special additions** — Error bars, annotations, reference lines?
5. **Ambiguities** — Overlapping or crowded points?

### STEP 1 — Extract axis metadata
For both axes record: label, unit, scale, range [min, max],
tick values array.
Map out all visible gridlines before reading any data points.

### STEP 2 — Extract series one at a time
For EACH series, complete fully before moving to the next:
- Identify series name from legend
- Note marker shape and colour
- Extract every visible (x, y) point left to right
- **For `scatter` (no connecting lines): treat each marker dot as
  an independent data point. Do NOT fit a curve, smooth, or
  interpolate — record the exact (x, y) position of every individual
  marker as it appears, including scattered or clustered points.
  Never replace individual points with a trend line approximation.**
- Round to 3 significant figures
- For log-scale axes, interpolate carefully
- Do NOT skip overlapping points — note overlap in metadata
- After completing a series, sanity check: does the number of
  extracted points match the number of visible markers in the image?
- Only move to the next series after current one is complete

### STEP 3 — Extract trendlines (only if `is_mixed: true`)
For each trendline:
- Associate with series by colour
- Record polynomial coefficients if equation is printed
- Record R² if printed
- If no equation printed, coefficients = null
- If `is_mixed: false`, skip this step entirely

### STEP 4 — Extract special additions
- `error_bars` — ± value per point per series, asymmetric:
  record upper and lower separately
- `annotations` — text labels, R², equations as strings
- `reference_line` — axis, value, label
Set anything not present to null.

### STEP 5 — Save JSON and display in chat

```json
{
  "chart_type": "scatter",
  "figure_metadata": {
    "title": "<string or null>",
    "caption": "<string or null>",
    "notes": "<string or null>",
    "resolution_flag": <true | false>
  },
  "axes": {
    "x": {"label": "<string>", "unit": "<string or null>",
          "scale": "<linear|log>", "range": [<min>, <max>],
          "ticks": [...]},
    "y": {"label": "<string>", "unit": "<string or null>",
          "scale": "<linear|log>", "range": [<min>, <max>],
          "ticks": [...]}
  },
  "data": {
    "series": [
      {
        "name": "<string>",
        "marker": "<shape>",
        "color": "<string>",
        "points": [{"x": <float>, "y": <float>,
                    "approximated": <true|false>}]
      }
    ]
  },
  "special_additions": {
    "error_bars": [{"series_name": "<string>",
                    "values": [{"x": <float>,
                                "error_plus": <float>,
                                "error_minus": <float>}]}],
    "trendline": [{"series_name": "<string>",
                   "coefficients": [<float>],
                   "r_squared": <float or null>}],
    "annotations": ["<string>"],
    "reference_line": {"axis": "<x|y>", "value": <float>,
                       "label": "<string or null>"}
  },
  "confidence": <float 0.0-1.0>,
  "confidence_level": "<HIGH|MEDIUM|LOW>"
}
```

---

## SECTION B — Bar (`bar_plain`, `bar_grouped`, `bar_stacked`)

### Reasoning Protocol
1. **Subtype** — Plain (one value per category), grouped (multiple
   series side by side), stacked (segments stacked)
2. **Orientation** — Vertical or horizontal?
3. **Axes** — Category axis and value axis labels, units, scale, range
4. **Series/segments** — Identify by colour, hatch, legend
5. **Special additions** — Error bars, annotations, reference lines?
6. **Ambiguities** — Short bars, log scale, similar colours?

### STEP 1 — Extract axis metadata
Category axis: label, unit, all category labels in order.
Value axis: label, unit, scale, range [min, max], tick values.

Before reading any bar heights, explicitly map out the gridlines:
- List every visible gridline value (e.g. 0, 50, 100, 150, 200)
- Calculate the pixel height per unit — this is your ruler for
  all subsequent readings

### STEP 2 — Extract bar values one series at a time
For EACH series, complete fully before moving to the next:
- Identify series name from legend, note colour
- For EACH bar in this series, left to right:
  - Locate the top edge of the bar — the highest point of the bar,
    not the middle
  - Draw an imaginary horizontal line from the bar top to the y-axis
  - Read the y-axis value at the exact point where that line meets
    the y-axis
  - If the line meets the y-axis between two tick marks, estimate
    proportionally based on its position between them
    (e.g. bar top is 30% of the way between tick 40 and tick 50
    → value is 43)
  - Never round up to the nearest tick mark — always read the
    exact position
  - For narrow bars, be extra careful to trace straight across
    horizontally — do not angle the line
  - Record value rounded to 3 significant figures
- After completing all bars in a series, sanity check: does the
  trend look visually consistent with what you extracted?
- Only move to the next series after current one is complete

For `bar_stacked`: record each segment's own value (not cumulative)
+ cumulative bottom, list bottom to top.

### STEP 3 — Extract special additions
- `error_bars` — ± per bar, asymmetric: upper and lower separately
- `annotations` — text labels, significance markers (*, **)
- `reference_line` — axis, value, label
Set anything not present to null.

### STEP 4 — Save JSON and display in chat

```json
{
  "chart_type": "<bar_plain|bar_grouped|bar_stacked>",
  "figure_metadata": {
    "title": "<string or null>",
    "caption": "<string or null>",
    "orientation": "<vertical|horizontal>",
    "notes": "<string or null>",
    "resolution_flag": <true | false>
  },
  "axes": {
    "category": {"label": "<string>", "unit": "<string or null>",
                 "categories": ["<string>"]},
    "value": {"label": "<string>", "unit": "<string or null>",
              "scale": "<linear|log>", "range": [<min>, <max>],
              "ticks": [...]}
  },
  "data": {
    "series": [
      {
        "name": "<string>",
        "color": "<string>",
        "bars": [{"category": "<string>", "value": <float>,
                  "cumulative_bottom": <float or null>,
                  "approximated": <true|false>}]
      }
    ]
  },
  "special_additions": {
    "error_bars": [{"series_name": "<string>",
                    "values": [{"category": "<string>",
                                "error_plus": <float>,
                                "error_minus": <float>}]}],
    "annotations": ["<string>"],
    "reference_line": {"axis": "<category|value>",
                       "value": <float>,
                       "label": "<string or null>"}
  },
  "confidence": <float 0.0-1.0>,
  "confidence_level": "<HIGH|MEDIUM|LOW>"
}
```

Rules: `cumulative_bottom` is null for plain/grouped, sum of
segments below for stacked.

---

## SECTION C — Line (`line`, `line_multiaxis`, `spectra`)

### Reasoning Protocol
1. **Subtype** — Standard line, dual Y-axis (`line_multiaxis`),
   or spectra?
2. **Series** — Line style, colour, marker shape, legend
3. **Axes** — Labels, units, scale, range. Dual Y: record both axes
4. **Data points** — Explicit markers or continuous line?
5. **Special additions** — Error bars, shaded intervals, annotations?
6. **Ambiguities** — Overlapping or crossing lines, log scale?

### STEP 1 — Extract axis metadata
Both axes: label, unit, scale, range, ticks.
For `line_multiaxis`: y1 (left) and y2 (right) separately.
For `spectra`: X axis is wavelength (nm), 2θ (degrees), or
wavenumber (cm⁻¹).

### STEP 2 — Extract series one at a time
For EACH series, complete fully before moving to the next:
- Identify series name from legend
- Note line style, marker shape, colour, y-axis assignment
- If explicit markers visible: record every marked point
- If continuous line: sample at every inflection point + regular
  intervals, minimum 8 points per series
- For `spectra`: record every peak position and intensity,
  sample baseline at regular intervals
- After completing a series, sanity check: does the trend look
  visually consistent?
- Only move to the next series after current one is complete

### STEP 3 — Extract special additions
- `error_bars` — ± per point, shaded intervals: upper and lower
  bounds per point
- `annotations` — equations, R², peak labels
- `reference_line` — axis, value, label
Set anything not present to null.

### STEP 4 — Save JSON and display in chat

```json
{
  "chart_type": "<line|line_multiaxis|spectra>",
  "figure_metadata": {
    "title": "<string or null>",
    "caption": "<string or null>",
    "notes": "<string or null>",
    "resolution_flag": <true | false>
  },
  "axes": {
    "x": {"label": "<string>", "unit": "<string or null>",
          "scale": "<linear|log>", "range": [<min>, <max>],
          "ticks": [...]},
    "y1": {"label": "<string>", "unit": "<string or null>",
           "scale": "<linear|log>", "range": [<min>, <max>],
           "ticks": [...]},
    "y2": {"label": "<string or null>", "unit": "<string or null>",
           "scale": "<linear|log or null>",
           "range": [<min>, <max>], "ticks": [...]}
  },
  "data": {
    "series": [
      {
        "name": "<string>",
        "line_style": "<solid|dashed|dotted|dash-dot>",
        "marker": "<shape or null>",
        "color": "<string>",
        "y_axis": "<y1|y2>",
        "points": [{"x": <float>, "y": <float>,
                    "approximated": <true|false>}]
      }
    ]
  },
  "special_additions": {
    "error_bars": [{"series_name": "<string>",
                    "values": [{"x": <float>,
                                "error_plus": <float>,
                                "error_minus": <float>}]}],
    "annotations": ["<string>"],
    "reference_line": {"axis": "<x|y>", "value": <float>,
                       "label": "<string or null>"}
  },
  "confidence": <float 0.0-1.0>,
  "confidence_level": "<HIGH|MEDIUM|LOW>"
}
```

Rules: `y2` is null for `line` and `spectra`. All series specify
`y_axis: "y1"` for single axis charts.

---

## SECTION D — Contour (`contour_filled`, `contour_line`, `contour_overlaid`)

### Reasoning Protocol
1. **Subtype** — Filled (colour gradient), line (iso-lines only),
   overlaid (both)?
2. **Axes** — X and Y labels, units, ranges (two process variables)
3. **Z metric** — Response variable from colorbar label or contour
   line labels
4. **Contour levels** — Visible level values from colorbar ticks
   or line labels
5. **Optimal point** — Visible peak/maximum region?
6. **Ambiguities** — Hard to read colorbar? Missing contour labels?

### STEP 1 — Extract axis metadata
X and Y axes: label, unit, scale, range, ticks.
Z axis (colorbar or line labels): label, unit, all visible
contour level values.

### STEP 2 — Extract contour data
- `contour_filled` — sample Z at regular 5×5 grid of (x, y)
  points, read from colorbar
- `contour_line` — for each labeled iso-line, record value and
  3-5 (x, y) coordinate pairs along it
- `contour_overlaid` — apply both
- `optimal_point` — (x, y, z) of maximum Z — always required,
  null if cannot be determined

### STEP 3 — Save JSON and display in chat

```json
{
  "chart_type": "<contour_filled|contour_line|contour_overlaid>",
  "figure_metadata": {
    "title": "<string or null>",
    "caption": "<string or null>",
    "notes": "<string or null>",
    "resolution_flag": <true | false>
  },
  "axes": {
    "x": {"label": "<string>", "unit": "<string or null>",
          "scale": "<linear|log>", "range": [<min>, <max>],
          "ticks": [...]},
    "y": {"label": "<string>", "unit": "<string or null>",
          "scale": "<linear|log>", "range": [<min>, <max>],
          "ticks": [...]},
    "z": {"label": "<string>", "unit": "<string or null>",
          "contour_levels": [<float>]}
  },
  "data": {
    "sampled_points": [{"x": <float>, "y": <float>, "z": <float>}],
    "iso_lines": [{"level": <float>,
                   "coordinates": [{"x": <float>, "y": <float>}]}],
    "optimal_point": {"x": <float>, "y": <float>, "z": <float>}
  },
  "confidence": <float 0.0-1.0>,
  "confidence_level": "<HIGH|MEDIUM|LOW>"
}
```

Rules: `sampled_points` null for `contour_line`. `iso_lines` null
for `contour_filled`. Both populated for `contour_overlaid`.

---

## SECTION E — Other (`box_plot`, `pie`, `radar`)

### Reasoning Protocol
Identify subtype first, then reason accordingly.

**Box plot:** Groups/series count, axis labels/range, outliers
present, notches present.
**Pie:** Slice count, label style (direct or legend), percentages
printed, sums to 100%?
**Radar:** Spoke count, series count, axis labels/ranges, values
labeled at spokes?

### BOX PLOT — Extract one box at a time
STEP 1 — Category axis: label, unit, all category labels.
Value axis: label, unit, scale, range, ticks.
Map gridlines before reading any values.

STEP 2 — For EACH box, complete fully before moving to next:
- Group label and series name
- Five-number summary: minimum (lower whisker), Q1, median, Q3,
  maximum (upper whisker)
- Outliers list
- Sanity check after each box: Q1 < median < Q3?

### PIE — Extract one slice at a time
STEP 1 — For EACH slice, complete fully before moving to next:
- Label exactly as printed
- Percentage as printed, or estimated from visual angle
- Mark as `"source": "printed"` or `"source": "estimated"`
STEP 2 — Verify all slices sum to 100%, note discrepancy if not.

### RADAR — Extract one series at a time
STEP 1 — All spoke labels in order, range per spoke.
STEP 2 — For EACH series, complete fully before moving to next:
- Name from legend
- Value at each spoke in order

### Save JSON and display in chat

Box plot:
```json
{
  "chart_type": "box_plot",
  "figure_metadata": {
    "title": "<string or null>",
    "caption": "<string or null>",
    "notes": "<string or null>",
    "resolution_flag": <true | false>
  },
  "axes": {
    "category": {"label": "<string>", "unit": "<string or null>",
                 "categories": ["<string>"]},
    "value": {"label": "<string>", "unit": "<string or null>",
              "scale": "<linear|log>", "range": [<min>, <max>],
              "ticks": [...]}
  },
  "data": {
    "boxes": [{"group": "<string>", "series": "<string or null>",
               "stats": {"minimum": <float>, "q1": <float>,
                         "median": <float>, "q3": <float>,
                         "maximum": <float>,
                         "outliers": [<float>]}}]
  },
  "confidence": <float 0.0-1.0>,
  "confidence_level": "<HIGH|MEDIUM|LOW>"
}
```

Pie:
```json
{
  "chart_type": "pie",
  "figure_metadata": {
    "title": "<string or null>",
    "caption": "<string or null>",
    "notes": "<string or null>",
    "resolution_flag": <true | false>
  },
  "data": {
    "slices": [{"label": "<string>", "percentage": <float>,
                "source": "<printed|estimated>"}],
    "total": 100.0,
    "sum_check": <float>
  },
  "confidence": <float 0.0-1.0>,
  "confidence_level": "<HIGH|MEDIUM|LOW>"
}
```

Radar:
```json
{
  "chart_type": "radar",
  "figure_metadata": {
    "title": "<string or null>",
    "caption": "<string or null>",
    "notes": "<string or null>",
    "resolution_flag": <true | false>
  },
  "axes": {
    "spokes": [{"label": "<string>", "range": [<min>, <max>]}]
  },
  "data": {
    "series": [{"name": "<string>",
                "values": [{"spoke": "<string>",
                            "value": <float>}]}]
  },
  "confidence": <float 0.0-1.0>,
  "confidence_level": "<HIGH|MEDIUM|LOW>"
}
```

---

## SECTION F — Heatmap (`heatmap`)

### Reasoning Protocol
1. **Axes** — Row and column labels, categorical or numeric?
2. **Cell values** — Printed inside cells or read from colour scale?
3. **Colour scale** — Range and metric?
4. **Grid size** — Rows × columns count
5. **Ambiguities** — Cells hard to read due to colour overlap?

### STEP 1 — Extract axis metadata
Row axis: label, all row labels top to bottom.
Column axis: label, all column labels left to right.
Colour scale: label, unit, min and max.

### STEP 2 — Extract cell values row by row, cell by cell
For EACH row, complete fully before moving to next row:
- For EACH cell in the row, left to right:
  - If value printed inside — record exactly, mark as `"printed"`
  - If not printed — estimate from colour scale, mark as
    `"estimated"`
  - Round to 3 significant figures
- Sanity check after each row: do values follow a visually
  consistent pattern?

### STEP 3 — Save JSON and display in chat

```json
{
  "chart_type": "heatmap",
  "figure_metadata": {
    "title": "<string or null>",
    "caption": "<string or null>",
    "notes": "<string or null>",
    "resolution_flag": <true | false>
  },
  "axes": {
    "rows": {"label": "<string>", "labels": ["<string>"]},
    "columns": {"label": "<string>", "labels": ["<string>"]},
    "color_scale": {"label": "<string>",
                    "unit": "<string or null>",
                    "range": [<min>, <max>]}
  },
  "data": {
    "matrix": [{"row": "<string>",
                "values": [{"column": "<string>",
                            "value": <float>,
                            "source": "<printed|estimated>",
                            "approximated": <true|false>}]}]
  },
  "confidence": <float 0.0-1.0>,
  "confidence_level": "<HIGH|MEDIUM|LOW>"
}
```

---

## SECTION G — Multipanel (`multipanel`)

### Reasoning Protocol
1. **Panel count** — Confirm against classifier `panels` field
2. **Panel labels** — a, b, c... or 1, 2, 3... or (a), (b), (c)?
3. **Panel layout** — Grid arrangement (e.g. 2×2, 2×3, 1×4)
4. **Panel types** — Chart type per panel from classifier JSON
5. **Shared elements** — Any panels sharing axis, legend, or title?

### STEP 1 — Confirm panel count and layout
Read `panels` field from classifier JSON.
Count panels, note layout arrangement.
Note any shared axes, legends, or titles across panels.

### STEP 2 — Extract each panel independently
For each panel, in order (a, b, c...):
- Visually isolate the panel from the others
- Note its chart type from classifier `panels` field
- Apply the matching section from this file for that chart type
- Complete the panel fully — all steps in that section — before
  moving to the next panel
- Never extract two panels simultaneously
- Save each panel JSON immediately after completing it

### STEP 3 — Save one JSON per panel
Save: `results/detected_figs_tables/[pdf_name]/[filename]_panel_a_extracted.json`
Naming: `[filename]_panel_[label]_extracted.json`
Each panel JSON follows its chart type structure with an added
`"panel": "<label>"` field at the top.
Print each to chat as completed.

### STEP 4 — Save panel index JSON after all panels complete

```json
{
  "filename": "<filename>",
  "total_panels": <integer>,
  "layout": "<e.g. 2x3>",
  "panels": [
    {
      "panel": "a",
      "chart_type": "<label>",
      "output_file": "<filename>_panel_a_extracted.json",
      "confidence": <float 0.0-1.0>,
      "confidence_level": "<HIGH|MEDIUM|LOW>"
    }
  ]
}
```

---

## SECTION H — Unknown (`unknown`)

No extraction attempted. Save minimal JSON immediately and move on.

```json
{
  "chart_type": "unknown",
  "filename": "<filename>",
  "figure_metadata": {
    "title": "<string or null>",
    "caption": "<string or null>",
    "notes": "Extraction skipped — unsupported chart type",
    "resolution_flag": <true | false>
  },
  "data": null,
  "confidence": 0.0,
  "confidence_level": "LOW",
  "flag": "unknown chart type — recommend human review"
}
```

---

## Universal Critical Rules
- Always run ALL pre-extraction checks before any section —
  no exceptions, no shortcuts
- Never fabricate data — only record what is clearly visible
  in the image
- Never approximate without flagging — set `"approximated": true`
  on any estimated value
- Always extract one series, bar, row, panel, or slice at a time —
  never extract multiple simultaneously
- For log-scale axes, double-check all values — log compression
  is the most common extraction error
- If two series share similar colours or markers, note how you
  distinguished them in `figure_metadata.notes`
- Always save JSON before ending session — never skip the save step
- Never overwrite existing files — if file exists, append a counter
- Display full JSON in chat after saving

## Next Step
Pass extracted JSON and original image to /validate