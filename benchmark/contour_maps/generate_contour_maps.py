"""
Generate 10 synthetic contour map images with ground truth metadata
for the REE Extraction Pipeline Benchmark Suite.
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
COLORBAR_FONTSIZE = 10
CLABEL_FONTSIZE = 8
LINE_LW = 1.0
OVERLAY_LINE_LW = 0.8
GRID_RES = 50

# ── Plot configurations ──────────────────────────────────────────────

# Coefficient design: Z = a0 + a1*X + a2*Y + a3*X*Y + a4*X^2 + a5*Y^2
# For a peak at (x_opt, y_opt): x_opt = -(a1 + a3*y_opt)/(2*a4), similar for y
# We design coefficients so the peak falls near the center of each grid.

PLOTS = [
    {  # Plot 1 — Filled
        "num": 1, "seed": 601, "style": "filled",
        "title": "Effect of pH and Extractant Concentration on Nd Extraction",
        "x_label": "pH", "y_label": "Extractant Concentration (M)",
        "colorbar_label": "Extraction Efficiency (%)",
        "x_range": [1.0, 4.0], "y_range": [0.1, 2.0],
        "z_metric": "extraction_eff", "z_clip": [0, 100],
        "colormap": "viridis", "n_levels": 10,
        "show_colorbar": True, "show_labels": False,
        # Peak near pH=2.5, conc=1.1
        "coeffs": {"a0": -45.3, "a1": 62.8, "a2": 55.4, "a3": 2.7, "a4": -12.3, "a5": -22.1},
        "noise_std": 1.5,
    },
    {  # Plot 2 — Filled
        "num": 2, "seed": 602, "style": "filled",
        "title": "RSM Contour Plot: Temperature and Contact Time Effect on La Extraction",
        "x_label": "Temperature (\u00b0C)", "y_label": "Contact Time (min)",
        "colorbar_label": "Extraction Efficiency (%)",
        "x_range": [20, 70], "y_range": [5, 60],
        "z_metric": "extraction_eff", "z_clip": [0, 100],
        "colormap": "RdYlGn", "n_levels": 12,
        "show_colorbar": True, "show_labels": False,
        # Peak near T=48, t=38
        "coeffs": {"a0": -120.7, "a1": 6.13, "a2": 3.82, "a3": 0.012, "a4": -0.063, "a5": -0.048},
        "noise_std": 2.0,
    },
    {  # Plot 3 — Filled
        "num": 3, "seed": 603, "style": "filled",
        "title": "Recovery of Ce as a Function of pH and Temperature",
        "x_label": "pH", "y_label": "Temperature (\u00b0C)",
        "colorbar_label": "Recovery (%)",
        "x_range": [1.5, 4.5], "y_range": [25, 65],
        "z_metric": "recovery", "z_clip": [0, 100],
        "colormap": "plasma", "n_levels": 10,
        "show_colorbar": True, "show_labels": False,
        # Peak near pH=3.0, T=45
        "coeffs": {"a0": -185.4, "a1": 98.2, "a2": 5.73, "a3": 0.35, "a4": -15.8, "a5": -0.061},
        "noise_std": 1.8,
    },
    {  # Plot 4 — Filled
        "num": 4, "seed": 604, "style": "filled",
        "title": "Extraction Efficiency vs Extractant Concentration and A:O Ratio",
        "x_label": "Extractant Concentration (M)", "y_label": "A:O Ratio",
        "colorbar_label": "Extraction Efficiency (%)",
        "x_range": [0.1, 2.0], "y_range": [0.5, 3.0],
        "z_metric": "extraction_eff", "z_clip": [0, 100],
        "colormap": "coolwarm", "n_levels": 8,
        "show_colorbar": True, "show_labels": False,
        # Peak near conc=1.1, A:O=1.8
        "coeffs": {"a0": -32.6, "a1": 78.3, "a2": 42.5, "a3": 5.1, "a4": -33.7, "a5": -11.2},
        "noise_std": 1.5,
    },
    {  # Plot 5 — Filled
        "num": 5, "seed": 605, "style": "filled",
        "title": "Distribution Ratio of Nd vs pH and Temperature",
        "x_label": "pH", "y_label": "Temperature (\u00b0C)",
        "colorbar_label": "Distribution Ratio (D)",
        "x_range": [1.0, 5.0], "y_range": [20, 60],
        "z_metric": "distribution_ratio", "z_clip": [0, 20],
        "colormap": "YlOrRd", "n_levels": 10,
        "show_colorbar": True, "show_labels": False,
        # Gentle peak near pH=3.5, T=42
        "coeffs": {"a0": -25.8, "a1": 12.3, "a2": 0.68, "a3": 0.05, "a4": -1.72, "a5": -0.008},
        "noise_std": 0.3,
    },
    {  # Plot 6 — Line only
        "num": 6, "seed": 606, "style": "line",
        "title": "Contour Lines: pH and Extractant Concentration Effect on Pr Extraction",
        "x_label": "pH", "y_label": "Extractant Concentration (M)",
        "colorbar_label": "Extraction Efficiency (%)",
        "x_range": [1.0, 4.0], "y_range": [0.1, 2.0],
        "z_metric": "extraction_eff", "z_clip": [0, 100],
        "colormap": None, "n_levels": 8,
        "show_colorbar": False, "show_labels": True,
        # Peak near pH=2.7, conc=1.2
        "coeffs": {"a0": -52.1, "a1": 65.4, "a2": 48.7, "a3": 3.2, "a4": -11.8, "a5": -18.9},
        "noise_std": 1.2,
    },
    {  # Plot 7 — Line only
        "num": 7, "seed": 607, "style": "line",
        "title": "Contour Lines: Temperature and Contact Time Effect on Recovery",
        "x_label": "Temperature (\u00b0C)", "y_label": "Contact Time (min)",
        "colorbar_label": "Recovery (%)",
        "x_range": [20, 70], "y_range": [5, 60],
        "z_metric": "recovery", "z_clip": [0, 100],
        "colormap": None, "n_levels": 10,
        "show_colorbar": False, "show_labels": True,
        # Peak near T=50, t=35
        "coeffs": {"a0": -135.2, "a1": 6.85, "a2": 4.12, "a3": 0.008, "a4": -0.068, "a5": -0.055},
        "noise_std": 1.8,
    },
    {  # Plot 8 — Line only
        "num": 8, "seed": 608, "style": "line",
        "title": "Contour Lines: pH and A:O Ratio Effect on Sm Extraction",
        "x_label": "pH", "y_label": "A:O Ratio",
        "colorbar_label": "Extraction Efficiency (%)",
        "x_range": [1.5, 4.5], "y_range": [0.5, 3.0],
        "z_metric": "extraction_eff", "z_clip": [0, 100],
        "colormap": None, "n_levels": 8,
        "show_colorbar": False, "show_labels": True,
        # Peak near pH=3.0, A:O=1.7
        "coeffs": {"a0": -68.3, "a1": 72.1, "a2": 38.6, "a3": 1.8, "a4": -11.5, "a5": -10.3},
        "noise_std": 1.3,
    },
    {  # Plot 9 — Overlaid
        "num": 9, "seed": 609, "style": "overlaid",
        "title": "RSM Surface: pH and Temperature Optimization for La Extraction",
        "x_label": "pH", "y_label": "Temperature (\u00b0C)",
        "colorbar_label": "Extraction Efficiency (%)",
        "x_range": [1.0, 4.0], "y_range": [25, 65],
        "z_metric": "extraction_eff", "z_clip": [0, 100],
        "colormap": "viridis", "n_levels": 12,
        "show_colorbar": True, "show_labels": True,
        # Peak near pH=2.6, T=47
        "coeffs": {"a0": -178.5, "a1": 95.3, "a2": 5.92, "a3": 0.42, "a4": -17.2, "a5": -0.062},
        "noise_std": 1.5,
    },
    {  # Plot 10 — Overlaid
        "num": 10, "seed": 610, "style": "overlaid",
        "title": "RSM Surface: Extractant Concentration and Contact Time for Ce Recovery",
        "x_label": "Extractant Concentration (M)", "y_label": "Contact Time (min)",
        "colorbar_label": "Recovery (%)",
        "x_range": [0.1, 2.0], "y_range": [5, 60],
        "z_metric": "recovery", "z_clip": [0, 100],
        "colormap": "RdYlGn", "n_levels": 10,
        "show_colorbar": True, "show_labels": True,
        # Peak near conc=1.1, t=35
        "coeffs": {"a0": -42.8, "a1": 82.5, "a2": 3.45, "a3": 0.95, "a4": -35.2, "a5": -0.046},
        "noise_std": 1.6,
    },
]


def apply_common_style(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)


def compute_surface(X, Y, coeffs, rng, noise_std):
    """Compute Z = a0 + a1*X + a2*Y + a3*X*Y + a4*X^2 + a5*Y^2 + noise."""
    c = coeffs
    Z = (c["a0"] + c["a1"] * X + c["a2"] * Y +
         c["a3"] * X * Y + c["a4"] * X**2 + c["a5"] * Y**2)
    noise = rng.normal(0, noise_std, Z.shape)
    Z = Z + noise
    return Z


def generate_plot(cfg, outdir):
    num = cfg["num"]
    rng = np.random.RandomState(cfg["seed"])

    # Create meshgrid
    x = np.linspace(cfg["x_range"][0], cfg["x_range"][1], GRID_RES)
    y = np.linspace(cfg["y_range"][0], cfg["y_range"][1], GRID_RES)
    X, Y = np.meshgrid(x, y)

    # Generate Z surface
    Z = compute_surface(X, Y, cfg["coeffs"], rng, cfg["noise_std"])

    # Clip to realistic range
    z_lo, z_hi = cfg["z_clip"]
    Z = np.clip(Z, z_lo, z_hi)

    # Find optimal point (maximum Z)
    max_idx = np.unravel_index(np.argmax(Z), Z.shape)
    opt_x = round(float(X[max_idx]), 4)
    opt_y = round(float(Y[max_idx]), 4)
    opt_z = round(float(Z[max_idx]), 2)

    # Compute contour levels
    z_min_actual = float(np.min(Z))
    z_max_actual = float(np.max(Z))
    levels = np.linspace(z_min_actual, z_max_actual, cfg["n_levels"] + 2)[1:-1]
    levels = np.round(levels, 1).tolist()

    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    apply_common_style(ax)

    if cfg["style"] == "filled":
        cf = ax.contourf(X, Y, Z, levels=cfg["n_levels"], cmap=cfg["colormap"])
        if cfg["show_colorbar"]:
            cbar = fig.colorbar(cf, ax=ax)
            cbar.set_label(cfg["colorbar_label"], fontsize=COLORBAR_FONTSIZE)
            cbar.ax.tick_params(labelsize=TICK_LABEL_FONTSIZE)
        # Store actual levels used
        levels = [round(float(l), 1) for l in cf.levels]

    elif cfg["style"] == "line":
        cs = ax.contour(X, Y, Z, levels=cfg["n_levels"], colors='black',
                        linewidths=LINE_LW)
        if cfg["show_labels"]:
            ax.clabel(cs, inline=True, fontsize=CLABEL_FONTSIZE, fmt='%.1f')
        levels = [round(float(l), 1) for l in cs.levels]

    elif cfg["style"] == "overlaid":
        cf = ax.contourf(X, Y, Z, levels=cfg["n_levels"], cmap=cfg["colormap"])
        cs = ax.contour(X, Y, Z, levels=cfg["n_levels"], colors='black',
                        linewidths=OVERLAY_LINE_LW)
        if cfg["show_labels"]:
            ax.clabel(cs, inline=True, fontsize=CLABEL_FONTSIZE, fmt='%.1f')
        if cfg["show_colorbar"]:
            cbar = fig.colorbar(cf, ax=ax)
            cbar.set_label(cfg["colorbar_label"], fontsize=COLORBAR_FONTSIZE)
            cbar.ax.tick_params(labelsize=TICK_LABEL_FONTSIZE)
        levels = [round(float(l), 1) for l in cf.levels]

    ax.set_xlabel(cfg["x_label"], fontsize=AXIS_LABEL_FONTSIZE)
    ax.set_ylabel(cfg["y_label"], fontsize=AXIS_LABEL_FONTSIZE)
    ax.set_title(cfg["title"], fontsize=TITLE_FONTSIZE, fontweight='bold')
    ax.tick_params(axis='both', labelsize=TICK_LABEL_FONTSIZE)

    # Save with exact dimensions
    fig.set_size_inches(8, 6)
    # Adjust margins — wider left margin for colorbar plots
    if cfg["show_colorbar"]:
        fig.subplots_adjust(left=0.10, right=0.88, top=0.92, bottom=0.12)
    else:
        fig.subplots_adjust(left=0.12, right=0.95, top=0.92, bottom=0.12)

    png_path = os.path.join(outdir, f"contour{num}.png")
    fig.savefig(png_path, dpi=DPI, facecolor='white')
    plt.close(fig)

    # Write metadata
    write_metadata(cfg, levels, opt_x, opt_y, opt_z, z_min_actual, z_max_actual, outdir)
    print(f"  Generated contour{num}.png and contour{num}.md")


def write_metadata(cfg, levels, opt_x, opt_y, opt_z, z_min, z_max, outdir):
    num = cfg["num"]

    style_map = {"filled": "Filled", "line": "Line only", "overlaid": "Overlaid"}
    style_str = style_map[cfg["style"]]
    cmap_str = cfg["colormap"] if cfg["colormap"] else "None (black lines)"
    labels_str = "Yes" if cfg["show_labels"] else "No"

    json_data = {
        "title": cfg["title"],
        "x_label": cfg["x_label"],
        "y_label": cfg["y_label"],
        "colorbar_label": cfg["colorbar_label"] if cfg["show_colorbar"] else None,
        "x_range": cfg["x_range"],
        "y_range": cfg["y_range"],
        "z_range": [round(z_min, 2), round(z_max, 2)],
        "grid_resolution": GRID_RES,
        "polynomial_coefficients": cfg["coeffs"],
        "contour_levels": levels,
        "optimal_point": {
            "x": opt_x,
            "y": opt_y,
            "z": opt_z,
        },
    }
    json_str = json.dumps(json_data, indent=2)

    notes_parts = []
    if cfg["colormap"]:
        notes_parts.append(f"Colormap: {cfg['colormap']}.")
    else:
        notes_parts.append("Black contour lines, no fill.")
    notes_parts.append(f"Noise std: {cfg['noise_std']}.")
    if cfg["style"] == "overlaid":
        notes_parts.append("Filled contour with black contour lines overlaid (linewidth 0.8).")
    elif cfg["style"] == "line":
        notes_parts.append("Line-only contour with inline labels (linewidth 1.0).")
    elif cfg["style"] == "filled":
        notes_parts.append("Filled contour with colorbar.")
    notes_text = " ".join(notes_parts)

    x_var_desc = f"{cfg['x_label']} ({cfg['x_range'][0]}–{cfg['x_range'][1]})"
    y_var_desc = f"{cfg['y_label']} ({cfg['y_range'][0]}–{cfg['y_range'][1]})"

    md = f"""# Ground Truth: contour{num}

