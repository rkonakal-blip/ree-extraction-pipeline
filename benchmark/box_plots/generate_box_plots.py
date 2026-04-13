"""
Generate 10 synthetic box plot images with ground truth metadata
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
BOX_WIDTH_SINGLE = 0.5
BOX_WIDTH_MULTI = 0.3
MEDIAN_LW = 2.0
WHISKER_LW = 1.2
EDGE_LW = 0.6
FLIER_SIZE = 5

# ── Color references ──────────────────────────────────────────────────
COLORS = {
    "steel_blue": "#4472C4",
    "coral_red": "#C0504D",
    "forest_green": "#4F7942",
    "medium_purple": "#7B4F9E",
    "teal": "#008080",
    "dark_orange": "#E26B0A",
}

# ── Metric generation parameters ─────────────────────────────────────
METRIC_PARAMS = {
    "extraction_eff": {"mean_range": (40, 90), "std_range": (3, 10)},
    "distribution_ratio": {"mean_range": (1, 15), "std_range": (0.2, 2.0)},
    "stripping_eff": {"mean_range": (50, 95), "std_range": (3, 8)},
    "separation_factor": {"mean_range": (0.8, 4.0), "std_range": (0.1, 0.5)},
    "recovery": {"mean_range": (50, 95), "std_range": (3, 10)},
}

# ── Plot configurations ──────────────────────────────────────────────
PLOTS = [
    {  # Plot 1
        "num": 1, "seed": 501,
        "n_groups": 4, "n_series": 1, "orientation": "vertical",
        "categories": ["1.5", "2.0", "2.5", "3.0"],
        "series_names": None,
        "title": "Distribution of Nd Extraction Efficiency Across pH Levels",
        "x_label": "pH", "y_label": "Extraction Efficiency (%)",
        "metric": "extraction_eff",
        "outliers": True, "notched": False,
        "color_type": "single", "color_value": "steel_blue",
        "colormap": None, "n_colors": None,
        "grid": "horizontal", "legend": False, "rotate_x": False,
    },
    {  # Plot 2
        "num": 2, "seed": 502,
        "n_groups": 5, "n_series": 1, "orientation": "vertical",
        "categories": ["20", "30", "40", "50", "60"],
        "series_names": None,
        "title": "Effect of Temperature on La Extraction Efficiency",
        "x_label": "Temperature (\u00b0C)", "y_label": "Extraction Efficiency (%)",
        "metric": "extraction_eff",
        "outliers": True, "notched": False,
        "color_type": "single", "color_value": "coral_red",
        "colormap": None, "n_colors": None,
        "grid": "horizontal", "legend": False, "rotate_x": False,
    },
    {  # Plot 3
        "num": 3, "seed": 503,
        "n_groups": 3, "n_series": 2, "orientation": "vertical",
        "categories": ["La", "Ce", "Nd"],
        "series_names": ["D2EHPA", "PC88A"],
        "title": "Distribution Ratio Variability of REEs by Extractant",
        "x_label": "REE Element", "y_label": "Distribution Ratio (D)",
        "metric": "distribution_ratio",
        "outliers": False, "notched": False,
        "color_type": "colormap", "color_value": None,
        "colormap": "tab10", "n_colors": 2,
        "grid": "horizontal", "legend": True, "rotate_x": False,
    },
    {  # Plot 4
        "num": 4, "seed": 504,
        "n_groups": 4, "n_series": 1, "orientation": "horizontal",
        "categories": ["HCl 1M", "HCl 2M", "H2SO4", "HNO3"],
        "series_names": None,
        "title": "Stripping Efficiency Distribution by Stripping Agent",
        "x_label": "Stripping Agent", "y_label": "Stripping Efficiency (%)",
        "metric": "stripping_eff",
        "outliers": True, "notched": False,
        "color_type": "single", "color_value": "forest_green",
        "colormap": None, "n_colors": None,
        "grid": "vertical", "legend": False, "rotate_x": False,
    },
    {  # Plot 5
        "num": 5, "seed": 505,
        "n_groups": 5, "n_series": 1, "orientation": "vertical",
        "categories": ["10", "20", "30", "45", "60"],
        "series_names": None,
        "title": "Extraction Efficiency Distribution vs Contact Time",
        "x_label": "Contact Time (min)", "y_label": "Extraction Efficiency (%)",
        "metric": "extraction_eff",
        "outliers": False, "notched": True,
        "color_type": "single", "color_value": "medium_purple",
        "colormap": None, "n_colors": None,
        "grid": "horizontal", "legend": False, "rotate_x": False,
    },
    {  # Plot 6
        "num": 6, "seed": 506,
        "n_groups": 4, "n_series": 2, "orientation": "vertical",
        "categories": ["D2EHPA", "Cyanex 272", "PC88A", "TBP"],
        "series_names": ["La", "Nd"],
        "title": "REE Recovery Distribution Across Extractants",
        "x_label": "Extractant", "y_label": "Recovery (%)",
        "metric": "recovery",
        "outliers": True, "notched": False,
        "color_type": "colormap", "color_value": None,
        "colormap": "Set1", "n_colors": 2,
        "grid": "horizontal", "legend": True, "rotate_x": True,
    },
    {  # Plot 7
        "num": 7, "seed": 507,
        "n_groups": 3, "n_series": 1, "orientation": "vertical",
        "categories": ["La/Ce", "Ce/Pr", "Pr/Nd"],
        "series_names": None,
        "title": "Separation Factor Variability for Adjacent REE Pairs",
        "x_label": "REE Pair", "y_label": "Separation Factor (\u03b1)",
        "metric": "separation_factor",
        "outliers": True, "notched": False,
        "color_type": "single", "color_value": "teal",
        "colormap": None, "n_colors": None,
        "grid": "horizontal", "legend": False, "rotate_x": False,
    },
    {  # Plot 8
        "num": 8, "seed": 508,
        "n_groups": 4, "n_series": 3, "orientation": "vertical",
        "categories": ["1:3", "1:1", "2:1", "3:1"],
        "series_names": ["D2EHPA", "Cyanex 272", "PC88A"],
        "title": "Extraction Efficiency Distribution at Different A:O Ratios",
        "x_label": "A:O Ratio", "y_label": "Extraction Efficiency (%)",
        "metric": "extraction_eff",
        "outliers": False, "notched": False,
        "color_type": "colormap", "color_value": None,
        "colormap": "tab10", "n_colors": 3,
        "grid": "horizontal", "legend": True, "rotate_x": False,
    },
    {  # Plot 9
        "num": 9, "seed": 509,
        "n_groups": 5, "n_series": 1, "orientation": "horizontal",
        "categories": ["50", "100", "200", "500", "1000"],
        "series_names": None,
        "title": "Distribution Ratio vs Initial Metal Concentration",
        "x_label": "Initial Concentration (mg/L)", "y_label": "Distribution Ratio (D)",
        "metric": "distribution_ratio",
        "outliers": True, "notched": False,
        "color_type": "single", "color_value": "dark_orange",
        "colormap": None, "n_colors": None,
        "grid": "vertical", "legend": False, "rotate_x": False,
    },
    {  # Plot 10
        "num": 10, "seed": 510,
        "n_groups": 3, "n_series": 2, "orientation": "vertical",
        "categories": ["Kerosene", "Hexane", "Toluene"],
        "series_names": ["La", "Nd"],
        "title": "Extraction Efficiency Distribution by Diluent Type",
        "x_label": "Diluent", "y_label": "Extraction Efficiency (%)",
        "metric": "extraction_eff",
        "outliers": True, "notched": True,
        "color_type": "colormap", "color_value": None,
        "colormap": "Paired", "n_colors": 2,
        "grid": "horizontal", "legend": True, "rotate_x": False,
    },
]


def get_colors_list(cfg):
    """Return list of colors for each series."""
    if cfg["color_type"] == "single":
        return [COLORS[cfg["color_value"]]]
    else:
        cmap = matplotlib.colormaps[cfg["colormap"]]
        return [cmap(i) for i in range(cfg["n_colors"])]


def generate_box_data(rng, metric, n_points, has_outliers):
    """Generate raw data for a single box."""
    params = METRIC_PARAMS[metric]
    mean = rng.uniform(*params["mean_range"])
    std = rng.uniform(*params["std_range"])
    # Non-round mean/std
    mean = round(mean, 2)
    std = round(std, 2)

    data = rng.normal(mean, std, n_points)
    data = np.round(data, 2)

    if has_outliers:
        # Compute IQR and add 1-3 outliers outside 1.5*IQR
        q1 = np.percentile(data, 25)
        q3 = np.percentile(data, 75)
        iqr = q3 - q1
        n_outliers = rng.randint(1, 4)
        outlier_vals = []
        for _ in range(n_outliers):
            if rng.random() < 0.5:
                # Low outlier
                outlier_vals.append(round(q1 - rng.uniform(1.6, 2.5) * iqr, 2))
            else:
                # High outlier
                outlier_vals.append(round(q3 + rng.uniform(1.6, 2.5) * iqr, 2))
        data = np.append(data, outlier_vals)
    else:
        # Clip to within 1.5*IQR
        q1 = np.percentile(data, 25)
        q3 = np.percentile(data, 75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        data = np.clip(data, lower, upper)
        data = np.round(data, 2)

    return data.tolist()


def extract_box_stats(bp, idx):
    """Extract five-number summary and outliers from a matplotlib boxplot result."""
    whisker_lo = bp['whiskers'][2 * idx].get_ydata()
    whisker_hi = bp['whiskers'][2 * idx + 1].get_ydata()
    cap_lo = bp['caps'][2 * idx].get_ydata()
    cap_hi = bp['caps'][2 * idx + 1].get_ydata()
    median_line = bp['medians'][idx].get_ydata()
    box_path = bp['boxes'][idx].get_path().vertices

    # Whisker ends = cap positions
    minimum = round(float(cap_lo[0]), 4)
    maximum = round(float(cap_hi[0]), 4)
    median = round(float(median_line[0]), 4)

    # Q1 and Q3 from box vertices
    y_vals = [v[1] for v in box_path]
    q1 = round(float(min(set(y_vals) - {min(y_vals)} if len(set(y_vals)) > 2 else y_vals)), 4)
    q3 = round(float(max(set(y_vals) - {max(y_vals)} if len(set(y_vals)) > 2 else y_vals)), 4)

    # More robust: use numpy on the raw data
    # We'll compute these separately
    return minimum, maximum, median


def extract_box_stats_horizontal(bp, idx):
    """Extract stats from horizontal boxplot (x-data instead of y-data)."""
    cap_lo = bp['caps'][2 * idx].get_xdata()
    cap_hi = bp['caps'][2 * idx + 1].get_xdata()
    median_line = bp['medians'][idx].get_xdata()

    minimum = round(float(cap_lo[0]), 4)
    maximum = round(float(cap_hi[0]), 4)
    median = round(float(median_line[0]), 4)
    return minimum, maximum, median


def compute_stats_from_data(raw_data):
    """Compute five-number summary and outliers matching matplotlib's boxplot defaults."""
    arr = np.array(raw_data)
    q1 = float(np.percentile(arr, 25))
    q3 = float(np.percentile(arr, 75))
    median = float(np.median(arr))
    iqr = q3 - q1

    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr

    # Whisker ends: most extreme data within fences
    within = arr[(arr >= lower_fence) & (arr <= upper_fence)]
    minimum = float(np.min(within)) if len(within) > 0 else float(np.min(arr))
    maximum = float(np.max(within)) if len(within) > 0 else float(np.max(arr))

    # Outliers: outside fences
    outliers = arr[(arr < lower_fence) | (arr > upper_fence)]
    outliers = sorted([round(float(o), 2) for o in outliers])

    return {
        "minimum": round(minimum, 2),
        "q1": round(q1, 2),
        "median": round(median, 2),
        "q3": round(q3, 2),
        "maximum": round(maximum, 2),
        "outliers": outliers,
    }


