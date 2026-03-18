"""
Generate 10 synthetic scatter plots with multiple trend lines and ground truth
metadata for the REE Extraction Pipeline Benchmark Suite.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import json

# ── Shared styling constants ──────────────────────────────────────────
FIGSIZE = (8, 6)
DPI = 300
TITLE_FONTSIZE = 13
AXIS_LABEL_FONTSIZE = 11
TICK_LABEL_FONTSIZE = 9
MARKER_SIZE = 70
TREND_LW = 1.8
TREND_ALPHA = 0.8
R2_FONTSIZE = 8
GRID_ALPHA = 0.3

MARKERS = ['o', 's', '^', 'D', 'v', 'P']

# ── Plot configurations ──────────────────────────────────────────────
PLOTS = [
    {  # Plot 1 — Linear
        "num": 1, "seed": 401,
        "n_series": 3, "trend_type": "linear", "points_per_series": 8,
        "series_names": ["D2EHPA", "Cyanex 272", "PC88A"],
        "title": "Effect of pH on REE Extraction with Linear Fitting",
        "x_label": "pH", "y_label": "Extraction Efficiency (%)",
        "y_range": [0, 100],
        "x_range": (1.0, 5.0),
        "colormap": "tab10", "n_colors": 3,
        "show_r2": True,
        # Linear params per series: (slope, intercept)
        "linear_params": [(12.0, 25.0), (8.0, 40.0), (15.0, 10.0)],
        "noise_std": 4.0,
    },
    {  # Plot 2 — Linear
        "num": 2, "seed": 402,
        "n_series": 2, "trend_type": "linear", "points_per_series": 10,
        "series_names": ["La", "Nd"],
        "title": "Distribution Ratio vs Extractant Concentration",
        "x_label": "Extractant Concentration (M)", "y_label": "Distribution Ratio (D)",
        "y_range": [0, 15],
        "x_range": (0.05, 2.0),
        "colormap": "Set1", "n_colors": 2,
        "show_r2": True,
        "linear_params": [(5.5, 1.2), (3.8, 2.5)],
        "noise_std": 0.6,
    },
    {  # Plot 3 — Linear
        "num": 3, "seed": 403,
        "n_series": 4, "trend_type": "linear", "points_per_series": 7,
        "series_names": ["La", "Ce", "Nd", "Pr"],
        "title": "Temperature Effect on REE Extraction Efficiency",
        "x_label": "Temperature (\u00b0C)", "y_label": "Extraction Efficiency (%)",
        "y_range": [30, 100],
        "x_range": (20.0, 70.0),
        "colormap": "tab10", "n_colors": 4,
        "show_r2": False,
        "linear_params": [(0.8, 35.0), (0.6, 45.0), (1.0, 28.0), (0.5, 50.0)],
        "noise_std": 3.5,
    },
    {  # Plot 4 — Linear
        "num": 4, "seed": 404,
        "n_series": 2, "trend_type": "linear", "points_per_series": 9,
        "series_names": ["D2EHPA", "PC88A"],
        "title": "Stripping Efficiency vs HCl Concentration",
        "x_label": "HCl Concentration (M)", "y_label": "Stripping Efficiency (%)",
        "y_range": [20, 100],
        "x_range": (0.5, 4.0),
        "colormap": "Paired", "n_colors": 2,
        "show_r2": True,
        "linear_params": [(15.0, 25.0), (12.0, 35.0)],
        "noise_std": 4.5,
    },
    {  # Plot 5 — Linear
        "num": 5, "seed": 405,
        "n_series": 3, "trend_type": "linear", "points_per_series": 8,
        "series_names": ["D2EHPA", "Cyanex 272", "PC88A"],
        "title": "REE Recovery vs Contact Time",
        "x_label": "Contact Time (min)", "y_label": "Recovery (%)",
        "y_range": [40, 100],
        "x_range": (5.0, 60.0),
        "colormap": "Set2", "n_colors": 3,
        "show_r2": False,
        "linear_params": [(0.7, 50.0), (0.5, 55.0), (0.9, 42.0)],
        "noise_std": 3.0,
    },
    {  # Plot 6 — Polynomial
        "num": 6, "seed": 406,
        "n_series": 2, "trend_type": "polynomial", "points_per_series": 10,
        "series_names": ["La", "Nd"],
        "title": "Polynomial Fit of Extraction Efficiency vs pH",
        "x_label": "pH", "y_label": "Extraction Efficiency (%)",
        "y_range": [0, 100],
        "x_range": (1.0, 5.0),
        "colormap": "tab10", "n_colors": 2,
        "show_r2": True,
        # Poly params per series: (a, b, c) for y = a*x^2 + b*x + c
        "poly_params": [(-8.0, 55.0, -10.0), (-6.0, 45.0, 5.0)],
        "noise_std": 4.0,
    },
    {  # Plot 7 — Polynomial
        "num": 7, "seed": 407,
        "n_series": 3, "trend_type": "polynomial", "points_per_series": 8,
        "series_names": ["D2EHPA", "Cyanex 272", "PC88A"],
        "title": "Distribution Ratio vs Temperature (Polynomial Fit)",
        "x_label": "Temperature (\u00b0C)", "y_label": "Distribution Ratio (D)",
        "y_range": [0, 20],
        "x_range": (20.0, 70.0),
        "colormap": "Set1", "n_colors": 3,
        "show_r2": False,
        "poly_params": [(-0.005, 0.6, -2.0), (-0.004, 0.5, 0.5), (-0.003, 0.4, 1.0)],
        "noise_std": 1.0,
    },
    {  # Plot 8 — Polynomial
        "num": 8, "seed": 408,
        "n_series": 2, "trend_type": "polynomial", "points_per_series": 9,
        "series_names": ["La", "Ce"],
        "title": "Extraction Efficiency vs Extractant Concentration",
        "x_label": "Extractant Concentration (M)", "y_label": "Extraction Efficiency (%)",
        "y_range": [10, 100],
        "x_range": (0.05, 2.0),
        "colormap": "Paired", "n_colors": 2,
        "show_r2": True,
        "poly_params": [(-25.0, 85.0, 15.0), (-20.0, 70.0, 20.0)],
        "noise_std": 4.0,
    },
    {  # Plot 9 — Polynomial
        "num": 9, "seed": 409,
        "n_series": 4, "trend_type": "polynomial", "points_per_series": 7,
        "series_names": ["La", "Ce", "Nd", "Pr"],
        "title": "REE Recovery Kinetics with Polynomial Fitting",
        "x_label": "Contact Time (min)", "y_label": "Recovery (%)",
        "y_range": [20, 100],
        "x_range": (5.0, 60.0),
        "colormap": "tab10", "n_colors": 4,
        "show_r2": False,
        "poly_params": [
            (-0.015, 1.8, 25.0),
            (-0.012, 1.5, 30.0),
            (-0.018, 2.0, 20.0),
            (-0.010, 1.3, 35.0),
        ],
        "noise_std": 3.5,
    },
    {  # Plot 10 — Polynomial
        "num": 10, "seed": 410,
        "n_series": 3, "trend_type": "polynomial", "points_per_series": 8,
        "series_names": ["D2EHPA", "Cyanex 272", "PC88A"],
        "title": "Separation Factor vs pH for REE Pairs",
        "x_label": "pH", "y_label": "Separation Factor (\u03b1)",
        "y_range": [0, 5],
        "x_range": (1.0, 5.0),
        "colormap": "Set2", "n_colors": 3,
        "show_r2": True,
        "poly_params": [(-0.3, 2.5, -1.5), (-0.25, 2.0, -0.8), (-0.2, 1.8, -0.5)],
        "noise_std": 0.2,
    },
]


def get_colors(colormap_name, n_colors):
    cmap = matplotlib.colormaps[colormap_name]
    return [cmap(i) for i in range(n_colors)]


def apply_common_style(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)


def compute_r2(y_actual, y_predicted):
    ss_res = np.sum((y_actual - y_predicted) ** 2)
    ss_tot = np.sum((y_actual - np.mean(y_actual)) ** 2)
    if ss_tot == 0:
        return 1.0
    return 1.0 - ss_res / ss_tot


def generate_plot(cfg, outdir):
    num = cfg["num"]
    rng = np.random.RandomState(cfg["seed"])
    n_series = cfg["n_series"]
    n_pts = cfg["points_per_series"]
    colors = get_colors(cfg["colormap"], cfg["n_colors"])
    x_lo, x_hi = cfg["x_range"]

    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    apply_common_style(ax)

    series_data = []

    for s in range(n_series):
        # Generate evenly spaced x with slight jitter
        x_base = np.linspace(x_lo, x_hi, n_pts)
        x_jitter = rng.uniform(-0.02 * (x_hi - x_lo), 0.02 * (x_hi - x_lo), n_pts)
        x_vals = np.round(x_base + x_jitter, 3)
        # Keep x within range
        x_vals = np.clip(x_vals, x_lo, x_hi)

        # Generate y values
        if cfg["trend_type"] == "linear":
            m, b = cfg["linear_params"][s]
            y_true = m * x_vals + b
        else:
            a, b, c = cfg["poly_params"][s]
            y_true = a * x_vals**2 + b * x_vals + c

        noise = rng.normal(0, cfg["noise_std"], n_pts)
        y_vals = np.round(y_true + noise, 2)

        # Clip y to y_range
        y_lo, y_hi = cfg["y_range"]
        y_vals = np.clip(y_vals, y_lo + 0.5, y_hi - 0.5)
        y_vals = np.round(y_vals, 2)
        x_vals = np.round(x_vals, 3)

        # Fit trend line
        if cfg["trend_type"] == "linear":
            coeffs = np.polyfit(x_vals, y_vals, 1)
        else:
            coeffs = np.polyfit(x_vals, y_vals, 2)

        # Compute R²
        y_pred = np.polyval(coeffs, x_vals)
        r2 = round(compute_r2(y_vals, y_pred), 4)

        # Plot scatter
        marker = MARKERS[s % len(MARKERS)]
        ax.scatter(x_vals, y_vals, color=colors[s], marker=marker,
                   s=MARKER_SIZE, edgecolors='white', linewidths=0.5,
                   label=cfg["series_names"][s], zorder=3)

        # Plot trend line
        x_smooth = np.linspace(x_lo, x_hi, 200)
        y_smooth = np.polyval(coeffs, x_smooth)
        # Clip trend line to y range for visual cleanliness
        y_smooth_clipped = np.clip(y_smooth, y_lo, y_hi)
        ax.plot(x_smooth, y_smooth_clipped, color=colors[s],
                linewidth=TREND_LW, alpha=TREND_ALPHA, zorder=2)

        # R² annotation
        r2_value = r2 if cfg["show_r2"] else None
        if cfg["show_r2"]:
            # Place near end of trend line, staggered vertically to avoid overlap
            x_annot = x_hi - 0.05 * (x_hi - x_lo)
            y_annot = np.polyval(coeffs, x_annot)
            # Offset each series annotation slightly
            y_offset = (s - (n_series - 1) / 2.0) * (y_hi - y_lo) * 0.04
            y_annot_pos = np.clip(y_annot + y_offset, y_lo + 2, y_hi - 2)
            ax.annotate(f"R\u00b2 = {r2:.2f}",
                        xy=(x_annot, y_annot_pos),
                        fontsize=R2_FONTSIZE, color=colors[s],
                        ha='right', va='center', fontweight='bold')

        series_data.append({
            "name": cfg["series_names"][s],
            "points": [{"x": float(x_vals[i]), "y": float(y_vals[i])}
                        for i in range(n_pts)],
            "trend_coefficients": [round(float(c), 6) for c in coeffs],
            "r_squared": r2_value,
        })

    ax.set_xlim(x_lo - 0.05 * (x_hi - x_lo), x_hi + 0.05 * (x_hi - x_lo))
    ax.set_ylim(cfg["y_range"])
    ax.set_xlabel(cfg["x_label"], fontsize=AXIS_LABEL_FONTSIZE)
    ax.set_ylabel(cfg["y_label"], fontsize=AXIS_LABEL_FONTSIZE)
    ax.set_title(cfg["title"], fontsize=TITLE_FONTSIZE, fontweight='bold')
    ax.tick_params(axis='both', labelsize=TICK_LABEL_FONTSIZE)

    # Gridlines — horizontal only
    ax.yaxis.grid(True, linestyle='--', color='lightgray', alpha=GRID_ALPHA)
    ax.xaxis.grid(False)
    ax.set_axisbelow(True)

    # Legend
    ax.legend(loc='best', frameon=True, edgecolor='lightgray',
              fancybox=False, fontsize=TICK_LABEL_FONTSIZE)

    # Save with exact dimensions
    fig.set_size_inches(8, 6)
    fig.subplots_adjust(left=0.12, right=0.95, top=0.92, bottom=0.12)

    png_path = os.path.join(outdir, f"scatter_trend{num}.png")
    fig.savefig(png_path, dpi=DPI, facecolor='white')
    plt.close(fig)

    # Write metadata
    write_metadata(cfg, series_data, outdir)
    print(f"  Generated scatter_trend{num}.png and scatter_trend{num}.md")


def write_metadata(cfg, series_data, outdir):
    num = cfg["num"]
    trend_str = "Linear" if cfg["trend_type"] == "linear" else "Polynomial degree 2"
    trend_json = "linear" if cfg["trend_type"] == "linear" else "polynomial_deg2"
    r2_str = "Yes" if cfg["show_r2"] else "No"

    json_data = {
        "title": cfg["title"],
        "x_label": cfg["x_label"],
        "y_label": cfg["y_label"],
        "y_axis_range": cfg["y_range"],
        "trend_type": trend_json,
        "series": series_data,
    }
    json_str = json.dumps(json_data, indent=2)

    notes_parts = []
    notes_parts.append(f"Color scheme: {cfg['colormap']} with {cfg['n_colors']} colors.")
    markers_used = [MARKERS[s % len(MARKERS)] for s in range(cfg["n_series"])]
    marker_desc = ", ".join(f"{cfg['series_names'][s]}: '{markers_used[s]}'"
                            for s in range(cfg["n_series"]))
    notes_parts.append(f"Marker styles: {marker_desc}.")
    notes_parts.append("Trend lines: solid, linewidth 1.8, alpha 0.8.")
    if cfg["show_r2"]:
        notes_parts.append("R\u00b2 annotations shown near end of each trend line.")
    notes_parts.append("Horizontal gridlines only (light gray, alpha 0.3).")
    notes_parts.append("Legend placed at best location to avoid data overlap.")
    notes_text = " ".join(notes_parts)

    md = f"""# Ground Truth: scatter_trend{num}

