# Stacked Bar Chart Synthetic Benchmark — Generation Spec

## Purpose

Generate **10 synthetic stacked bar chart images** and paired **ground truth JSON metadata files** for the REE extraction pipeline benchmark.

---

## Output Requirements

For each of the 10 plots, produce **two files**:

1. **Image**: `stacked_barplot{N}.png`
   - Format: PNG, 300 DPI, 8 × 6 inches (2400 × 1800 px)
   - Style: Clean, publication-quality, white background

2. **Ground truth**: `stacked_barplot{N}.md`
   - Markdown file containing a structured JSON block with exact values used to generate the plot

### Save location — CRITICAL

Save ALL 20 files to this exact path:
```
C:\Users\%USERNAME%\Desktop\ree-extraction-pipeline\benchmark\bar_charts\stacked\
```

If `%USERNAME%` does not resolve, use the actual Windows username of the current session. Do not save anywhere else. After generation, print the full path of every file saved as confirmation.

---

## Variation Table

| Plot # | # Groups (X) | # Segments per bar | Orientation | Y-Axis Metric | X-Axis Categories | Y-Axis Range | Color scheme | Gridlines | Legend |
|--------|-------------|-------------------|-------------|---------------|-------------------|--------------|--------------|-----------|--------|
| 1 | 5 | 3 | Vertical | Extraction efficiency (%) | pH (1.5, 2.0, 2.5, 3.0, 3.5) | 0–100 | tab10, 3 colors | Horizontal only | Yes |
| 2 | 4 | 4 | Vertical | Mass distribution (%) | REE elements (La, Ce, Nd, Pr) | 0–100 | tab10, 4 colors | Horizontal only | Yes |
| 3 | 6 | 3 | Vertical | Extraction efficiency (%) | Temperature °C (20, 30, 40, 50, 60, 70) | 0–100 | Set2, 3 colors | Horizontal only | Yes |
| 4 | 5 | 5 | Vertical | Composition (%) | Reagent types (D2EHPA, Cyanex 272, PC88A, TBP, EHEHPA) | 0–100 | tab10, 5 colors | Horizontal only | Yes |
| 5 | 4 | 3 | Horizontal | Mass balance (mg) | Leaching stages (Stage 1, Stage 2, Stage 3, Stage 4) | 0–500 | Set1, 3 colors | Vertical only | Yes |
| 6 | 6 | 4 | Vertical | Extraction efficiency (%) | Contact time min (5, 10, 20, 30, 45, 60) | 0–100 | tab20, 4 colors | Horizontal only | Yes |
| 7 | 5 | 3 | Vertical | Species distribution (%) | Aqueous pH (1, 2, 3, 4, 5) | 0–100 | Paired, 3 colors | Horizontal only | Yes |
| 8 | 4 | 6 | Vertical | Elemental composition (%) | Ore samples (S1, S2, S3, S4) | 0–100 | tab10, 6 colors | Horizontal only | Yes |
| 9 | 5 | 4 | Vertical | Recovery (%) | A:O ratio (1:3, 1:2, 1:1, 2:1, 3:1) | 0–100 | Set2, 4 colors | Horizontal only | Yes |
| 10 | 6 | 3 | Horizontal | Concentration (mg/L) | REE elements (La, Ce, Pr, Nd, Sm, Eu) | 0–300 | tab10, 3 colors | Vertical only | Yes |

---

## Segment Labels

Each stacked bar has named segments. Use these for all plots:

| Plot # | Segment names (bottom → top) |
|--------|------------------------------|
| 1 | Organic phase, Aqueous phase, Interfacial |
| 2 | Extracted, Raffinate, Scrubbed, Stripped |
| 3 | D2EHPA fraction, PC88A fraction, Residual |
| 4 | La, Ce, Nd, Pr, Others |
| 5 | REE fraction, Iron impurity, Silica impurity |
| 6 | Fast extraction, Slow extraction, Equilibrium, Residual |
| 7 | Free ion, Mono-complex, Di-complex |
| 8 | La, Ce, Nd, Pr, Sm, Others |
| 9 | Extracted, Co-extracted, Scrubbed, Stripped |
| 10 | Extracted fraction, Aqueous residual, Precipitated |

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
- Bar width: 0.55 for vertical, 0.5 for horizontal
- Bar edge: black, line width 0.6
- Legend: inside plot, upper right, light gray frame
- X-tick labels: rotate 45° right-aligned when labels are long (reagent names, phase names); keep horizontal for short labels (pH values, temperatures, ratios)

