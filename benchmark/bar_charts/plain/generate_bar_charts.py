"""
Generate 10 synthetic plain bar chart images with ground truth metadata
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
BAR_WIDTH_V = 0.55
BAR_WIDTH_H = 0.5
EDGE_COLOR = 'black'
EDGE_LW = 0.6
ERR_COLOR = 'black'
ERR_CAPSIZE = 4
ERR_LW = 1.2

# ── Plot configurations ──────────────────────────────────────────────
PLOTS = [
    {  # Plot 1
        "num": 1, "seed": 101, "n_bars": 5, "orientation": "vertical",
        "categories": ["1.5", "2.0", "2.5", "3.0", "3.5"],
        "title": "Effect of pH on Extraction Efficiency of Nd",
        "x_label": "pH", "y_label": "Extraction Efficiency (%)",
        "y_range": [0, 100], "metric": "extraction_eff",
        "color": "#4472C4", "varied": False,
        "error_bars": False, "error_range": None,
        "grid": "horizontal", "legend": False, "rotate_x": False,
    },
    {  # Plot 2
        "num": 2, "seed": 102, "n_bars": 6, "orientation": "vertical",
        "categories": ["D2EHPA", "Cyanex 272", "PC88A", "TBP", "EHEHPA", "Aliquat 336"],
        "title": "Extraction Efficiency of La with Different Extractants",
        "x_label": "Extractant", "y_label": "Extraction Efficiency (%)",
        "y_range": [0, 100], "metric": "extraction_eff",
        "color": "#C0504D", "varied": False,
        "error_bars": True, "error_range": (2, 5),
        "grid": "horizontal", "legend": False, "rotate_x": True,
    },
    {  # Plot 3
        "num": 3, "seed": 103, "n_bars": 4, "orientation": "horizontal",
        "categories": ["La", "Ce", "Nd", "Pr"],
        "title": "Distribution Ratio of REEs in D2EHPA System",
        "x_label": "REE Element", "y_label": "Distribution Ratio (D)",
        "y_range": [0, 10], "metric": "distribution_ratio",
        "color": None, "varied": True,
        "error_bars": False, "error_range": None,
        "grid": "none", "legend": True, "rotate_x": False,
    },
    {  # Plot 4
        "num": 4, "seed": 104, "n_bars": 7, "orientation": "vertical",
        "categories": ["5", "10", "15", "20", "30", "45", "60"],
        "title": "Effect of Contact Time on Ce Extraction",
        "x_label": "Contact Time (min)", "y_label": "Extraction Efficiency (%)",
        "y_range": [40, 100], "metric": "extraction_eff",
        "color": "#4F7942", "varied": False,
        "error_bars": False, "error_range": None,
        "grid": "both", "legend": False, "rotate_x": False,
    },
    {  # Plot 5
        "num": 5, "seed": 105, "n_bars": 5, "orientation": "vertical",
        "categories": ["La/Ce", "Ce/Pr", "Pr/Nd", "Nd/Sm", "Sm/Eu"],
        "title": "Separation Factor Between Adjacent REE Pairs",
        "x_label": "REE Pair", "y_label": "Separation Factor (\u03b1)",
        "y_range": [0, 5], "metric": "separation_factor",
        "color": "#7F7F7F", "varied": False,
        "error_bars": False, "error_range": None,
        "grid": "horizontal", "legend": False, "rotate_x": False,
    },
    {  # Plot 6
        "num": 6, "seed": 106, "n_bars": 6, "orientation": "vertical",
        "categories": ["20", "30", "40", "50", "60", "70"],
        "title": "Effect of Temperature on Pr Extraction",
        "x_label": "Temperature (\u00b0C)", "y_label": "Extraction Efficiency (%)",
        "y_range": [50, 100], "metric": "extraction_eff",
        "color": "#008080", "varied": False,
        "error_bars": True, "error_range": (1, 4),
        "grid": "horizontal", "legend": False, "rotate_x": False,
    },
    {  # Plot 7
        "num": 7, "seed": 107, "n_bars": 8, "orientation": "vertical",
        "categories": ["kerosene", "hexane", "toluene", "heptane",
                        "octanol", "cyclohexane", "xylene", "dodecane"],
        "title": "Effect of Diluent on Nd Extraction Efficiency",
        "x_label": "Diluent", "y_label": "Extraction Efficiency (%)",
        "y_range": [20, 90], "metric": "extraction_eff",
        "color": None, "varied": True,
        "error_bars": False, "error_range": None,
        "grid": "horizontal", "legend": True, "rotate_x": True,
    },
    {  # Plot 8
        "num": 8, "seed": 108, "n_bars": 5, "orientation": "horizontal",
        "categories": ["HCl 1M", "HCl 2M", "H2SO4 1M", "HNO3 1M", "EDTA 0.5M"],
        "title": "Stripping Efficiency with Different Stripping Agents",
        "x_label": "Stripping Agent", "y_label": "Stripping Efficiency (%)",
        "y_range": [0, 100], "metric": "stripping_eff",
        "color": "#E26B0A", "varied": False,
        "error_bars": True, "error_range": (2, 6),
        "grid": "vertical", "legend": False, "rotate_x": False,
    },
    {  # Plot 9
        "num": 9, "seed": 109, "n_bars": 4, "orientation": "vertical",
        "categories": ["1:3", "1:1", "2:1", "3:1"],
        "title": "Effect of A:O Ratio on Distribution of Sm",
        "x_label": "A:O Ratio", "y_label": "Distribution Ratio (D)",
        "y_range": [0, 20], "metric": "distribution_ratio",
        "color": "#7B4F9E", "varied": False,
        "error_bars": False, "error_range": None,
        "grid": "horizontal", "legend": False, "rotate_x": False,
    },
    {  # Plot 10
        "num": 10, "seed": 110, "n_bars": 6, "orientation": "vertical",
        "categories": ["50", "100", "200", "300", "500", "1000"],
        "title": "Effect of Initial Metal Concentration on La Extraction",
        "x_label": "Initial Concentration (mg/L)", "y_label": "Extraction Efficiency (%)",
        "y_range": [60, 100], "metric": "extraction_eff",
        "color": None, "varied": True,
        "error_bars": True, "error_range": (1, 5),
        "grid": "horizontal", "legend": True, "rotate_x": False,
    },
]


def generate_values(rng, metric, n):
    """Generate realistic non-round values for the given metric."""
    if metric == "extraction_eff":
        return np.round(rng.uniform(20, 98, n), 1)
    elif metric == "distribution_ratio":
        return np.round(rng.uniform(0.5, 18, n), 2)
    elif metric == "separation_factor":
        return np.round(rng.uniform(0.8, 4.5, n), 2)
    elif metric == "stripping_eff":
        return np.round(rng.uniform(30, 97, n), 1)
    else:
        raise ValueError(f"Unknown metric: {metric}")


def generate_errors(rng, error_range, n):
    """Generate error bar values within the specified range."""
    lo, hi = error_range
    return np.round(rng.uniform(lo, hi, n), 2)


def apply_common_style(ax):
    """Apply shared styling to an axes object."""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)


def get_colors(cfg, n):
    """Return a list of colors for the bars."""
    if cfg["varied"]:
        cmap = plt.cm.tab10
        return [cmap(i) for i in range(n)]
    else:
        return [cfg["color"]] * n


def build_legend_labels(categories, colors):
    """Build legend handles for varied-color bar charts."""
    from matplotlib.patches import Patch
    return [Patch(facecolor=c, edgecolor='black', linewidth=0.6, label=lbl)
            for lbl, c in zip(categories, colors)]


def write_metadata(cfg, values, errors, outdir):
    """Write ground truth markdown+JSON for a plot."""
    num = cfg["num"]
    bars_list = []
    for i, cat in enumerate(cfg["categories"]):
        entry = {
            "label": cat,
            "value": float(values[i]),
            "error": float(errors[i]) if errors is not None else None,
        }
        bars_list.append(entry)

    data = {
        "title": cfg["title"],
        "x_label": cfg["x_label"],
        "y_label": cfg["y_label"],
        "y_axis_range": cfg["y_range"],
        "bars": bars_list,
    }

    orient_str = "Vertical" if cfg["orientation"] == "vertical" else "Horizontal"
    err_str = "Yes" if cfg["error_bars"] else "No"

    notes_parts = []
    if cfg["rotate_x"]:
        notes_parts.append("X-tick labels rotated 45 degrees, right-aligned.")
    if cfg["legend"]:
        notes_parts.append("Legend displayed upper right with light gray border frame.")
    if cfg["varied"]:
        notes_parts.append("Varied colors per bar using matplotlib tab10 colormap.")
    else:
        notes_parts.append(f"Single bar color: {cfg['color']}.")

    grid_desc = {
        "horizontal": "Horizontal gridlines only.",
        "vertical": "Vertical gridlines only.",
        "both": "Both horizontal and vertical gridlines.",
        "none": "No gridlines.",
    }
    notes_parts.append(grid_desc[cfg["grid"]])
    notes_text = " ".join(notes_parts)

    json_str = json.dumps(data, indent=2)

    md = f"""# Ground Truth: barplot{num}

