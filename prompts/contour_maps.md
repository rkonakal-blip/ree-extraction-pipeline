# Contour Map Synthetic Benchmark — Generation Spec

## Purpose

Generate **10 synthetic contour map images** and paired **ground truth JSON metadata files** for the REE extraction pipeline benchmark. Contour maps are common in Response Surface Methodology (RSM) optimization studies in REE extraction literature, where two process variables are plotted against each other and the response (e.g. extraction efficiency) is shown as a color gradient or contour lines.

---

## Output Requirements

For each of the 10 plots, produce **two files**:

1. **Image**: `contour{N}.png`
   - Format: PNG, 300 DPI, 8 × 6 inches (2400 × 1800 px)
   - Style: Clean, publication-quality, white background

2. **Ground truth**: `contour{N}.md`
   - Markdown file containing a structured JSON block with exact values used to generate the plot

### Save location — CRITICAL

Save ALL 20 files to this exact path:
```
C:\Users\Rithika\Desktop\ree-extraction-pipeline\benchmark\contour_maps\
```

Create the `contour_maps\` folder if it does not exist. Do not save anywhere else. After generation, print the full path of every file saved as confirmation.

---

## Variation Table

Plots 1–5 are **filled contour** (contourf). Plots 6–8 are **line contour only** (contour). Plots 9–10 are **overlaid** (contourf + contour lines on top).

| Plot # | Style | Z Metric | X-Axis Variable | Y-Axis Variable | X Range | Y Range | Colormap | Contour levels | Colorbar | Labels on lines |
|--------|-------|----------|-----------------|-----------------|---------|---------|----------|----------------|----------|-----------------|
| 1 | Filled | Extraction efficiency (%) | pH | Extractant conc. (M) | 1.0–4.0 | 0.1–2.0 | viridis | 10 | Yes | No |
| 2 | Filled | Extraction efficiency (%) | Temperature (°C) | Contact time (min) | 20–70 | 5–60 | RdYlGn | 12 | Yes | No |
| 3 | Filled | Recovery (%) | pH | Temperature (°C) | 1.5–4.5 | 25–65 | plasma | 10 | Yes | No |
| 4 | Filled | Extraction efficiency (%) | Extractant conc. (M) | A:O ratio | 0.1–2.0 | 0.5–3.0 | coolwarm | 8 | Yes | No |
| 5 | Filled | Distribution ratio D | pH | Temperature (°C) | 1.0–5.0 | 20–60 | YlOrRd | 10 | Yes | No |
| 6 | Line only | Extraction efficiency (%) | pH | Extractant conc. (M) | 1.0–4.0 | 0.1–2.0 | None (black lines) | 8 | No | Yes |
| 7 | Line only | Recovery (%) | Temperature (°C) | Contact time (min) | 20–70 | 5–60 | None (black lines) | 10 | No | Yes |
| 8 | Line only | Extraction efficiency (%) | pH | A:O ratio | 1.5–4.5 | 0.5–3.0 | None (black lines) | 8 | No | Yes |
| 9 | Overlaid | Extraction efficiency (%) | pH | Temperature (°C) | 1.0–4.0 | 25–65 | viridis | 12 | Yes | Yes |
| 10 | Overlaid | Recovery (%) | Extractant conc. (M) | Contact time (min) | 0.1–2.0 | 5–60 | RdYlGn | 10 | Yes | Yes |

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
- Colorbar label: same as Z metric (e.g. "Extraction Efficiency (%)")
- Colorbar font size: 10pt
- Contour line labels (where specified): inline, font size 8pt, format to 1 decimal place
- For line-only plots: use solid black lines, line width 1.0
- For overlaid plots: filled contour underneath, black contour lines on top, line width 0.8

### Step 3 — Data generation rules

For each plot:
- Create a 2D meshgrid of X and Y values using `numpy.meshgrid` with **50 points per axis**
- Generate the Z surface using a realistic 2D polynomial response surface:
  ```python
  Z = a0 + a1*X + a2*Y + a3*X*Y + a4*X**2 + a5*Y**2 + noise
  ```
- Choose coefficients so the surface has a realistic shape for REE extraction:
  - Extraction efficiency and recovery surfaces should have a clear optimum (peak) somewhere in the middle of the grid — not at the edges
  - Distribution ratio D surfaces can be monotonically increasing or have a gentle peak
  - Add small gaussian noise: `numpy.random.normal(0, noise_std)` where noise_std is 1–3% of Z range
- Clip Z values to realistic ranges:
  - Extraction efficiency (%): 0–100
  - Recovery (%): 0–100
  - Distribution ratio D: 0–20
- **Do not use perfectly round numbers** for coefficients

**numpy seeds:**

| Plot # | numpy seed |
|--------|------------|
| 1 | 601 |
| 2 | 602 |
| 3 | 603 |
| 4 | 604 |
| 5 | 605 |
| 6 | 606 |
| 7 | 607 |
| 8 | 608 |
| 9 | 609 |
| 10 | 610 |

### Step 4 — Axis and title formatting

| Plot # | Chart Title | X-Axis Label | Y-Axis Label | Colorbar Label |
|--------|-------------|--------------|--------------|----------------|
| 1 | Effect of pH and Extractant Concentration on Nd Extraction | pH | Extractant Concentration (M) | Extraction Efficiency (%) |
| 2 | RSM Contour Plot: Temperature and Contact Time Effect on La Extraction | Temperature (°C) | Contact Time (min) | Extraction Efficiency (%) |
| 3 | Recovery of Ce as a Function of pH and Temperature | pH | Temperature (°C) | Recovery (%) |
| 4 | Extraction Efficiency vs Extractant Concentration and A:O Ratio | Extractant Concentration (M) | A:O Ratio | Extraction Efficiency (%) |
| 5 | Distribution Ratio of Nd vs pH and Temperature | pH | Temperature (°C) | Distribution Ratio (D) |
| 6 | Contour Lines: pH and Extractant Concentration Effect on Pr Extraction | pH | Extractant Concentration (M) | Extraction Efficiency (%) |
| 7 | Contour Lines: Temperature and Contact Time Effect on Recovery | Temperature (°C) | Contact Time (min) | Recovery (%) |
| 8 | Contour Lines: pH and A:O Ratio Effect on Sm Extraction | pH | A:O Ratio | Extraction Efficiency (%) |
| 9 | RSM Surface: pH and Temperature Optimization for La Extraction | pH | Temperature (°C) | Extraction Efficiency (%) |
| 10 | RSM Surface: Extractant Concentration and Contact Time for Ce Recovery | Extractant Concentration (M) | Contact Time (min) | Recovery (%) |

### Step 5 — Ground truth metadata format

For each plot create `contour{N}.md` with this structure:

~~~markdown
# Ground Truth: contour{N}

## Plot Configuration

- **Plot type**: Contour map
- **Style**: [Filled / Line only / Overlaid]
- **Z metric**: [metric name]
- **X variable**: [variable name and range]
- **Y variable**: [variable name and range]
- **Grid resolution**: 50 × 50
- **Number of contour levels**: [N]
- **Colormap**: [name or None]
- **Contour line labels shown**: [Yes / No]
- **numpy seed**: [seed]

## Data

```json
{
  "title": "[chart title]",
  "x_label": "[x-axis label]",
  "y_label": "[y-axis label]",
  "colorbar_label": "[colorbar label or null]",
  "x_range": [min, max],
  "y_range": [min, max],
  "z_range": [min, max],
  "grid_resolution": 50,
  "polynomial_coefficients": {
    "a0": [float],
    "a1": [float],
    "a2": [float],
    "a3": [float],
    "a4": [float],
    "a5": [float]
  },
  "contour_levels": [list of exact float values used as contour levels],
  "optimal_point": {
    "x": [float],
    "y": [float],
    "z": [float]
  }
}
```

## Notes

[Any special formatting notes — e.g. colormap used, line label positions, noise std used]
~~~

**Critical:**
- `polynomial_coefficients` must be the exact values used to generate the Z surface
- `contour_levels` must be the exact list of level values passed to matplotlib's contour/contourf
- `optimal_point` is the (x, y) location of the maximum Z value on the grid and its Z value — this is the key extraction target for RSM plots
- `z_range` is the actual min and max of the generated Z surface after clipping

### Step 6 — File output and validation

After generating all files:
1. Verify all 20 files exist in `C:\Users\Rithika\Desktop\ree-extraction-pipeline\benchmark\contour_maps\`
2. Verify each PNG is 2400 × 1800 px
3. Verify each MD file contains valid JSON
4. Print a confirmation list of all 20 file paths

---

## Validation Checklist

Before finishing, verify each plot:

- [ ] Title matches specification exactly
- [ ] X and Y axis labels match exactly
- [ ] Colorbar present and labeled for filled and overlaid plots
- [ ] No colorbar for line-only plots
- [ ] Contour line labels present only where specified
- [ ] Correct style applied (filled / line only / overlaid)
- [ ] Correct colormap applied
- [ ] Correct number of contour levels
- [ ] Z surface has a visible optimum within the grid (not at edges)
- [ ] DPI is 300
- [ ] Ground truth JSON contains polynomial coefficients, contour levels, and optimal point
- [ ] numpy seed matches seed table
- [ ] Files saved to C:\Users\Rithika\Desktop\ree-extraction-pipeline\benchmark\contour_maps\

---

*This document is part of the REE Extraction Pipeline Benchmark Suite — Contour Maps (Suite 6 of 7).*