### Step 3 — Data generation rules
- All segment values within a single bar **must sum to exactly 100%** for percentage metrics, or to a realistic total for absolute metrics
- Use `numpy` with fixed seeds (see table below) — one seed per plot
- Values must be **realistic** for REE extraction literature — no perfectly round numbers
- Bottom segment has an absolute baseline (y=0); all segments above it require subtraction to get true height — the ground truth JSON must store both the **raw segment value** and the **cumulative bottom** for each segment

| Plot # | numpy seed |
|--------|------------|
| 1 | 201 |
| 2 | 202 |
| 3 | 203 |
| 4 | 204 |
| 5 | 205 |
| 6 | 206 |
| 7 | 207 |
| 8 | 208 |
| 9 | 209 |
| 10 | 210 |

### Step 4 — Axis and title formatting

| Plot # | Chart Title | X-Axis Label | Y-Axis Label |
|--------|-------------|--------------|--------------|
| 1 | Phase Distribution Across pH Levels | pH | Proportion (%) |
| 2 | REE Mass Distribution After Solvent Extraction | REE Element | Mass Distribution (%) |
| 3 | Extraction Fraction by Temperature | Temperature (°C) | Extraction Efficiency (%) |
| 4 | Reagent Composition Effect on REE Recovery | Extractant | Composition (%) |
| 5 | Mass Balance Across Leaching Stages | Leaching Stage | Mass (mg) |
| 6 | Extraction Kinetics by Contact Time | Contact Time (min) | Extraction Efficiency (%) |
| 7 | Species Distribution vs Aqueous pH | Aqueous pH | Species Distribution (%) |
| 8 | Elemental Composition of Ore Samples | Ore Sample | Elemental Composition (%) |
| 9 | Recovery Distribution Across A:O Ratios | A:O Ratio | Recovery (%) |
| 10 | REE Concentration Distribution After Processing | REE Element | Concentration (mg/L) |

### Step 5 — Ground truth metadata format

For each plot create `stacked_barplot{N}.md` with this structure:

~~~markdown
# Ground Truth: stacked_barplot{N}

## Plot Configuration

- **Plot type**: Stacked bar chart
- **Orientation**: [Vertical / Horizontal]
- **Number of groups**: [N]
- **Number of segments**: [N]
- **Y-axis metric**: [metric]
- **numpy seed**: [seed]

## Data

```json
{
  "title": "[chart title]",
  "x_label": "[x-axis label]",
  "y_label": "[y-axis label]",
  "y_axis_range": [min, max],
  "segments": ["segment1", "segment2", "segment3"],
  "bars": [
    {
      "label": "[x category]",
      "segments": [
        {"name": "segment1", "value": [exact float], "cumulative_bottom": 0.0},
        {"name": "segment2", "value": [exact float], "cumulative_bottom": [exact float]},
        {"name": "segment3", "value": [exact float], "cumulative_bottom": [exact float]}
      ]
    }
  ]
}
```

## Notes

[Any special formatting notes]
~~~

**Critical**: `value` must be the exact float used to draw that segment. `cumulative_bottom` is the sum of all segment values below it — this is essential for accurate extraction evaluation.

### Step 6 — File output and validation

After generating all files:
1. Verify all 20 files exist in `C:\Users\%USERNAME%\Desktop\ree-extraction-pipeline\benchmark\bar_charts\stacked\`
2. Verify each PNG is 2400 × 1800 px
3. Verify each MD file contains valid JSON
4. Print a confirmation list of all 20 file paths

---

## Validation Checklist

Before finishing, verify each plot:

- [ ] Title matches specification exactly
- [ ] X and Y axis labels match exactly
- [ ] Correct number of groups and segments
- [ ] All percentage bars sum to 100%
- [ ] Orientation correct (vertical/horizontal)
- [ ] Correct color scheme applied
- [ ] Gridlines match specification
- [ ] Legend present and correctly labeled
- [ ] DPI is 300
- [ ] Ground truth JSON contains exact values AND cumulative bottoms
- [ ] numpy seed matches seed table
- [ ] Files saved to correct Desktop path

---

*This document is part of the REE Extraction Pipeline Benchmark Suite — Stacked Bar Charts (Suite 3 of 3).*