## Plot Configuration

- **Plot type**: Scatter plot with multiple trend lines
- **Trend line type**: {trend_str}
- **Number of series**: {cfg['n_series']}
- **Points per series**: {cfg['points_per_series']}
- **R\u00b2 shown on plot**: {r2_str}
- **numpy seed**: {cfg['seed']}

## Data

```json
{json_str}
```

## Notes

{notes_text}
"""
    filepath = os.path.join(outdir, f"scatter_trend{num}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)


def validate(outdir):
    from PIL import Image
    all_ok = True
    for i in range(1, 11):
        png = os.path.join(outdir, f"scatter_trend{i}.png")
        md = os.path.join(outdir, f"scatter_trend{i}.md")

        for fpath in (png, md):
            if not os.path.isfile(fpath):
                print(f"  MISSING: {fpath}")
                all_ok = False
            elif os.path.getsize(fpath) == 0:
                print(f"  EMPTY: {fpath}")
                all_ok = False

        if os.path.isfile(png):
            img = Image.open(png)
            w, h = img.size
            if (w, h) != (2400, 1800):
                print(f"  scatter_trend{i}.png: size {w}x{h} (expected 2400x1800)")

        if os.path.isfile(md):
            with open(md, 'r', encoding='utf-8') as f:
                content = f.read()
            try:
                json_start = content.index('```json\n') + 8
                json_end = content.index('\n```', json_start)
                parsed = json.loads(content[json_start:json_end])
                for series in parsed["series"]:
                    if "points" not in series or "trend_coefficients" not in series:
                        print(f"  scatter_trend{i}.md: missing points or trend_coefficients")
                        all_ok = False
                    n_expected = len(series["points"])
                    if n_expected < 5:
                        print(f"  scatter_trend{i}.md: series '{series['name']}' has only {n_expected} points")
            except (ValueError, json.JSONDecodeError) as e:
                print(f"  scatter_trend{i}.md: JSON parse error — {e}")
                all_ok = False

    return all_ok


def main():
    outdir = os.path.dirname(os.path.abspath(__file__))
    print(f"Output directory: {outdir}")
    print(f"Generating 10 scatter plots with trend lines...\n")

    for cfg in PLOTS:
        generate_plot(cfg, outdir)

    print(f"\nValidating outputs...")
    ok = validate(outdir)

    print(f"\n{'='*60}")
    if ok:
        print("All 20 files generated and validated successfully!")
    else:
        print("Some validation issues found (see above).")
    print(f"{'='*60}")

    files = sorted(f for f in os.listdir(outdir)
                   if f.startswith('scatter_trend') and (f.endswith('.png') or f.endswith('.md')))
    print(f"\nGenerated files ({len(files)}):")
    for f in files:
        full = os.path.join(outdir, f)
        size = os.path.getsize(full)
        print(f"  {full}  ({size:,} bytes)")


if __name__ == "__main__":
    main()
