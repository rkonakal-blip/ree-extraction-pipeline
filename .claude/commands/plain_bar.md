# Plain Bar Chart Synthetic Benchmark — Generation Prompt & Variation Table

## Purpose

This document specifies the generation of **10 synthetic plain bar chart images** and their paired **ground truth JSON metadata files** for use in a rare earth element (REE) extraction pipeline benchmark. Each plot must be realistic, publication-quality, and reflect actual figure styles found in REE hydrometallurgy literature.

---

## Output Requirements

For each of the 10 bar charts, produce **two files**:

1. **Image file**: `barplot{N}.png` (e.g., `barplot1.png`, `barplot2.png`, ..., `barplot10.png`)
   - Format: PNG
   - Resolution: 300 DPI
   - Size: 8 × 6 inches (2400 × 1800 px at 300 DPI)
   - Style: Clean, publication-quality, white background

2. **Ground truth metadata file**: `barplot{N}.md` (e.g., `barplot1.md`, `barplot2.md`, ..., `barplot10.md`)
   - Format: Markdown containing a structured JSON block
   - Must include all values used to generate the plot so that extraction accuracy can be evaluated

---

## Variation Table

Each row defines the configuration for one plot. Follow these specifications exactly.

| Plot # | # Bars | Orientation | Y-Axis Metric | X-Axis Categories | Error Bars | Y-Axis Range | Bar Color Style | Gridlines | Legend |
|--------|--------|-------------|---------------|-------------------|------------|--------------|-----------------|-----------|--------|
| 1 | 5 | Vertical | Extraction efficiency (%) | pH levels (1.5, 2.0, 2.5, 3.0, 3.5) | None | 0–100 | Single color (steel blue) | Horizontal only | No |
| 2 | 6 | Vertical | Extraction efficiency (%) | Reagent types (D2EHPA, Cyanex 272, PC88A, TBP, EHEHPA, Aliquat 336) | Yes (±2–5%) | 0–100 | Single color (coral red) | Horizontal only | No |
| 3 | 4 | Horizontal | Distribution ratio D | REE elements (La, Ce, Nd, Pr) | None | 0–10 | Varied colors per bar | None | Yes |
| 4 | 7 | Vertical | Extraction efficiency (%) | Contact time in min (5, 10, 15, 20, 30, 45, 60) | None | 40–100 | Single color (forest green) | Both axes | No |
| 5 | 5 | Vertical | Separation factor (α) | REE pairs (La/Ce, Ce/Pr, Pr/Nd, Nd/Sm, Sm/Eu) | None | 0–5 | Single color (slate gray) | Horizontal only | No |
| 6 | 6 | Vertical | Extraction efficiency (%) | Temperature °C (20, 30, 40, 50, 60, 70) | Yes (±1–4%) | 50–100 | Single color (teal) | Horizontal only | No |
| 7 | 8 | Vertical | Extraction efficiency (%) | Diluent type (kerosene, hexane, toluene, heptane, octanol, cyclohexane, xylene, dodecane) | None | 20–90 | Varied colors per bar | Horizontal only | Yes |
| 8 | 5 | Horizontal | Stripping efficiency (%) | Stripping agent (HCl 1M, HCl 2M, H2SO4 1M, HNO3 1M, EDTA 0.5M) | Yes (±2–6%) | 0–100 | Single color (dark orange) | Vertical only | No |
| 9 | 4 | Vertical | Distribution ratio D | Aqueous-to-organic ratio A:O (1:3, 1:1, 2:1, 3:1) | None | 0–20 | Single color (medium purple) | Horizontal only | No |
| 10 | 6 | Vertical | Extraction efficiency (%) | Initial metal concentration mg/L (50, 100, 200, 300, 500, 1000) | Yes (±1–5%) | 60–100 | Varied colors per bar | Horizontal only | Yes |

---

## Detailed Generation Instructions

### Step 1 — Environment Setup

Use Python with `matplotlib` and `numpy`. Do not use any external plot libraries beyond these two.

```bash
pip install matplotlib numpy
```

### Step 2 — Plot Styling Requirements

Apply the following to **all 10 plots** consistently:

- **Font**: DejaVu Sans (matplotlib default) or Arial if available
- **Title font size**: 13pt, bold
- **Axis label font size**: 11pt
- **Tick label font size**: 9pt
- **Bar width**: 0.55 for vertical; 0.5 for horizontal
- **Figure DPI**: 300
- **Figure size**: (8, 6) inches
- **Background**: White (`#FFFFFF`)
- **Spine visibility**: Keep bottom and left spines; remove top and right spines
- **Error bar style**: Black caps, cap size 4, line width 1.2
- **Bar edge**: Black edge, line width 0.6
- **Legend**: Place inside plot, upper right, frame with light gray border

### Step 3 — Data Generation Rules