def apply_common_style(ax):
    """Apply shared styling."""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)


def generate_plot(cfg, outdir):
    """Generate a single box plot and its metadata."""
    num = cfg["num"]
    rng = np.random.RandomState(cfg["seed"])

    n_groups = cfg["n_groups"]
    n_series = cfg["n_series"]
    colors = get_colors_list(cfg)
    is_multi = n_series > 1
    box_width = BOX_WIDTH_MULTI if is_multi else BOX_WIDTH_SINGLE

    # Generate all raw data
    # all_data[g][s] = list of floats
    all_data = []
    for g in range(n_groups):
        group_data = []
        n_points = rng.randint(30, 51)
        for s in range(n_series):
            data = generate_box_data(rng, cfg["metric"], n_points, cfg["outliers"])
            group_data.append(data)
        all_data.append(group_data)

    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    apply_common_style(ax)

    # Determine positions for boxes
    positions = []
    all_flat_data = []
    box_colors = []

    if is_multi:
        for g in range(n_groups):
            center = g + 1
            offsets = np.linspace(-(n_series - 1) * box_width / 2,
                                  (n_series - 1) * box_width / 2,
                                  n_series)
            for s in range(n_series):
                positions.append(center + offsets[s])
                all_flat_data.append(all_data[g][s])
                box_colors.append(colors[s])
    else:
        for g in range(n_groups):
            positions.append(g + 1)
            all_flat_data.append(all_data[g][0])
            box_colors.append(colors[0])

    is_horizontal = cfg["orientation"] == "horizontal"

    bp = ax.boxplot(
        all_flat_data,
        positions=positions,
        widths=box_width,
        vert=(not is_horizontal),
        notch=cfg["notched"],
        patch_artist=True,
        showfliers=cfg["outliers"],
    )

    # Style boxes
    for i, patch in enumerate(bp['boxes']):
        patch.set_facecolor(box_colors[i])
        patch.set_edgecolor('black')
        patch.set_linewidth(EDGE_LW)
        patch.set_alpha(0.7)

    for median in bp['medians']:
        median.set_color('black')
        median.set_linewidth(MEDIAN_LW)

    for whisker in bp['whiskers']:
        whisker.set_color('black')
        whisker.set_linewidth(WHISKER_LW)

    for cap in bp['caps']:
        cap.set_color('black')
        cap.set_linewidth(WHISKER_LW)

    if cfg["outliers"]:
        for i, flier in enumerate(bp['fliers']):
            flier.set_marker('o')
            flier.set_markersize(FLIER_SIZE)
            flier.set_markerfacecolor(box_colors[i])
            flier.set_markeredgecolor(box_colors[i])

    # Set tick labels
    if is_horizontal:
        tick_positions = list(range(1, n_groups + 1))
        ax.set_yticks(tick_positions)
        ax.set_yticklabels(cfg["categories"], fontsize=TICK_LABEL_FONTSIZE)
        ax.set_xlabel(cfg["y_label"], fontsize=AXIS_LABEL_FONTSIZE)
        ax.set_ylabel(cfg["x_label"], fontsize=AXIS_LABEL_FONTSIZE)
    else:
        tick_positions = list(range(1, n_groups + 1))
        ax.set_xticks(tick_positions)
        if cfg["rotate_x"]:
            ax.set_xticklabels(cfg["categories"], fontsize=TICK_LABEL_FONTSIZE,
                               rotation=45, ha='right')
        else:
            ax.set_xticklabels(cfg["categories"], fontsize=TICK_LABEL_FONTSIZE)
        ax.set_xlabel(cfg["x_label"], fontsize=AXIS_LABEL_FONTSIZE)
        ax.set_ylabel(cfg["y_label"], fontsize=AXIS_LABEL_FONTSIZE)

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

    # Legend for multi-series
    if cfg["legend"] and is_multi:
        from matplotlib.patches import Patch
        handles = [Patch(facecolor=colors[s], edgecolor='black', linewidth=0.6,
                         alpha=0.7, label=cfg["series_names"][s])
                   for s in range(n_series)]
        ax.legend(handles=handles, loc='upper right', frameon=True,
                  edgecolor='lightgray', fancybox=False, fontsize=TICK_LABEL_FONTSIZE)

    # Save with exact dimensions
    fig.set_size_inches(8, 6)
    fig.subplots_adjust(left=0.12, right=0.95, top=0.92, bottom=0.12)
    if cfg["rotate_x"]:
        fig.subplots_adjust(bottom=0.20)
    if is_horizontal:
        fig.subplots_adjust(left=0.18)

    png_path = os.path.join(outdir, f"boxplot{num}.png")
    fig.savefig(png_path, dpi=DPI, facecolor='white')
    plt.close(fig)

    # Build ground truth metadata
    boxes_json = []
    idx = 0
    for g in range(n_groups):
        for s in range(n_series):
            raw = all_data[g][s]
            stats = compute_stats_from_data(raw)
            series_label = cfg["series_names"][s] if is_multi else None
            boxes_json.append({
                "group_label": cfg["categories"][g],
                "series_label": series_label,
                "stats": stats,
                "raw_data": [round(float(v), 2) for v in raw],
            })
            idx += 1

    write_metadata(cfg, boxes_json, outdir)
    print(f"  Generated boxplot{num}.png and boxplot{num}.md")