## Plot Configuration

- **Plot type**: Contour map
- **Style**: {style_str}
- **Z metric**: {cfg['colorbar_label']}
- **X variable**: {x_var_desc}
- **Y variable**: {y_var_desc}
- **Grid resolution**: {GRID_RES} \u00d7 {GRID_RES}
- **Number of contour levels**: {cfg['n_levels']}
- **Colormap**: {cmap_str}
- **Contour line labels shown**: {labels_str}
- **numpy seed**: {cfg['seed']}

## Data

```json
{json_str}
```

## Notes

{notes_text}
"""
    filepath = os.path.join(outdir, f"contour{num}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)


def validate(outdir):
    from PIL import Image
    all_ok = True
    for i in range(1, 11):
        png = os.path.join(outdir, f"contour{i}.png")
        md = os.path.join(outdir, f"contour{i}.md")

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
                print(f"  contour{i}.png: size {w}x{h} (expected 2400x1800)")

        if os.path.isfile(md):
            with open(md, 'r', encoding='utf-8') as f:
                content = f.read()
            try:
                json_start = content.index('```json\n') + 8
                json_end = content.index('\n```', json_start)
                parsed = json.loads(content[json_start:json_end])
                # Check required fields
                for field in ("polynomial_coefficients", "contour_levels", "optimal_point"):
                    if field not in parsed:
                        print(f"  contour{i}.md: missing '{field}'")
                        all_ok = False
                # Check optimal point is within grid
                opt = parsed.get("optimal_point", {})
                xr = parsed.get("x_range", [0, 0])
                yr = parsed.get("y_range", [0, 0])
                if opt:
                    if not (xr[0] <= opt["x"] <= xr[1]):
                        print(f"  contour{i}.md: optimal x={opt['x']} outside x_range")
                    if not (yr[0] <= opt["y"] <= yr[1]):
                        print(f"  contour{i}.md: optimal y={opt['y']} outside y_range")
            except (ValueError, json.JSONDecodeError) as e:
                print(f"  contour{i}.md: JSON parse error — {e}")
                all_ok = False

    return all_ok


def main():
    outdir = os.path.dirname(os.path.abspath(__file__))
    print(f"Output directory: {outdir}")
    print(f"Generating 10 contour maps...\n")

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
                   if f.startswith('contour') and (f.endswith('.png') or f.endswith('.md')))
    print(f"\nGenerated files ({len(files)}):")
    for f in files:
        full = os.path.join(outdir, f)
        size = os.path.getsize(full)
        print(f"  {full}  ({size:,} bytes)")


if __name__ == "__main__":
    main()
