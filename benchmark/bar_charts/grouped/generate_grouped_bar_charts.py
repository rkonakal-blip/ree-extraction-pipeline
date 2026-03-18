"""
Generate 10 synthetic grouped bar chart images with ground truth metadata
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
EDGE_COLOR = 'black'
EDGE_LW = 0.6
ERR_COLOR = 'black'
ERR_CAPSIZE = 4
ERR_LW = 1.2

# ── Plot configurations ──────────────────────────────────────────────
PLOTS = [
    {  # Plot 1
        "num": 1, "seed": 301,
        "n_groups": 4, "n_series": 3, "orientation": "vertical",
        "categories": ["1.5", "2.0", "2.5", "3.0"],
        "series_names": ["D2EHPA", "Cyanex 272", "PC88A"],
        "title": "Extraction Efficiency of REEs with Different Extractants vs pH",
        "x_label": "pH", "y_label": "Extraction Efficiency (%)",
        "y_range": [0, 100], "metric": "extraction_eff",
        "error_bars": False, "error_range": None,
        "colormap": "tab10", "n_colors": 3,
        "grid": "horizontal", "rotate_x": False,
    },
    {  # Plot 2
        "num": 2, "seed": 302,
        "n_groups": 5, "n_series": 2, "orientation": "vertical",
        "categories": ["20", "30", "40", "50", "60"],
        "series_names": ["La", "Nd"],
        "title": "Effect of Temperature on La and Nd Extraction",
        "x_label": "Temperature (\u00b0C)", "y_label": "Extraction Efficiency (%)",
        "y_range": [0, 100], "metric": "extraction_eff",
        "error_bars": True, "error_range": (2, 5),
        "colormap": "Set1", "n_colors": 2,
        "grid": "horizontal", "rotate_x": False,
    },
    {  # Plot 3
        "num": 3, "seed": 303,
        "n_groups": 3, "n_series": 4, "orientation": "vertical",
        "categories": ["La", "Ce", "Nd"],
        "series_names": ["0.1M extractant", "0.5M extractant", "1.0M extractant", "2.0M extractant"],
        "title": "Distribution Ratio of REEs at Different Extractant Concentrations",
        "x_label": "REE Element", "y_label": "Distribution Ratio (D)",
        "y_range": [0, 15], "metric": "distribution_ratio_15",
        "error_bars": False, "error_range": None,
        "colormap": "tab10", "n_colors": 4,
        "grid": "horizontal", "rotate_x": False,
    },
    {  # Plot 4
        "num": 4, "seed": 304,
        "n_groups": 4, "n_series": 3, "orientation": "horizontal",
        "categories": ["HCl 1M", "HCl 2M", "H2SO4", "HNO3"],
        "series_names": ["La", "Ce", "Nd"],
        "title": "Stripping Efficiency of REEs with Different Stripping Agents",
        "x_label": "Stripping Agent", "y_label": "Stripping Efficiency (%)",
        "y_range": [0, 100], "metric": "stripping_eff",
        "error_bars": False, "error_range": None,
        "colormap": "Set2", "n_colors": 3,
        "grid": "vertical", "rotate_x": False,
    },
    {  # Plot 5
        "num": 5, "seed": 305,
        "n_groups": 5, "n_series": 2, "orientation": "vertical",
        "categories": ["10", "20", "30", "45", "60"],
        "series_names": ["D2EHPA", "PC88A"],
        "title": "Extraction Kinetics of D2EHPA vs PC88A",
        "x_label": "Contact Time (min)", "y_label": "Extraction Efficiency (%)",
        "y_range": [40, 100], "metric": "extraction_eff",
        "error_bars": True, "error_range": (1, 4),
        "colormap": "Paired", "n_colors": 2,
        "grid": "horizontal", "rotate_x": False,
    },
    {  # Plot 6
        "num": 6, "seed": 306,
        "n_groups": 4, "n_series": 4, "orientation": "vertical",
        "categories": ["La/Ce", "Ce/Pr", "Pr/Nd", "Nd/Sm"],
        "series_names": ["0.1M D2EHPA", "0.5M D2EHPA", "1.0M D2EHPA", "2.0M D2EHPA"],
        "title": "Separation Factor for Adjacent REE Pairs at Different Extractant Concentrations",
        "x_label": "REE Pair", "y_label": "Separation Factor (\u03b1)",
        "y_range": [0, 5], "metric": "separation_factor",
        "error_bars": False, "error_range": None,
        "colormap": "tab10", "n_colors": 4,
        "grid": "horizontal", "rotate_x": False,
    },
    {  # Plot 7
        "num": 7, "seed": 307,
        "n_groups": 6, "n_series": 3, "orientation": "vertical",
        "categories": ["50", "100", "200", "300", "500", "1000"],
        "series_names": ["D2EHPA", "Cyanex 272", "PC88A"],
        "title": "Effect of Initial Concentration on REE Extraction",
        "x_label": "Initial Concentration (mg/L)", "y_label": "Extraction Efficiency (%)",
        "y_range": [0, 100], "metric": "extraction_eff",
        "error_bars": True, "error_range": (2, 6),
        "colormap": "Set1", "n_colors": 3,
        "grid": "horizontal", "rotate_x": False,
    },
    {  # Plot 8
        "num": 8, "seed": 308,
        "n_groups": 3, "n_series": 5, "orientation": "vertical",
        "categories": ["Kerosene", "Hexane", "Toluene"],
        "series_names": ["La", "Ce", "Nd", "Pr", "Sm"],
        "title": "Recovery of REEs with Different Diluents",
        "x_label": "Diluent", "y_label": "Recovery (%)",
        "y_range": [50, 100], "metric": "recovery",
        "error_bars": False, "error_range": None,
        "colormap": "tab20", "n_colors": 5,
        "grid": "horizontal", "rotate_x": False,
    },
    {  # Plot 9
        "num": 9, "seed": 309,
        "n_groups": 5, "n_series": 2, "orientation": "horizontal",
        "categories": ["1:3", "1:2", "1:1", "2:1", "3:1"],
        "series_names": ["La", "Nd"],
        "title": "Distribution Ratio of La and Nd at Different A:O Ratios",
        "x_label": "A:O Ratio", "y_label": "Distribution Ratio (D)",
        "y_range": [0, 20], "metric": "distribution_ratio",
        "error_bars": False, "error_range": None,
        "colormap": "Set2", "n_colors": 2,
        "grid": "vertical", "rotate_x": False,
    },
    {  # Plot 10
        "num": 10, "seed": 310,
        "n_groups": 4, "n_series": 3, "orientation": "vertical",
        "categories": ["0.1", "0.5", "1.0", "2.0"],
        "series_names": ["D2EHPA", "Cyanex 272", "PC88A"],
        "title": "Extraction Efficiency at Different Reagent Concentrations",
        "x_label": "Reagent Concentration (M)", "y_label": "Extraction Efficiency (%)",
        "y_range": [0, 100], "metric": "extraction_eff",
        "error_bars": True, "error_range": (1, 5),
        "colormap": "tab10", "n_colors": 3,
        "grid": "horizontal", "rotate_x": False,
    },
]


def generate_values(rng, metric, n):
    """Generate realistic non-round values for the given metric."""
    if metric == "extraction_eff":
        return np.round(rng.uniform(20, 98, n), 1)
    elif metric == "distribution_ratio":
        return np.round(rng.uniform(0.5, 18, n), 2)
    elif metric == "distribution_ratio_15":
        return np.round(rng.uniform(0.5, 14, n), 2)
    elif metric == "separation_factor":
        return np.round(rng.uniform(0.8, 4.5, n), 2)
    elif metric == "stripping_eff":
        return np.round(rng.uniform(30, 97, n), 1)
    elif metric == "recovery":
        return np.round(rng.uniform(50, 98, n), 1)
    else:
        raise ValueError(f"Unknown metric: {metric}")


def generate_errors(rng, error_range, n):
    """Generate error bar values within the specified range."""
    lo, hi = error_range
    return np.round(rng.uniform(lo, hi, n), 2)


def get_colors(colormap_name, n_colors):
    """Get colors from the specified colormap."""
    cmap = matplotlib.colormaps[colormap_name]
    return [cmap(i) for i in range(n_colors)]


def apply_common_style(ax):
    """Apply shared styling to axes."""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)


def write_metadata(cfg, data, errors, outdir):
    """Write ground truth markdown+JSON for a grouped bar plot."""
    num = cfg["num"]
    orient_str = "Vertical" if cfg["orientation"] == "vertical" else "Horizontal"
    err_str = "Yes" if cfg["error_bars"] else "No"

    groups_list = []
    for g in range(cfg["n_groups"]):
        bars = []
        for s in range(cfg["n_series"]):
            bars.append({
                "series": cfg["series_names"][s],
                "value": float(data[g, s]),
                "error": float(errors[g, s]) if errors is not None else None,
            })
        groups_list.append({
            "label": cfg["categories"][g],
            "bars": bars,
        })

    json_data = {
        "title": cfg["title"],
        "x_label": cfg["x_label"],
        "y_label": cfg["y_label"],
        "y_axis_range": cfg["y_range"],
        "series": cfg["series_names"],
        "groups": groups_list,
    }

    json_str = json.dumps(json_data, indent=2)

    bar_width = round(0.8 / cfg["n_series"], 4)
    notes_parts = []
    if cfg["rotate_x"]:
        notes_parts.append("X-tick labels rotated 45 degrees, right-aligned.")
    notes_parts.append(f"Color scheme: {cfg['colormap']} with {cfg['n_colors']} colors.")
    notes_parts.append(f"Bar width per series: {bar_width}.")
    grid_desc = {
        "horizontal": "Horizontal gridlines only.",
        "vertical": "Vertical gridlines only.",
    }
    notes_parts.append(grid_desc[cfg["grid"]])
    notes_parts.append("Legend displayed upper right with light gray border frame.")
    notes_text = " ".join(notes_parts)

    md = f"""# Ground Truth: grouped_barplot{num}

