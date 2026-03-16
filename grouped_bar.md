# Grouped Bar Chart Synthetic Benchmark — Generation Spec

## Purpose

Generate **10 synthetic grouped bar chart images** and paired **ground truth JSON metadata files** for the REE extraction pipeline benchmark.

---

## Output Requirements

For each of the 10 plots, produce **two files**:

1. **Image**: `grouped_barplot{N}.png`
   - Format: PNG, 300 DPI, 8 × 6 inches (2400 × 1800 px)
   - Style: Clean, publication-quality, white background

2. **Ground truth**: `grouped_barplot{N}.md`
   - Markdown file containing a structured JSON block with exact values used to generate the plot

### Save location — CRITICAL

Save ALL 20 files to this exact path:
```
C:\Users\%USERNAME%\Desktop\ree-extraction-pipeline\benchmark\bar_charts\grouped\
```

If `%USERNAME%` does not resolve, use the actual Windows username of the current session. Do not save anywhere else. After generation, print the full path of every file saved as confirmation.

---

## Variation Table

| Plot # | # Groups (X) | # Series per group | Orientation | Y-Axis Metric | X-Axis Categories | Error Bars | Y-Axis Range | Color scheme | Gridlines | Legend |
|--------|-------------|-------------------|-------------|---------------|-------------------|------------|--------------|--------------|-----------|--------|
| 1 | 4 | 3 | Vertical | Extraction efficiency (%) | pH (1.5, 2.0, 2.5, 3.0) | No | 0–100 | tab10, 3 colors | Horizontal only | Yes |
| 2 | 5 | 2 | Vertical | Extraction efficiency (%) | Temperature °C (20, 30, 40, 50, 60) | Yes (±2–5%) | 0–100 | Set1, 2 colors | Horizontal only | Yes |
| 3 | 3 | 4 | Vertical | Distribution ratio D | REE elements (La, Ce, Nd) | No | 0–15 | tab10, 4 colors | Horizontal only | Yes |
| 4 | 4 | 3 | Horizontal | Stripping efficiency (%) | Stripping agents (HCl 1M, HCl 2M, H2SO4, HNO3) | No | 0–100 | Set2, 3 colors | Vertical only | Yes |
| 5 | 5 | 2 | Vertical | Extraction efficiency (%) | Contact time min (10, 20, 30, 45, 60) | Yes (±1–4%) | 40–100 | Paired, 2 colors | Horizontal only | Yes |
| 6 | 4 | 4 | Vertical | Separation factor (α) | REE pairs (La/Ce, Ce/Pr, Pr/Nd, Nd/Sm) | No | 0–5 | tab10, 4 colors | Horizontal only | Yes |
| 7 | 6 | 3 | Vertical | Extraction efficiency (%) | Initial conc. mg/L (50, 100, 200, 300, 500, 1000) | Yes (±2–6%) | 0–100 | Set1, 3 colors | Horizontal only | Yes |
| 8 | 3 | 5 | Vertical | Recovery (%) | Diluent type (Kerosene, Hexane, Toluene) | No | 50–100 | tab20, 5 colors | Horizontal only | Yes |
| 9 | 5 | 2 | Horizontal | Distribution ratio D | A:O ratio (1:3, 1:2, 1:1, 2:1, 3:1) | No | 0–20 | Set2, 2 colors | Vertical only | Yes |
| 10 | 4 | 3 | Vertical | Extraction efficiency (%) | Reagent conc. M (0.1, 0.5, 1.0, 2.0) | Yes (±1–5%) | 0–100 | tab10, 3 colors | Horizontal only | Yes |

---

## Series Labels

Each group has named series (the legend entries). Use these for all plots:

