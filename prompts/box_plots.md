# Box Plot Synthetic Benchmark — Generation Spec

## Purpose

Generate **10 synthetic box plots** and paired **ground truth JSON metadata files** for the REE extraction pipeline benchmark. Each plot tests whether the extraction pipeline can correctly identify the five-number summary (minimum, Q1, median, Q3, maximum) and outliers for each box, across multiple groups and series.

---

## Output Requirements

For each of the 10 plots, produce **two files**:

1. **Image**: `boxplot{N}.png`
   - Format: PNG, 300 DPI, 8 × 6 inches (2400 × 1800 px)
   - Style: Clean, publication-quality, white background

2. **Ground truth**: `boxplot{N}.md`
   - Markdown file containing a structured JSON block with exact values used to generate the plot

### Save location — CRITICAL

Save ALL 20 files to this exact path:
```
C:\Users\Rithika\Desktop\ree-extraction-pipeline\benchmark\box_plots\
```

Create the `box_plots\` folder if it does not exist. Do not save anywhere else. After generation, print the full path of every file saved as confirmation.

---

## Variation Table

| Plot # | # Groups (X) | # Series per group | Orientation | Y-Axis Metric | X-Axis Categories | Outliers | Notched | Color scheme | Gridlines | Legend |
|--------|-------------|-------------------|-------------|---------------|-------------------|----------|---------|--------------|-----------|--------|
| 1 | 4 | 1 | Vertical | Extraction efficiency (%) | pH (1.5, 2.0, 2.5, 3.0) | Yes | No | Single (steel blue) | Horizontal only | No |
| 2 | 5 | 1 | Vertical | Extraction efficiency (%) | Temperature °C (20, 30, 40, 50, 60) | Yes | No | Single (coral red) | Horizontal only | No |
| 3 | 3 | 2 | Vertical | Distribution ratio D | REE elements (La, Ce, Nd) | No | No | tab10, 2 colors | Horizontal only | Yes |
| 4 | 4 | 1 | Horizontal | Stripping efficiency (%) | Stripping agents (HCl 1M, HCl 2M, H2SO4, HNO3) | Yes | No | Single (forest green) | Vertical only | No |
| 5 | 5 | 1 | Vertical | Extraction efficiency (%) | Contact time min (10, 20, 30, 45, 60) | No | Yes | Single (medium purple) | Horizontal only | No |
| 6 | 4 | 2 | Vertical | Recovery (%) | Extractant (D2EHPA, Cyanex 272, PC88A, TBP) | Yes | No | Set1, 2 colors | Horizontal only | Yes |
| 7 | 3 | 1 | Vertical | Separation factor (α) | REE pairs (La/Ce, Ce/Pr, Pr/Nd) | Yes | No | Single (teal) | Horizontal only | No |
| 8 | 4 | 3 | Vertical | Extraction efficiency (%) | A:O ratio (1:3, 1:1, 2:1, 3:1) | No | No | tab10, 3 colors | Horizontal only | Yes |
| 9 | 5 | 1 | Horizontal | Distribution ratio D | Initial conc. mg/L (50, 100, 200, 500, 1000) | Yes | No | Single (dark orange) | Vertical only | No |
| 10 | 3 | 2 | Vertical | Extraction efficiency (%) | Diluent (Kerosene, Hexane, Toluene) | Yes | Yes | Paired, 2 colors | Horizontal only | Yes |

---

## Series Labels (for multi-series plots only)

| Plot # | Series names |
|--------|-------------|
| 3 | D2EHPA, PC88A |
| 6 | La, Nd |
| 8 | D2EHPA, Cyanex 272, PC88A |
| 10 | La, Nd |

---

## Detailed Generation Instructions

### Step 1 — Environment setup
```bash
pip install matplotlib numpy
```

### Step 2 — Universal styling (apply to ALL plots)
- Font: DejaVu Sans
- Title font size: 13pt bold
- Axis label font size: 11pt
- Tick label font size: 9pt
- Figure DPI: 300
- Figure size: (8, 6) inches
- Background: white `#FFFFFF`
- Remove top and right spines
- Box width: 0.5 for single series; 0.3 for multi-series
- Median line: black, line width 2.0
- Whisker line width: 1.2
- Outlier markers: `o`, marker size 5, same color as box, filled
- Notch style (where specified): standard matplotlib notched box
- Legend: inside plot, upper right, light gray frame (only for multi-series plots)
- X-tick labels: rotate 45° right-aligned when labels are long; keep horizontal for short labels

### Step 3 — Data generation rules

For each box generate a realistic sample dataset:
- Generate **30–50 raw data points** per box using `numpy.random.normal(mean, std)`
- Choose realistic means and stds for REE extraction literature:
  - Extraction efficiency (%): mean between 40–90%, std between 3–10%
  - Distribution ratio D: mean between 1–15, std between 0.2–2.0
  - Stripping efficiency (%): mean between 50–95%, std between 3–8%
  - Separation factor α: mean between 0.8–4.0, std between 0.1–0.5
  - Recovery (%): mean between 50–95%, std between 3–10%