## Plot Configuration

- **Plot type**: Grouped bar chart
- **Orientation**: {orient_str}
- **Number of groups**: {cfg['n_groups']}
- **Number of series**: {cfg['n_series']}
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
    filepath = os.path.join(outdir, f"grouped_barplot{num}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)


def generate_plot(cfg, outdir):
    """Generate a single grouped bar chart and its metadata."""
    num = cfg["num"]
    rng = np.random.RandomState(cfg["seed"])

    n_groups = cfg["n_groups"]
    n_series = cfg["n_series"]

    # Generate data: shape (n_groups, n_series)
    data = np.zeros((n_groups, n_series))
    for s in range(n_series):
        data[:, s] = generate_values(rng, cfg["metric"], n_groups)

    # Clamp to y_range
    lo, hi = cfg["y_range"]
    data = np.clip(data, lo + 1, hi - 1)
    if cfg["metric"] in ("extraction_eff", "stripping_eff", "recovery"):
        data = np.round(data, 1)
    else:
        data = np.round(data, 2)

    # Generate errors
    errors = None
    if cfg["error_bars"]:
        errors = np.zeros((n_groups, n_series))
        for s in range(n_series):
            errors[:, s] = generate_errors(rng, cfg["error_range"], n_groups)

    colors = get_colors(cfg["colormap"], cfg["n_colors"])
    bar_width = 0.8 / n_series

    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    apply_common_style(ax)

    if cfg["orientation"] == "vertical":
        x = np.arange(n_groups)
        for s in range(n_series):
            offset = (s - (n_series - 1) / 2.0) * bar_width
            err_kw = {}
            yerr = None
            if errors is not None:
                yerr = errors[:, s]
                err_kw = dict(ecolor=ERR_COLOR, capsize=ERR_CAPSIZE, elinewidth=ERR_LW)
            ax.bar(x + offset, data[:, s], width=bar_width,
                   color=colors[s], edgecolor=EDGE_COLOR, linewidth=EDGE_LW,
                   label=cfg["series_names"][s],
                   yerr=yerr, error_kw=err_kw)

        ax.set_xticks(x)
        if cfg["rotate_x"]:
            ax.set_xticklabels(cfg["categories"], fontsize=TICK_LABEL_FONTSIZE,
                               rotation=45, ha='right')
        else:
            ax.set_xticklabels(cfg["categories"], fontsize=TICK_LABEL_FONTSIZE)
        ax.set_ylim(cfg["y_range"])
        ax.set_xlabel(cfg["x_label"], fontsize=AXIS_LABEL_FONTSIZE)
        ax.set_ylabel(cfg["y_label"], fontsize=AXIS_LABEL_FONTSIZE)
    else:
        # Horizontal
        y = np.arange(n_groups)
        for s in range(n_series):
            offset = (s - (n_series - 1) / 2.0) * bar_width
            err_kw = {}
            xerr = None
            if errors is not None:
                xerr = errors[:, s]
                err_kw = dict(ecolor=ERR_COLOR, capsize=ERR_CAPSIZE, elinewidth=ERR_LW)
            ax.barh(y + offset, data[:, s], height=bar_width,
                    color=colors[s], edgecolor=EDGE_COLOR, linewidth=EDGE_LW,
                    label=cfg["series_names"][s],
                    xerr=xerr, error_kw=err_kw)

        ax.set_yticks(y)
        ax.set_yticklabels(cfg["categories"], fontsize=TICK_LABEL_FONTSIZE)
        ax.set_xlim(cfg["y_range"])
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

    # Legend
    ax.legend(loc='upper right', frameon=True, edgecolor='lightgray',
              fancybox=False, fontsize=TICK_LABEL_FONTSIZE)

    # Save with exact dimensions
    fig.set_size_inches(8, 6)
    fig.subplots_adjust(left=0.12, right=0.95, top=0.92, bottom=0.12)
    if cfg["rotate_x"]:
        fig.subplots_adjust(bottom=0.20)
    if cfg["orientation"] == "horizontal":
        fig.subplots_adjust(left=0.18)

    png_path = os.path.join(outdir, f"grouped_barplot{num}.png")
    fig.savefig(png_path, dpi=DPI, facecolor='white')
    plt.close(fig)

    # Write metadata
    write_metadata(cfg, data, errors, outdir)
    print(f"  Generated grouped_barplot{num}.png and grouped_barplot{num}.md")


def validate(outdir):
    """Validate all outputs."""
    from PIL import Image
    all_ok = True
    for i in range(1, 11):
        png = os.path.join(outdir, f"grouped_barplot{i}.png")
        md = os.path.join(outdir, f"grouped_barplot{i}.md")

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
                print(f"  grouped_barplot{i}.png: size {w}x{h} (expected 2400x1800)")

        # Check MD contains valid JSON
        if os.path.isfile(md):
            with open(md, 'r', encoding='utf-8') as f:
                content = f.read()
            try:
                json_start = content.index('```json\n') + 8
                json_end = content.index('\n```', json_start)
                json.loads(content[json_start:json_end])
            except (ValueError, json.JSONDecodeError) as e:
                print(f"  grouped_barplot{i}.md: JSON parse error — {e}")
                all_ok = False

    return all_ok


def main():
    outdir = os.path.dirname(os.path.abspath(__file__))
    print(f"Output directory: {outdir}")
    print(f"Generating 10 grouped bar charts...\n")

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

    # List all generated files with full paths
    files = sorted(f for f in os.listdir(outdir)
                   if f.startswith('grouped_barplot') and (f.endswith('.png') or f.endswith('.md')))
    print(f"\nGenerated files ({len(files)}):")
    for f in files:
        full = os.path.join(outdir, f)
        size = os.path.getsize(full)
        print(f"  {full}  ({size:,} bytes)")


if __name__ == "__main__":
    main()