| Plot # | Series names |
|--------|-------------|
| 1 | D2EHPA, Cyanex 272, PC88A |
| 2 | La, Nd |
| 3 | 0.1M extractant, 0.5M extractant, 1.0M extractant, 2.0M extractant |
| 4 | La, Ce, Nd |
| 5 | D2EHPA, PC88A |
| 6 | 0.1M D2EHPA, 0.5M D2EHPA, 1.0M D2EHPA, 2.0M D2EHPA |
| 7 | D2EHPA, Cyanex 272, PC88A |
| 8 | La, Ce, Nd, Pr, Sm |
| 9 | La, Nd |
| 10 | D2EHPA, Cyanex 272, PC88A |

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
- Bar width per series: 0.8 / number_of_series (so groups don't overlap)
- Bar edge: black, line width 0.6
- Error bar style: black caps, cap size 4, line width 1.2
- Legend: inside plot, upper right, light gray frame
- X-tick labels: rotate 45° right-aligned when labels are long; keep horizontal for short labels (pH, temperature, ratios)
- Group bars must be centered on their x-tick position — offset each series symmetrically around the center

### Step 3 — Data generation rules
- Values must be **realistic** for REE extraction literature — no perfectly round numbers
- Each series within a group represents a different extractant or REE — values should vary meaningfully between series
- Use `numpy` with fixed seeds (see table below)
- Error bar values (where specified) must be positive floats representing ± standard deviation

| Plot # | numpy seed |
|--------|------------|
| 1 | 301 |
| 2 | 302 |
| 3 | 303 |
| 4 | 304 |
| 5 | 305 |
| 6 | 306 |
| 7 | 307 |
| 8 | 308 |
| 9 | 309 |
| 10 | 310 |

### Step 4 — Axis and title formatting

| Plot # | Chart Title | X-Axis Label | Y-Axis Label |
|--------|-------------|--------------|--------------|
| 1 | Extraction Efficiency of REEs with Different Extractants vs pH | pH | Extraction Efficiency (%) |
| 2 | Effect of Temperature on La and Nd Extraction | Temperature (°C) | Extraction Efficiency (%) |
| 3 | Distribution Ratio of REEs at Different Extractant Concentrations | REE Element | Distribution Ratio (D) |
| 4 | Stripping Efficiency of REEs with Different Stripping Agents | Stripping Agent | Stripping Efficiency (%) |
| 5 | Extraction Kinetics of D2EHPA vs PC88A | Contact Time (min) | Extraction Efficiency (%) |
| 6 | Separation Factor for Adjacent REE Pairs at Different Extractant Concentrations | REE Pair | Separation Factor (α) |
| 7 | Effect of Initial Concentration on REE Extraction | Initial Concentration (mg/L) | Extraction Efficiency (%) |
| 8 | Recovery of REEs with Different Diluents | Diluent | Recovery (%) |
| 9 | Distribution Ratio of La and Nd at Different A:O Ratios | A:O Ratio | Distribution Ratio (D) |
| 10 | Extraction Efficiency at Different Reagent Concentrations | Reagent Concentration (M) | Extraction Efficiency (%) |

### Step 5 — Ground truth metadata format

For each plot create `grouped_barplot{N}.md` with this structure:

~~~markdown
# Ground Truth: grouped_barplot{N}

## Plot Configuration

- **Plot type**: Grouped bar chart
- **Orientation**: [Vertical / Horizontal]
- **Number of groups**: [N]
- **Number of series**: [N]
- **Y-axis metric**: [metric]
- **Error bars present**: [Yes / No]
- **numpy seed**: [seed]

## Data

```json
{
  "title": "[chart title]",
  "x_label": "[x-axis label]",
  "y_label": "[y-axis label]",
  "y_axis_range": [min, max],
  "series": ["series1", "series2", "series3"],
  "groups": [
    {
      "label": "[x category]",
      "bars": [
        {"series": "series1", "value": [exact float], "error": [float or null]},
        {"series": "series2", "value": [exact float], "error": [float or null]},
        {"series": "series3", "value": [exact float], "error": [float or null]}
      ]
    }
  ]
}
```

## Notes

[Any special formatting notes — e.g. rotated x-tick labels, bar width used, group spacing]
~~~

**Critical**: `value` must be the exact float used to draw that bar. Every bar must be uniquely identifiable by its `group label + series name` combination — this is how extraction accuracy will be evaluated.

### Step 6 — File output and validation

After generating all files:
1. Verify all 20 files exist in `C:\Users\%USERNAME%\Desktop\ree-extraction-pipeline\benchmark\bar_charts\grouped\`
2. Verify each PNG is 2400 × 1800 px
3. Verify each MD file contains valid JSON
4. Print a confirmation list of all 20 file paths

---

## Validation Checklist

Before finishing, verify each plot:

- [ ] Title matches specification exactly
- [ ] X and Y axis labels match exactly
- [ ] Correct number of groups and series
- [ ] Bars within each group are correctly centered on x-tick
- [ ] No bars from adjacent groups overlap
- [ ] Error bars present only where specified
- [ ] Orientation correct (vertical/horizontal)
- [ ] Correct color scheme applied
- [ ] Gridlines match specification
- [ ] Legend present and correctly labeled
- [ ] DPI is 300
- [ ] Ground truth JSON identifies each bar by group + series
- [ ] numpy seed matches seed table
- [ ] Files saved to correct Desktop path

---

*This document is part of the REE Extraction Pipeline Benchmark Suite — Grouped Bar Charts (Suite 2 of 3).*