def write_metadata(cfg, boxes_json, outdir):
    """Write ground truth markdown+JSON."""
    num = cfg["num"]
    orient_str = "Vertical" if cfg["orientation"] == "vertical" else "Horizontal"
    outlier_str = "Yes" if cfg["outliers"] else "No"
    notch_str = "Yes" if cfg["notched"] else "No"

    json_data = {
        "title": cfg["title"],
        "x_label": cfg["x_label"],
        "y_label": cfg["y_label"],
        "boxes": boxes_json,
    }
    json_str = json.dumps(json_data, indent=2)

    notes_parts = []
    if cfg["color_type"] == "single":
        notes_parts.append(f"Single box color: {COLORS[cfg['color_value']]}.")
    else:
        notes_parts.append(f"Color scheme: {cfg['colormap']} with {cfg['n_colors']} colors.")
    if cfg["notched"]:
        notes_parts.append("Notched box style applied.")
    if cfg["rotate_x"]:
        notes_parts.append("X-tick labels rotated 45 degrees, right-aligned.")
    if cfg["legend"]:
        notes_parts.append("Legend displayed upper right with light gray border frame.")
    grid_desc = {
        "horizontal": "Horizontal gridlines only.",
        "vertical": "Vertical gridlines only.",
    }
    notes_parts.append(grid_desc[cfg["grid"]])
    notes_text = " ".join(notes_parts)

    md = f"""# Ground Truth: boxplot{num}

## Plot Configuration

- **Plot type**: Box plot
- **Orientation**: {orient_str}
- **Number of groups**: {cfg['n_groups']}
- **Number of series per group**: {cfg['n_series']}
- **Outliers shown**: {outlier_str}
- **Notched**: {notch_str}
- **numpy seed**: {cfg['seed']}

## Data

```json
{json_str}
```

## Notes

{notes_text}
"""
    filepath = os.path.join(outdir, f"boxplot{num}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)


def validate(outdir):
    """Validate all outputs."""
    from PIL import Image
    all_ok = True
    for i in range(1, 11):
        png = os.path.join(outdir, f"boxplot{i}.png")
        md = os.path.join(outdir, f"boxplot{i}.md")

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
                print(f"  boxplot{i}.png: size {w}x{h} (expected 2400x1800)")

        if os.path.isfile(md):
            with open(md, 'r', encoding='utf-8') as f:
                content = f.read()
            try:
                json_start = content.index('```json\n') + 8
                json_end = content.index('\n```', json_start)
                parsed = json.loads(content[json_start:json_end])
                # Check each box has stats and raw_data
                for box in parsed["boxes"]:
                    if "stats" not in box or "raw_data" not in box:
                        print(f"  boxplot{i}.md: missing stats or raw_data")
                        all_ok = False
                    elif len(box["raw_data"]) < 20:
                        print(f"  boxplot{i}.md: raw_data has only {len(box['raw_data'])} points")
            except (ValueError, json.JSONDecodeError) as e:
                print(f"  boxplot{i}.md: JSON parse error — {e}")
                all_ok = False

    return all_ok


def main():
    outdir = os.path.dirname(os.path.abspath(__file__))
    print(f"Output directory: {outdir}")
    print(f"Generating 10 box plots...\n")

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
                   if f.startswith('boxplot') and (f.endswith('.png') or f.endswith('.md')))
    print(f"\nGenerated files ({len(files)}):")
    for f in files:
        full = os.path.join(outdir, f)
        size = os.path.getsize(full)
        print(f"  {full}  ({size:,} bytes)")


if __name__ == "__main__":
    main()
