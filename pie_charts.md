# Pie Chart Synthetic Benchmark — Generation Spec

## Purpose

Generate **10 synthetic pie chart images** and paired **ground truth JSON metadata files** for the REE extraction pipeline benchmark. Pie charts appear in REE extraction literature primarily for showing elemental composition of ore samples, leachate breakdowns, and phase distributions.

---

## Output Requirements

For each of the 10 plots, produce **two files**:

1. **Image**: `piechart{N}.png`
   - Format: PNG, 300 DPI, 8 × 6 inches (2400 × 1800 px)
   - Style: Clean, publication-quality, white background

2. **Ground truth**: `piechart{N}.md`
   - Markdown file containing a structured JSON block with exact values used to generate the plot

### Save location — CRITICAL

Save ALL 20 files to this exact path:
```
C:\Users\Rithika\Desktop\ree-extraction-pipeline\benchmark\pie_charts\
```

Create the `pie_charts\` folder if it does not exist. Do not save anywhere else. After generation, print the full path of every file saved as confirmation.

---

## Variation Table

| Plot # | # Slices | Label style | Percentage shown | Z Metric | Color scheme | Legend | Start angle |
|--------|----------|-------------|-----------------|----------|--------------|--------|-------------|
| 1 | 5 | Slice labels only | Yes, inside slice | REE elemental composition (%) | tab10 | No | 90 |
| 2 | 6 | Legend only | Yes, inside slice | Leachate composition (%) | Set2 | Yes | 90 |
| 3 | 4 | Slice labels only | Yes, outside slice | Phase distribution (%) | Paired | No | 0 |
| 4 | 7 | Legend only | Yes, inside slice | Ore mineral composition (%) | tab10 | Yes | 90 |
| 5 | 5 | Both label and percentage | Yes, outside slice | Solvent extraction yield (%) | Set1 | No | 45 |
| 6 | 4 | Slice labels only | Yes, inside slice | REE distribution in leachate (%) | tab20 | No | 90 |
| 7 | 6 | Legend only | Yes, inside slice | Impurity breakdown (%) | Set2 | Yes | 0 |
| 8 | 8 | Legend only | Yes, inside slice | Ore sample composition (%) | tab10 | Yes | 90 |
| 9 | 5 | Both label and percentage | Yes, outside slice | Mass balance distribution (%) | Paired | No | 90 |
| 10 | 6 | Slice labels only | Yes, inside slice | REE concentrate composition (%) | Set1 | No | 45 |

---

## Slice Labels

| Plot # | Slice names |
|--------|------------|
| 1 | La, Ce, Nd, Pr, Others |
| 2 | La, Ce, Nd, Pr, Sm, Others |
| 3 | Organic phase, Aqueous phase, Interfacial, Precipitate |
| 4 | La, Ce, Nd, Pr, Sm, Eu, Others |
| 5 | D2EHPA fraction, PC88A fraction, Cyanex fraction, Raffinate, Losses |
| 6 | La, Ce, Nd, Pr |
| 7 | Iron, Calcium, Magnesium, Silica, Aluminum, Others |
| 8 | La, Ce, Nd, Pr, Sm, Eu, Gd, Others |
| 9 | Extracted, Stripped, Scrubbed, Raffinate, Losses |
| 10 | La, Ce, Nd, Pr, Sm, Others |

---

## Detailed Generation Instructions

### Step 1 — Environment setup
```bash
pip install matplotlib numpy
```

### Step 2 — Universal styling (apply to ALL plots)
- Font: DejaVu Sans
- Title font size: 13pt bold
- Percentage label font size: 9pt
- Slice label font size: 9pt
- Figure DPI: 300
- Figure size: (8, 6) inches
- Background: white `#FFFFFF`
- Pie radius: 0.85 (slightly smaller than default to leave room for outside labels)
- Wedge edge color: white, line width 1.5 (clean separation between slices)
- For labels inside slice: only show if slice is large enough (> 5%) — skip label for tiny slices
- For labels outside slice: use matplotlib's default label positioning with leader lines
- Legend (where specified): place to the right of the pie, outside the chart area
- Shadow: False
- Percentage format: `%.1f%%` (one decimal place)

