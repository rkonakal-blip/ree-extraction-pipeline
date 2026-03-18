# Scatter Plot with Multiple Trend Lines — Generation Spec

## Purpose

Generate **10 synthetic scatter plots with multiple trend lines** and paired **ground truth JSON metadata files** for the REE extraction pipeline benchmark. Each plot contains multiple data series, each with its own scatter points and fitted trend line — testing whether the extraction pipeline can correctly associate points and trend lines with their respective series.

---

## Output Requirements

For each of the 10 plots, produce **two files**:

1. **Image**: `scatter_trend{N}.png`
   - Format: PNG, 300 DPI, 8 × 6 inches (2400 × 1800 px)
   - Style: Clean, publication-quality, white background

2. **Ground truth**: `scatter_trend{N}.md`
   - Markdown file containing a structured JSON block with exact values used to generate the plot

### Save location — CRITICAL

Save ALL 20 files to this exact path:
```
C:\Users\%USERNAME%\Desktop\ree-extraction-pipeline\benchmark\scatter_plots\with_trendlines\
```

Create the `with_trendlines\` subfolder if it does not exist. If `%USERNAME%` does not resolve, use the actual Windows username of the current session. Do not save anywhere else. After generation, print the full path of every file saved as confirmation.

---

## Variation Table

Plots 1–5 use **linear** trend lines. Plots 6–10 use **polynomial (degree 2)** trend lines.

| Plot # | # Series | Trend type | Y-Axis Metric | X-Axis Variable | Points per series | Y-Axis Range | Color scheme | Show R² on plot | Legend |
|--------|----------|------------|---------------|-----------------|-------------------|--------------|--------------|-----------------|--------|
| 1 | 3 | Linear | Extraction efficiency (%) | pH | 8 | 0–100 | tab10, 3 colors | Yes | Yes |
| 2 | 2 | Linear | Distribution ratio D | Extractant conc. (M) | 10 | 0–15 | Set1, 2 colors | Yes | Yes |
| 3 | 4 | Linear | Extraction efficiency (%) | Temperature (°C) | 7 | 30–100 | tab10, 4 colors | No | Yes |
| 4 | 2 | Linear | Stripping efficiency (%) | HCl concentration (M) | 9 | 20–100 | Paired, 2 colors | Yes | Yes |
| 5 | 3 | Linear | Recovery (%) | Contact time (min) | 8 | 40–100 | Set2, 3 colors | No | Yes |
| 6 | 2 | Polynomial | Extraction efficiency (%) | pH | 10 | 0–100 | tab10, 2 colors | Yes | Yes |
| 7 | 3 | Polynomial | Distribution ratio D | Temperature (°C) | 8 | 0–20 | Set1, 3 colors | No | Yes |
| 8 | 2 | Polynomial | Extraction efficiency (%) | Extractant conc. (M) | 9 | 10–100 | Paired, 2 colors | Yes | Yes |
| 9 | 4 | Polynomial | Recovery (%) | Contact time (min) | 7 | 20–100 | tab10, 4 colors | No | Yes |
| 10 | 3 | Polynomial | Separation factor (α) | pH | 8 | 0–5 | Set2, 3 colors | Yes | Yes |

---

## Series Labels

| Plot # | Series names |
|--------|-------------|
| 1 | D2EHPA, Cyanex 272, PC88A |
| 2 | La, Nd |
| 3 | La, Ce, Nd, Pr |
| 4 | D2EHPA, PC88A |
| 5 | D2EHPA, Cyanex 272, PC88A |
| 6 | La, Nd |
| 7 | D2EHPA, Cyanex 272, PC88A |
| 8 | La, Ce |
| 9 | La, Ce, Nd, Pr |
| 10 | D2EHPA, Cyanex 272, PC88A |

---

## Detailed Generation Instructions

### Step 1 — Environment setup
```bash
pip install matplotlib numpy scipy
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
- Scatter marker size: 60–80
- Scatter marker styles: use distinct markers per series (e.g. `o`, `s`, `^`, `D`) — one per series, consistent with legend
- Trend line style: solid line, line width 1.8, same color as its series markers but slightly lighter (alpha 0.8)
- Legend: inside plot, upper right or best location to avoid data, light gray frame
- Gridlines: light gray, alpha 0.3, horizontal only unless specified otherwise

### Step 3 — Data generation rules

**For linear trend plots (1–5):**
- Generate x values as evenly spaced points within a realistic range for that variable
- Generate true y values using a linear relationship: `y = m*x + b + noise`
- Choose realistic `m` and `b` per series so lines are distinct and don't overlap completely
- Add gaussian noise: `numpy.random.normal(0, noise_std)` where noise_std is 3–8% of the y range
- Fit and plot using `numpy.polyfit(x, y, 1)`
- If R² shown: compute as `1 - SS_res/SS_tot` and annotate each series on the plot

