# Figure and Plot Classification

## Purpose
Second stage of the REE extraction pipeline for figures and plots.
Given a cropped figure image from the Detect stage, classify it into 
one of the supported chart types and return a structured JSON output.
Do not extract any data — classification only.

## Input
- Single cropped figure PNG from results/detected_figs_tables/[pdf_name]/figures/
- Usage: /classify [path/to/figure.png]

## Supported Labels

| Category | Labels |
|---|---|
| Bar | `bar_plain`, `bar_grouped`, `bar_stacked` |
| Scatter | `scatter`, `scatter_line` |
| Line | `line`, `line_multiaxis`, `spectra` |
| Contour | `contour_filled`, `contour_line`, `contour_overlaid` |
| Other | `box_plot`, `pie`, `table`, `heatmap`, `radar` |
| Special | `multipanel`, `unknown` |

## Reasoning Protocol

Before outputting JSON, reason through these visual features in order:

1. **Panels** — Are there multiple labeled sub-figures (a, b, c...)? 
   If yes, classify each panel independently.
2. **Chart structure** — What is the dominant visual structure? 
   Bars, points, lines, filled regions, grid cells?
3. **Axes** — How many axes? Are there dual Y axes? What do the 
   axis labels suggest?
4. **Overlays** — Are there multiple chart types overlaid on the 
   same axes? (e.g. scatter points with a fitted line)
5. **Legend** — What does the legend reveal about series types?
6. **Domain cues** — Do axis labels suggest spectra (wavelength, 
   2θ, intensity), contour (two process variables + colorbar), 
   or standard REE extraction data (pH, D values, recovery %)?

Only after reasoning through all six points, output the JSON.

## Output Format

Reason first, then return this exact JSON structure and nothing else 
after it — no explanation, no preamble:

**Field rules:**
- `chart_type` — must be one of the supported labels, nothing else
- `confidence` — float between 0.0 and 1.0
- `confidence_level` — HIGH if confidence >= 0.85, MEDIUM if 
  0.60–0.84, LOW if below 0.60
- `is_multipanel` true → `panels` must list each panel's label, 
  `chart_type` must be `multipanel`
- `is_mixed` true → `primary` is dominant type, `secondary` is 
  overlaid type, `chart_type` reflects combination (e.g. `scatter_line`)
- `is_multipanel` false → `panels` is null
- `is_mixed` false → `secondary` is null
- `primary` always reflects main chart type even for single 
  non-mixed figures
- `special_additions` is always a list — empty `[]` if none apply

**Special additions options:**
- `error_bars` — uncertainty markers on data points or bars
- `trendline` — fitted curve overlaid on data, not raw data series
- `annotations` — text labels directly on data points or regions
- `reference_line` — horizontal or vertical threshold/reference line

```json
{
  "filename": "<input image filename>",
  "chart_type": "<label from supported list>",
  "confidence": <float 0.0–1.0>,
  "confidence_level": "<HIGH | MEDIUM | LOW>",
  "is_multipanel": <true | false>,
  "panels": <{"a": "<label>", "b": "<label>", ...} | null>,
  "is_mixed": <true | false>,
  "primary": "<label>",
  "secondary": <"<label>" | null>,
  "special_additions": ["<addition>", ...]
}
```

## Output Save
Save to: `results/detected_figs_tables/[pdf_name]/[filename]_classified.json`
Print the JSON to chat after saving.

## Few-Shot Examples

### Example 1 — Multi-panel figure (complex grid)

**What you see:** Six sub-figures arranged in a 2×3 grid, labeled 
(a) through (f). Panels (a), (b), (c) show filled color gradient 
plots with colorbars. Panels (d), (e) show scatter points with 
fitted curves. Panel (f) shows grouped rectangular bars with error 
markers on top of each bar.

**Reasoning:**
1. Six labeled panels detected in a 2×3 grid — panels do not need 
   to be side by side, any grid arrangement counts
2. Panels (a)(b)(c): smooth color gradients + colorbars + two 
   continuous axes → contour_filled
3. Panels (d)(e): discrete points + fitted curves on same axes → 
   scatter_line (mixed)
4. Panel (f): rectangular bars grouped per category + uncertainty 
   markers → bar_grouped, error_bars present
5. No dual axes in any panel
6. Each panel classified independently regardless of layout

**Output:**
```json
{
  "filename": "syn_001_page2_figure1.png",
  "chart_type": "multipanel",
  "confidence": 0.95,
  "confidence_level": "HIGH",
  "is_multipanel": true,
  "panels": {
    "a": "contour_filled",
    "b": "contour_filled",
    "c": "contour_filled",
    "d": "scatter_line",
    "e": "scatter_line",
    "f": "bar_grouped"
  },
  "is_mixed": false,
  "primary": "multipanel",
  "secondary": null,
  "special_additions": ["error_bars"]
}
```

### Example 2 — Mixed scatter + line

**What you see:** A single plot with discrete data points (different 
marker shapes per series) AND smooth curves passing through or near 
each series of points.

**Reasoning:**
1. Single panel — no labeled sub-figures
2. Both discrete points and continuous curves present on same axes
3. Single X and Y axis
4. Curves appear fitted to the point series — not independent data
5. Legend shows both marker and line entries for same series
6. Axis labels suggest extraction efficiency vs pH — standard REE 
   scatter data

**Output:**
```json
{
  "filename": "syn_001_page3_figure2.png",
  "chart_type": "scatter_line",
  "confidence": 0.91,
  "confidence_level": "HIGH",
  "is_multipanel": false,
  "panels": null,
  "is_mixed": true,
  "primary": "scatter",
  "secondary": "line",
  "special_additions": ["trendline"]
}
```

### Example 3 — Contour vs Heatmap

**What you see:** A grid of colored cells, each cell a uniform solid 
color, no contour lines, axes are categorical labels not continuous 
numeric values.

**Reasoning:**
1. Single panel
2. Grid of uniform colored cells — no smooth gradients, no iso-lines
3. Both axes are categorical (e.g. extractant names vs pH levels)
4. No colorbar with contour levels — just a discrete color scale
5. No legend suggesting series
6. Structure matches a correlation matrix or parameter comparison grid

**Output:**
```json
{
  "filename": "syn_001_page5_figure3.png",
  "chart_type": "heatmap",
  "confidence": 0.93,
  "confidence_level": "HIGH",
  "is_multipanel": false,
  "panels": null,
  "is_mixed": false,
  "primary": "heatmap",
  "secondary": null,
  "special_additions": []
}
```

## Rules
- Never force a classification — use `unknown` if genuinely ambiguous
- Never extract data — classification only
- Always complete the full reasoning protocol before outputting JSON
- Confidence guidance:
  - HIGH (>= 0.85) — unambiguous, clear visual structure
  - MEDIUM (0.60–0.84) — mostly clear but some ambiguity
  - LOW (< 0.60) — significant uncertainty, multiple plausible labels
- If confidence is LOW, add a `"flag": "low confidence — recommend 
  human review"` field to the output JSON
- Save output before ending — never skip the save step

## Next Step
Pass classified JSON and original image to:
- /extract if chart_type is any figure or plot type
- /table if chart_type is `table`
- Flag for human review if chart_type is `unknown` or 
  confidence_level is LOW