### Step 3 — Data generation rules

- Generate slice values using `numpy.random.dirichlet` to ensure they sum to exactly 100%
- Scale to percentages: `values = numpy.random.dirichlet(alpha) * 100`
- Choose alpha parameters so slices are realistic — not all equal, not one dominant slice taking 90%:
  - Aim for a natural spread: largest slice 25–45%, smallest slice 3–12%
  - Use different alpha vectors per plot to get variety
- **Do not use perfectly round numbers** — keep values to 1–2 decimal places
- All slice values must sum to exactly 100.0%
- Use `numpy` with fixed seeds (see table below)

**numpy seeds:**

| Plot # | numpy seed |
|--------|------------|
| 1 | 701 |
| 2 | 702 |
| 3 | 703 |
| 4 | 704 |
| 5 | 705 |
| 6 | 706 |
| 7 | 707 |
| 8 | 708 |
| 9 | 709 |
| 10 | 710 |

### Step 4 — Axis and title formatting

| Plot # | Chart Title |
|--------|-------------|
| 1 | REE Elemental Composition of Leach Solution |
| 2 | Composition of Leachate After Acid Digestion |
| 3 | Phase Distribution After Solvent Extraction |
| 4 | Mineral Composition of REE Ore Sample |
| 5 | Solvent Extraction Yield Distribution |
| 6 | REE Distribution in Leachate Solution |
| 7 | Impurity Breakdown in Leach Solution |
| 8 | Elemental Composition of REE Ore Sample |
| 9 | Mass Balance Distribution After Processing |
| 10 | REE Concentrate Composition After Stripping |

### Step 5 — Ground truth metadata format

For each plot create `piechart{N}.md` with this structure:

~~~markdown
# Ground Truth: piechart{N}

## Plot Configuration

- **Plot type**: Pie chart
- **Number of slices**: [N]
- **Label style**: [Slice labels only / Legend only / Both label and percentage]
- **Percentage position**: [Inside slice / Outside slice]
- **Start angle**: [degrees]
- **numpy seed**: [seed]

## Data

```json
{
  "title": "[chart title]",
  "start_angle": [float],
  "slices": [
    {
      "label": "[slice name]",
      "value": [exact float],
      "percentage": [exact float]
    }
  ],
  "total": 100.0
}
```

## Notes

[Any special formatting notes — e.g. which slices had labels skipped due to small size, legend position, color order]
~~~

**Critical:**
- `value` and `percentage` are the same thing here (since all values are already in %) — store both explicitly for clarity
- Values must be the exact floats passed to matplotlib's `pie()` function
- All `percentage` values must sum to exactly 100.0
- If any slice label was skipped because the slice was too small (< 5%), note which ones in the Notes section

### Step 6 — File output and validation

After generating all files:
1. Verify all 20 files exist in `C:\Users\Rithika\Desktop\ree-extraction-pipeline\benchmark\pie_charts\`
2. Verify each PNG is 2400 × 1800 px
3. Verify each MD file contains valid JSON
4. Verify all slice percentages sum to 100.0 in each MD file
5. Print a confirmation list of all 20 file paths

---

## Validation Checklist

Before finishing, verify each plot:

- [ ] Title matches specification exactly
- [ ] Correct number of slices
- [ ] Correct label style (inside / outside / legend)
- [ ] Percentage values displayed on plot
- [ ] Legend present only where specified
- [ ] Correct colormap applied
- [ ] Correct start angle applied
- [ ] Slices sum to exactly 100%
- [ ] No perfectly round numbers in slice values
- [ ] Wedge edges are white for clean separation
- [ ] DPI is 300
- [ ] Ground truth JSON contains exact slice values summing to 100.0
- [ ] numpy seed matches seed table
- [ ] Files saved to C:\Users\Rithika\Desktop\ree-extraction-pipeline\benchmark\pie_charts\

---

*This document is part of the REE Extraction Pipeline Benchmark Suite — Pie Charts (Suite 7 of 7).*