**For polynomial trend plots (6–10):**
- Generate x values as evenly spaced points within a realistic range
- Generate true y values using a degree-2 polynomial: `y = a*x² + b*x + c + noise`
- Choose coefficients so curves are realistic — avoid extreme parabolas, prefer gentle curves with a clear peak or trough
- Add gaussian noise: `numpy.random.normal(0, noise_std)` where noise_std is 3–8% of y range
- Fit and plot using `numpy.polyfit(x, y, 2)`
- If R² shown: compute and annotate each series on the plot

**R² annotation style:**
- Place R² text near the end of each trend line, not overlapping other series
- Format: `R² = 0.97` (2 decimal places)
- Font size: 8pt, same color as the series

**numpy seeds:**

| Plot # | numpy seed |
|--------|------------|
| 1 | 401 |
| 2 | 402 |
| 3 | 403 |
| 4 | 404 |
| 5 | 405 |
| 6 | 406 |
| 7 | 407 |
| 8 | 408 |
| 9 | 409 |
| 10 | 410 |

### Step 4 — Axis and title formatting

| Plot # | Chart Title | X-Axis Label | Y-Axis Label |
|--------|-------------|--------------|--------------|
| 1 | Effect of pH on REE Extraction with Linear Fitting | pH | Extraction Efficiency (%) |
| 2 | Distribution Ratio vs Extractant Concentration | Extractant Concentration (M) | Distribution Ratio (D) |
| 3 | Temperature Effect on REE Extraction Efficiency | Temperature (°C) | Extraction Efficiency (%) |
| 4 | Stripping Efficiency vs HCl Concentration | HCl Concentration (M) | Stripping Efficiency (%) |
| 5 | REE Recovery vs Contact Time | Contact Time (min) | Recovery (%) |
| 6 | Polynomial Fit of Extraction Efficiency vs pH | pH | Extraction Efficiency (%) |
| 7 | Distribution Ratio vs Temperature (Polynomial Fit) | Temperature (°C) | Distribution Ratio (D) |
| 8 | Extraction Efficiency vs Extractant Concentration | Extractant Concentration (M) | Extraction Efficiency (%) |
| 9 | REE Recovery Kinetics with Polynomial Fitting | Contact Time (min) | Recovery (%) |
| 10 | Separation Factor vs pH for REE Pairs | pH | Separation Factor (α) |

### Step 5 — Ground truth metadata format

For each plot create `scatter_trend{N}.md` with this structure:

~~~markdown
# Ground Truth: scatter_trend{N}

## Plot Configuration

- **Plot type**: Scatter plot with multiple trend lines
- **Trend line type**: [Linear / Polynomial degree 2]
- **Number of series**: [N]
- **Points per series**: [N]
- **R² shown on plot**: [Yes / No]
- **numpy seed**: [seed]

## Data

```json
{
  "title": "[chart title]",
  "x_label": "[x-axis label]",
  "y_label": "[y-axis label]",
  "y_axis_range": [min, max],
  "trend_type": "[linear / polynomial_deg2]",
  "series": [
    {
      "name": "[series name]",
      "points": [
        {"x": [exact float], "y": [exact float]},
        {"x": [exact float], "y": [exact float]}
      ],
      "trend_coefficients": [list of exact floats from polyfit, highest degree first],
      "r_squared": [float or null if not shown]
    }
  ]
}
```

## Notes

[Any special formatting notes — e.g. R² annotation positions, marker styles used per series, legend placement]
~~~

**Critical:**
- `points` must contain the exact (x, y) coordinates of every scatter point plotted
- `trend_coefficients` must be the exact output of `numpy.polyfit` — `[m, b]` for linear, `[a, b, c]` for polynomial
- `r_squared` must be the exact computed value, or null if not displayed on the plot
- This is the ground truth against which extraction accuracy will be measured

### Step 6 — File output and validation

After generating all files:
1. Verify all 20 files exist in the correct Desktop path
2. Verify each PNG is 2400 × 1800 px
3. Verify each MD file contains valid JSON
4. Print a confirmation list of all 20 file paths

---

## Validation Checklist

Before finishing, verify each plot:

- [ ] Title matches specification exactly
- [ ] X and Y axis labels match exactly
- [ ] Correct number of series
- [ ] Correct trend line type (linear vs polynomial)
- [ ] Each series has distinct marker style AND color
- [ ] Trend lines are visually distinct from scatter points (same color, lighter)
- [ ] R² annotations present only where specified, correctly placed
- [ ] Legend present and correctly labeled with series names
- [ ] DPI is 300
- [ ] Ground truth JSON contains all scatter points, trend coefficients, and R² values
- [ ] numpy seed matches seed table
- [ ] Files saved to correct Desktop path

---

*This document is part of the REE Extraction Pipeline Benchmark Suite — Scatter Plots with Multiple Trend Lines (Suite 5 of 5).*