- All bar values must be **realistic** for REE extraction literature:
  - Extraction efficiency (%): values between 20–98%, non-monotonic patterns allowed
  - Distribution ratio D: values between 0.5–18, realistic variation
  - Separation factor α: values between 0.8–4.5
  - Stripping efficiency (%): values between 30–97%
- **Do not use perfectly round numbers** — add slight variation (e.g., 72.3 not 72.0)
- Error bar values (if specified) must be positive floats representing ± standard deviation
- Generate all values programmatically using `numpy` with a fixed random seed per plot for reproducibility

Use this seed assignment:
| Plot # | numpy seed |
|--------|------------|
| 1 | 101 |
| 2 | 102 |
| 3 | 103 |
| 4 | 104 |
| 5 | 105 |
| 6 | 106 |
| 7 | 107 |
| 8 | 108 |
| 9 | 109 |
| 10 | 110 |

### Step 4 — Axis and Title Formatting

Follow these title and axis label conventions from REE literature:

| Plot # | Chart Title | X-Axis Label | Y-Axis Label |
|--------|-------------|--------------|--------------|
| 1 | Effect of pH on Extraction Efficiency of Nd | pH | Extraction Efficiency (%) |
| 2 | Extraction Efficiency of La with Different Extractants | Extractant | Extraction Efficiency (%) |
| 3 | Distribution Ratio of REEs in D2EHPA System | REE Element | Distribution Ratio (D) |
| 4 | Effect of Contact Time on Ce Extraction | Contact Time (min) | Extraction Efficiency (%) |
| 5 | Separation Factor Between Adjacent REE Pairs | REE Pair | Separation Factor (α) |
| 6 | Effect of Temperature on Pr Extraction | Temperature (°C) | Extraction Efficiency (%) |
| 7 | Effect of Diluent on Nd Extraction Efficiency | Diluent | Extraction Efficiency (%) |
| 8 | Stripping Efficiency with Different Stripping Agents | Stripping Agent | Stripping Efficiency (%) |
| 9 | Effect of A:O Ratio on Distribution of Sm | A:O Ratio | Distribution Ratio (D) |
| 10 | Effect of Initial Metal Concentration on La Extraction | Initial Concentration (mg/L) | Extraction Efficiency (%) |

### Step 5 — Ground Truth Metadata File Format

For each plot, create `barplot{N}.md` with the following structure exactly:

~~~markdown
# Ground Truth: barplot{N}

## Plot Configuration

- **Plot type**: Plain bar chart
- **Orientation**: [Vertical / Horizontal]
- **Number of bars**: [N]
- **Y-axis metric**: [metric name]
- **Error bars present**: [Yes / No]
- **numpy seed**: [seed]

## Data

```json
{
  "title": "[chart title]",
  "x_label": "[x-axis label]",
  "y_label": "[y-axis label]",
  "y_axis_range": [min, max],
  "bars": [
    {"label": "[category label]", "value": [exact float], "error": [float or null]},
    ...
  ]
}
```

## Notes

[Any special formatting notes — e.g., rotated x-tick labels, legend position, color scheme used]
~~~

**Critical**: The `value` fields in the JSON must be the **exact floating point numbers used to generate the bars** — not rounded approximations. This is the ground truth against which extraction accuracy will be measured.

### Step 6 — X-Tick Label Handling

- For plots with long category labels (reagent names, diluent names, stripping agents): rotate x-tick labels **45 degrees**, right-aligned
- For plots with short labels (pH values, temperatures, A:O ratios): keep labels horizontal
- For horizontal bar charts: y-tick labels are the category labels — keep them horizontal and left-aligned

### Step 7 — File Output

Save all files to the current working directory. Run a final check that:
- All 10 PNG files exist and are non-empty
- All 10 MD files exist and contain valid JSON in the code block
- Image dimensions are correct (2400 × 1800 px)

Print a confirmation summary at the end listing all 20 files generated.

---

## Color Reference

| Color name used in table | Matplotlib color string |
|--------------------------|------------------------|
| Steel blue | `#4472C4` |
| Coral red | `#C0504D` |
| Forest green | `#4F7942` |
| Slate gray | `#7F7F7F` |
| Teal | `#008080` |
| Dark orange | `#E26B0A` |
| Medium purple | `#7B4F9E` |
| Varied colors per bar | Use matplotlib tab10 colormap, one color per bar |

---

## Validation Checklist

Before finalizing, verify each plot against this checklist:

- [ ] Title matches the specification table exactly
- [ ] X and Y axis labels match exactly
- [ ] Number of bars matches specification
- [ ] Orientation (vertical/horizontal) is correct
- [ ] Error bars present only where specified
- [ ] Y-axis range matches specification
- [ ] Color style matches specification
- [ ] Gridlines match specification
- [ ] Legend present only where specified
- [ ] DPI is 300
- [ ] Ground truth JSON contains exact values used in plotting
- [ ] numpy seed matches the seed table

---

*This document is part of the REE Extraction Pipeline Benchmark Suite — Plain Bar Charts (Suite 1 of 3).*