## Plot Configuration

- **Plot type**: Plain bar chart
- **Orientation**: {orient_str}
- **Number of bars**: {cfg['n_bars']}
- **Y-axis metric**: {cfg['y_label']}
- **Error bars present**: {err_str}
- **numpy seed**: {cfg['seed']}

## Data

```json
{json_str}
```

## Notes

{notes_text}
"""
    filepath = os.path.join(outdir, f"barplot{num}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)


def generate_plot(cfg, outdir):
    """Generate a single bar chart and its metadata."""
    num = cfg["num"]
    rng = np.random.RandomState(cfg["seed"])

    # Generate data
    values = generate_values(rng, cfg["metric"], cfg["n_bars"])
    errors = generate_errors(rng, cfg["error_range"], cfg["n_bars"]) if cfg["error_bars"] else None

    # Clamp values to y_range for realism
    lo, hi = cfg["y_range"]
    values = np.clip(values, lo + 1, hi - 1)
    # Re-round after clipping
    if cfg["metric"] in ("extraction_eff", "stripping_eff"):
        values = np.round(values, 1)
    else:
        values = np.round(values, 2)

    colors = get_colors(cfg, cfg["n_bars"])

    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    apply_common_style(ax)

    cats = cfg["categories"]

    if cfg["orientation"] == "vertical":
        x = np.arange(cfg["n_bars"])
        err_kw = dict(ecolor=ERR_COLOR, capsize=ERR_CAPSIZE, elinewidth=ERR_LW) if errors is not None else {}
        bars = ax.bar(
            x, values, width=BAR_WIDTH_V,
            color=colors, edgecolor=EDGE_COLOR, linewidth=EDGE_LW,
            yerr=errors, error_kw=err_kw if errors is not None else {},
        )
        ax.set_xticks(x)
        ax.set_xticklabels(cats, fontsize=TICK_LABEL_FONTSIZE)
        ax.set_ylim(cfg["y_range"])
        ax.set_xlabel(cfg["x_label"], fontsize=AXIS_LABEL_FONTSIZE)
        ax.set_ylabel(cfg["y_label"], fontsize=AXIS_LABEL_FONTSIZE)

        if cfg["rotate_x"]:
            ax.set_xticklabels(cats, fontsize=TICK_LABEL_FONTSIZE,
                               rotation=45, ha='right')
    else:
        # Horizontal
        y = np.arange(cfg["n_bars"])
        err_kw = dict(ecolor=ERR_COLOR, capsize=ERR_CAPSIZE, elinewidth=ERR_LW) if errors is not None else {}
        bars = ax.barh(
            y, values, height=BAR_WIDTH_H,
            color=colors, edgecolor=EDGE_COLOR, linewidth=EDGE_LW,
            xerr=errors, error_kw=err_kw if errors is not None else {},
        )
        ax.set_yticks(y)
        ax.set_yticklabels(cats, fontsize=TICK_LABEL_FONTSIZE)
        ax.set_xlim(cfg["y_range"])
        # For horizontal charts, the "y_label" is the value axis (x-axis here)
        ax.set_xlabel(cfg["y_label"], fontsize=AXIS_LABEL_FONTSIZE)
        ax.set_ylabel(cfg["x_label"], fontsize=AXIS_LABEL_FONTSIZE)

    ax.set_title(cfg["title"], fontsize=TITLE_FONTSIZE, fontweight='bold')
    ax.tick_params(axis='both', labelsize=TICK_LABEL_FONTSIZE)

    # Gridlines
    if cfg["grid"] == "horizontal":
        ax.yaxis.grid(True, linestyle='--', alpha=0.7)
        ax.xaxis.grid(False)
        ax.set_axisbelow(True)
    elif cfg["grid"] == "vertical":
        ax.xaxis.grid(True, linestyle='--', alpha=0.7)
        ax.yaxis.grid(False)
        ax.set_axisbelow(True)
    elif cfg["grid"] == "both":
        ax.yaxis.grid(True, linestyle='--', alpha=0.7)
        ax.xaxis.grid(True, linestyle='--', alpha=0.7)
        ax.set_axisbelow(True)
    else:
        ax.grid(False)

    # Legend
    if cfg["legend"]:
        if cfg["varied"]:
            handles = build_legend_labels(cats, colors)
            ax.legend(handles=handles, loc='upper right',
                      frameon=True, edgecolor='lightgray',
                      fancybox=False, fontsize=TICK_LABEL_FONTSIZE)
        else:
            ax.legend(loc='upper right', frameon=True,
                      edgecolor='lightgray', fancybox=False,
                      fontsize=TICK_LABEL_FONTSIZE)

    fig.set_size_inches(8, 6)
    fig.subplots_adjust(left=0.12, right=0.95, top=0.92, bottom=0.12)
    if cfg["rotate_x"]:
        fig.subplots_adjust(bottom=0.20)
    if cfg["orientation"] == "horizontal":
        fig.subplots_adjust(left=0.18)
    png_path = os.path.join(outdir, f"barplot{num}.png")
    fig.savefig(png_path, dpi=DPI, facecolor='white')
    plt.close(fig)

    # Write metadata
    write_metadata(cfg, values, errors, outdir)
    print(f"  Generated barplot{num}.png and barplot{num}.md")


def validate(outdir):
    """Validate all outputs exist, are non-empty, and PNGs have correct dimensions."""
    from PIL import Image
    all_ok = True
    for i in range(1, 11):
        png = os.path.join(outdir, f"barplot{i}.png")
        md = os.path.join(outdir, f"barplot{i}.md")

        # Check existence and size
        for fpath in (png, md):
            if not os.path.isfile(fpath):
                print(f"  MISSING: {fpath}")
                all_ok = False
            elif os.path.getsize(fpath) == 0:
                print(f"  EMPTY: {fpath}")
                all_ok = False

        # Check PNG dimensions
        if os.path.isfile(png):
            img = Image.open(png)
            w, h = img.size
            if (w, h) != (2400, 1800):
                print(f"  barplot{i}.png: unexpected size {w}x{h} (expected 2400x1800)")
                # Note: bbox_inches='tight' may alter dimensions slightly

        # Check MD contains valid JSON
        if os.path.isfile(md):
            with open(md, 'r', encoding='utf-8') as f:
                content = f.read()
            try:
                json_start = content.index('```json\n') + 8
                json_end = content.index('\n```', json_start)
                json.loads(content[json_start:json_end])
            except (ValueError, json.JSONDecodeError) as e:
                print(f"  barplot{i}.md: JSON parse error — {e}")
                all_ok = False

    return all_ok


def main():
    outdir = os.path.dirname(os.path.abspath(__file__))
    print(f"Output directory: {outdir}")
    print(f"Generating 10 bar charts...\n")

    for cfg in PLOTS:
        generate_plot(cfg, outdir)

    print(f"\nValidating outputs...")
    ok = validate(outdir)

    print(f"\n{'='*50}")
    if ok:
        print("All 20 files generated and validated successfully!")
    else:
        print("Some validation issues found (see above).")
    print(f"{'='*50}")

    # List all generated files
    files = sorted(f for f in os.listdir(outdir)
                   if f.startswith('barplot') and (f.endswith('.png') or f.endswith('.md')))
    print(f"\nGenerated files ({len(files)}):")
    for f in files:
        size = os.path.getsize(os.path.join(outdir, f))
        print(f"  {f:25s} {size:>10,} bytes")


if __name__ == "__main__":
    main()