- **Do not use perfectly round numbers** for means or stds
- For plots **with outliers**: after generating the sample, manually append 1–3 outlier values that fall outside 1.5×IQR
- For plots **without outliers**: clip all values to within 1.5×IQR so no fliers appear
- Use `numpy` with fixed seeds (see table below)
- matplotlib's `boxplot()` will compute the five-number summary automatically from the raw data — store both the raw data points AND the computed statistics in the ground truth

**numpy seeds:**

| Plot # | numpy seed |
|--------|------------|
| 1 | 501 |
| 2 | 502 |
| 3 | 503 |
| 4 | 504 |
| 5 | 505 |
| 6 | 506 |
| 7 | 507 |
| 8 | 508 |
| 9 | 509 |
| 10 | 510 |

### Step 4 — Axis and title formatting

| Plot # | Chart Title | X-Axis Label | Y-Axis Label |
|--------|-------------|--------------|--------------|
| 1 | Distribution of Nd Extraction Efficiency Across pH Levels | pH | Extraction Efficiency (%) |
| 2 | Effect of Temperature on La Extraction Efficiency | Temperature (°C) | Extraction Efficiency (%) |
| 3 | Distribution Ratio Variability of REEs by Extractant | REE Element | Distribution Ratio (D) |
| 4 | Stripping Efficiency Distribution by Stripping Agent | Stripping Agent | Stripping Efficiency (%) |
| 5 | Extraction Efficiency Distribution vs Contact Time | Contact Time (min) | Extraction Efficiency (%) |
| 6 | REE Recovery Distribution Across Extractants | Extractant | Recovery (%) |
| 7 | Separation Factor Variability for Adjacent REE Pairs | REE Pair | Separation Factor (α) |
| 8 | Extraction Efficiency Distribution at Different A:O Ratios | A:O Ratio | Extraction Efficiency (%) |
| 9 | Distribution Ratio vs Initial Metal Concentration | Initial Concentration (mg/L) | Distribution Ratio (D) |
| 10 | Extraction Efficiency Distribution by Diluent Type | Diluent | Extraction Efficiency (%) |

### Step 5 — Ground truth metadata format

For each plot create `boxplot{N}.md` with this structure:

~~~markdown
# Ground Truth: boxplot{N}

## Plot Configuration

- **Plot type**: Box plot
- **Orientation**: [Vertical / Horizontal]
- **Number of groups**: [N]
- **Number of series per group**: [N]
- **Outliers shown**: [Yes / No]
- **Notched**: [Yes / No]
- **numpy seed**: [seed]

## Data

```json
{
  "title": "[chart title]",
  "x_label": "[x-axis label]",
  "y_label": "[y-axis label]",
  "boxes": [
    {
      "group_label": "[x category]",
      "series_label": "[series name or null if single series]",
      "stats": {
        "minimum": [exact float],
        "q1": [exact float],
        "median": [exact float],
        "q3": [exact float],
        "maximum": [exact float],
        "outliers": [list of exact floats, or empty list]
      },
      "raw_data": [list of all exact floats used to generate this box]
    }
  ]
}
```

## Notes

[Any special formatting notes — e.g. notch style, outlier positions, legend placement, color per series]
~~~

**Critical:**
- `stats` must contain the exact five-number summary as computed by matplotlib from the raw data — not approximations
- `minimum` and `maximum` refer to the **whisker ends** (1.5×IQR), not the absolute min/max of raw data
- `outliers` must list every flier point plotted — empty list if none
- `raw_data` must contain every data point passed to matplotlib's boxplot function
- For multi-series plots, each box gets its own entry identified by both `group_label` and `series_label`

### Step 6 — File output and validation

After generating all files:
1. Verify all 20 files exist in `C:\Users\Rithika\Desktop\ree-extraction-pipeline\benchmark\box_plots\`
2. Verify each PNG is 2400 × 1800 px
3. Verify each MD file contains valid JSON
4. Print a confirmation list of all 20 file paths

---

## Validation Checklist

Before finishing, verify each plot:

- [ ] Title matches specification exactly
- [ ] X and Y axis labels match exactly
- [ ] Correct number of groups and series
- [ ] Outliers present only where specified
- [ ] Notched style applied only where specified
- [ ] Orientation correct (vertical/horizontal)
- [ ] Correct color scheme applied
- [ ] Gridlines match specification
- [ ] Legend present only for multi-series plots
- [ ] DPI is 300
- [ ] Ground truth JSON contains five-number summary, outlier list, AND raw data
- [ ] `minimum` and `maximum` are whisker ends, not absolute data extremes
- [ ] numpy seed matches seed table
- [ ] Files saved to C:\Users\Rithika\Desktop\ree-extraction-pipeline\benchmark\box_plots\

---

*This document is part of the REE Extraction Pipeline Benchmark Suite — Box Plots (Suite 5 of 5).*
