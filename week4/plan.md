# Plan: Generate 7 Synthetic REE Scatter Plots

## Context
Generate 7 scatter plots with ground truth JSON files themed around rare earth element (REE) extraction science. Each plot needs realistic axis ranges/units and must follow specific correlation and series-count rules.

## Output Directory
`C:/Users/Rithika/benchmark/scatter_plots/` (create if not exists)

## Plot Specifications

| ID | Title | X-axis | Y-axis | Correlation | Series |
|----|-------|--------|--------|-------------|--------|
| scatter_01 | Effect of HCl Concentration on Nd Extraction | HCl Concentration (mol/L) [0.5–6.0] | Nd Extraction Efficiency (%) [20–98] | Strong positive | 1 |
| scatter_02 | Temperature Dependence of Ce Recovery | Temperature (°C) [25–90] | Ce Recovery Rate (%) [15–95] | Strong positive | 1 |
| scatter_03 | La Leaching Yield vs Contact Time | Contact Time (min) [10–180] | La Leaching Yield (%) [30–95] | Strong positive | 1 |
| scatter_04 | Ore Particle Size Effect on Dy Extraction | Ore Particle Size (μm) [50–500] | Dy Extraction Efficiency (%) [30–80] | Weak/noisy | 1 |
| scatter_05 | pH Influence on Eu Distribution Coefficient | pH [1.0–5.0] | Eu Distribution Coefficient (Kd) [0.5–15] | Weak/noisy | 1 |
| scatter_06 | D2EHPA Concentration vs Separation Factor | D2EHPA Concentration (mol/L) [0.1–1.0] | Separation Factor (β) [1.0–8.0] | Positive (varies by pair) | 2 (Nd/Pr, La/Ce) |
| scatter_07 | REE Recovery During Acid Leaching | Leaching Time (h) [0.5–8.0] | Recovery (%) [10–95] | Mixed | 3 (La, Ce, Nd) |

## Implementation — Single Python Script

Create `benchmark/scatter_plots/generate_scatter_plots.py` that:

### Step 1: Generate ground truth data
- Use `numpy` with a fixed random seed for reproducibility
- For each plot, generate x-values uniformly spaced (+ slight jitter) across the range
- Compute y-values using a base function + noise:
  - **Strong positive** (01–03): `y = a*x + b + noise(σ_small)` or gentle curve, r > 0.9
  - **Weak/noisy** (04–05): `y = a*x + b + noise(σ_large)`, r ~ 0.3–0.6
  - **Multi-series** (06–07): each series gets its own slope/offset
- Round all values to 1–2 decimal places
- 20 points per single-series plot; 15–20 points per series in multi-series plots
- Save each as `scatter_XX_gt.json` in the specified JSON schema

### Step 2: Plot from JSON (not from raw arrays)
- Re-read each JSON file to guarantee the plotted values exactly match ground truth
- **Scientific journal style:**
  - Muted color palette (e.g., `['#2b6ca3', '#d45e00', '#2ca02c']`)
  - Open markers: `'o'`, `'s'`, `'^'` with `facecolors='none'`, `edgecolors=color`
  - White background, no top/right spines (`ax.spines['top'].set_visible(False)`)
  - Font: serif family, ~10pt for labels, ~11pt for title
  - Figure size: `(6, 4.5)` for clean proportions
- Title, axis labels with units
- Legend (even for single series — shows element/pair name)
- Light gridlines (`alpha=0.3`, dashed)
- Save as `scatter_XX.jpg` at 300 DPI, `bbox_inches='tight'`

## Files Created
- `benchmark/scatter_plots/generate_scatter_plots.py` — the generator script
- `benchmark/scatter_plots/scatter_01_gt.json` through `scatter_07_gt.json` — ground truth
- `benchmark/scatter_plots/scatter_01.jpg` through `scatter_07.jpg` — plot images

## Verification
1. Run the script: `python benchmark/scatter_plots/generate_scatter_plots.py`
2. Confirm 14 files exist (7 JSON + 7 JPG) in `benchmark/scatter_plots/`
3. Spot-check a JSON file to verify schema and value ranges
4. Open a JPG to verify labels, legend, gridlines, and DPI
