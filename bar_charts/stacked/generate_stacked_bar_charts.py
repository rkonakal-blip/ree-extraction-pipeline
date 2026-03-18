"""
Generate 10 synthetic stacked bar chart images with ground truth metadata
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

# ── Plot configurations ──────────────────────────────────────────────
PLOTS = [
    {  # Plot 1
        "num": 1, "seed": 201,
        "n_groups": 5, "n_segments": 3, "orientation": "vertical",
        "categories": ["1.5", "2.0", "2.5", "3.0", "3.5"],
        "segments": ["Organic phase", "Aqueous phase", "Interfacial"],
        "title": "Phase Distribution Across pH Levels",
        "x_label": "pH", "y_label": "Proportion (%)",
        "y_range": [0, 100], "metric_type": "percentage",
        "colormap": "tab10", "n_colors": 3,
        "grid": "horizontal", "rotate_x": False,
    },
    {  # Plot 2
        "num": 2, "seed": 202,
        "n_groups": 4, "n_segments": 4, "orientation": "vertical",
        "categories": ["La", "Ce", "Nd", "Pr"],
        "segments": ["Extracted", "Raffinate", "Scrubbed", "Stripped"],
        "title": "REE Mass Distribution After Solvent Extraction",
        "x_label": "REE Element", "y_label": "Mass Distribution (%)",
        "y_range": [0, 100], "metric_type": "percentage",
        "colormap": "tab10", "n_colors": 4,
        "grid": "horizontal", "rotate_x": False,
    },
    {  # Plot 3
        "num": 3, "seed": 203,
        "n_groups": 6, "n_segments": 3, "orientation": "vertical",
        "categories": ["20", "30", "40", "50", "60", "70"],
        "segments": ["D2EHPA fraction", "PC88A fraction", "Residual"],
        "title": "Extraction Fraction by Temperature",
        "x_label": "Temperature (\u00b0C)", "y_label": "Extraction Efficiency (%)",
        "y_range": [0, 100], "metric_type": "percentage",
        "colormap": "Set2", "n_colors": 3,
        "grid": "horizontal", "rotate_x": False,
    },
    {  # Plot 4
        "num": 4, "seed": 204,
        "n_groups": 5, "n_segments": 5, "orientation": "vertical",
        "categories": ["D2EHPA", "Cyanex 272", "PC88A", "TBP", "EHEHPA"],
        "segments": ["La", "Ce", "Nd", "Pr", "Others"],
        "title": "Reagent Composition Effect on REE Recovery",
        "x_label": "Extractant", "y_label": "Composition (%)",
        "y_range": [0, 100], "metric_type": "percentage",
        "colormap": "tab10", "n_colors": 5,
        "grid": "horizontal", "rotate_x": True,
    },
    {  # Plot 5
        "num": 5, "seed": 205,
        "n_groups": 4, "n_segments": 3, "orientation": "horizontal",
        "categories": ["Stage 1", "Stage 2", "Stage 3", "Stage 4"],
        "segments": ["REE fraction", "Iron impurity", "Silica impurity"],
        "title": "Mass Balance Across Leaching Stages",
        "x_label": "Leaching Stage", "y_label": "Mass (mg)",
        "y_range": [0, 500], "metric_type": "absolute",
        "abs_total_range": (200, 480),
        "colormap": "Set1", "n_colors": 3,
        "grid": "vertical", "rotate_x": False,
    },
    {  # Plot 6
        "num": 6, "seed": 206,
        "n_groups": 6, "n_segments": 4, "orientation": "vertical",
        "categories": ["5", "10", "20", "30", "45", "60"],
        "segments": ["Fast extraction", "Slow extraction", "Equilibrium", "Residual"],
        "title": "Extraction Kinetics by Contact Time",
        "x_label": "Contact Time (min)", "y_label": "Extraction Efficiency (%)",
        "y_range": [0, 100], "metric_type": "percentage",
        "colormap": "tab20", "n_colors": 4,
        "grid": "horizontal", "rotate_x": False,
    },
    {  # Plot 7
        "num": 7, "seed": 207,
        "n_groups": 5, "n_segments": 3, "orientation": "vertical",
        "categories": ["1", "2", "3", "4", "5"],
        "segments": ["Free ion", "Mono-complex", "Di-complex"],
        "title": "Species Distribution vs Aqueous pH",
        "x_label": "Aqueous pH", "y_label": "Species Distribution (%)",
        "y_range": [0, 100], "metric_type": "percentage",
        "colormap": "Paired", "n_colors": 3,
        "grid": "horizontal", "rotate_x": False,
    },
    {  # Plot 8
        "num": 8, "seed": 208,
        "n_groups": 4, "n_segments": 6, "orientation": "vertical",
        "categories": ["S1", "S2", "S3", "S4"],
        "segments": ["La", "Ce", "Nd", "Pr", "Sm", "Others"],
        "title": "Elemental Composition of Ore Samples",
        "x_label": "Ore Sample", "y_label": "Elemental Composition (%)",
        "y_range": [0, 100], "metric_type": "percentage",
        "colormap": "tab10", "n_colors": 6,
        "grid": "horizontal", "rotate_x": False,
    },
    {  # Plot 9
        "num": 9, "seed": 209,
        "n_groups": 5, "n_segments": 4, "orientation": "vertical",
        "categories": ["1:3", "1:2", "1:1", "2:1", "3:1"],
        "segments": ["Extracted", "Co-extracted", "Scrubbed", "Stripped"],
        "title": "Recovery Distribution Across A:O Ratios",
        "x_label": "A:O Ratio", "y_label": "Recovery (%)",
        "y_range": [0, 100], "metric_type": "percentage",
        "colormap": "Set2", "n_colors": 4,
        "grid": "horizontal", "rotate_x": False,
    },
    {  # Plot 10
        "num": 10, "seed": 210,
        "n_groups": 6, "n_segments": 3, "orientation": "horizontal",
        "categories": ["La", "Ce", "Pr", "Nd", "Sm", "Eu"],
        "segments": ["Extracted fraction", "Aqueous residual", "Precipitated"],
        "title": "REE Concentration Distribution After Processing",
        "x_label": "REE Element", "y_label": "Concentration (mg/L)",
        "y_range": [0, 300], "metric_type": "absolute",
        "abs_total_range": (120, 280),
        "colormap": "tab10", "n_colors": 3,
        "grid": "vertical", "rotate_x": False,
    },
]


def generate_percentage_data(rng, n_groups, n_segments):
    """Generate segment values that sum to exactly 100% per group."""
    all_values = []
    for _ in range(n_groups):
        raw = rng.uniform(0.5, 10, n_segments)
        proportions = raw / raw.sum() * 100.0
        # Round to 1 decimal, adjust last segment to ensure sum = 100.0
        rounded = np.round(proportions, 1)
        rounded[-1] = np.round(100.0 - rounded[:-1].sum(), 1)
        all_values.append(rounded)
    return np.array(all_values)


def generate_absolute_data(rng, n_groups, n_segments, total_range):
    """Generate segment values with realistic totals for absolute metrics."""
    all_values = []
    for _ in range(n_groups):
        total = rng.uniform(*total_range)
        raw = rng.uniform(0.5, 10, n_segments)
        proportions = raw / raw.sum() * total
        rounded = np.round(proportions, 1)
        all_values.append(rounded)
    return np.array(all_values)


def get_colors(colormap_name, n_colors):
    """Get colors from the specified colormap."""
    cmap = plt.cm.get_cmap(colormap_name)
    return [cmap(i) for i in range(n_colors)]


def apply_common_style(ax):
    """Apply shared styling to axes."""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)


def write_metadata(cfg, data, outdir):
    """Write ground truth markdown+JSON for a stacked bar plot."""
    num = cfg["num"]
    orient_str = "Vertical" if cfg["orientation"] == "vertical" else "Horizontal"

    bars_list = []
    for g in range(cfg["n_groups"]):
        seg_list = []
        cumulative = 0.0
        for s in range(cfg["n_segments"]):
            val = float(data[g, s])
            seg_list.append({
                "name": cfg["segments"][s],
                "value": val,
                "cumulative_bottom": round(cumulative, 1),
            })
            cumulative += val
        bars_list.append({
            "label": cfg["categories"][g],
            "segments": seg_list,
        })

    json_data = {
        "title": cfg["title"],
        "x_label": cfg["x_label"],
        "y_label": cfg["y_label"],
        "y_axis_range": cfg["y_range"],
        "segments": cfg["segments"],
        "bars": bars_list,
    }

    json_str = json.dumps(json_data, indent=2)

    notes_parts = []
    if cfg["rotate_x"]:
        notes_parts.append("X-tick labels rotated 45 degrees, right-aligned.")
    notes_parts.append(f"Color scheme: {cfg['colormap']} with {cfg['n_colors']} colors.")
    grid_desc = {
        "horizontal": "Horizontal gridlines only.",
        "vertical": "Vertical gridlines only.",
    }
    notes_parts.append(grid_desc[cfg["grid"]])
    notes_parts.append("Legend displayed upper right with light gray border frame.")
    if cfg["metric_type"] == "percentage":
        notes_parts.append("All bars sum to 100%.")
    notes_text = " ".join(notes_parts)

    md = f"""# Ground Truth: stacked_barplot{num}

## Plot Configuration

- **Plot type**: Stacked bar chart
- **Orientation**: {orient_str}
- **Number of groups**: {cfg['n_groups']}
- **Number of segments**: {cfg['n_segments']}
- **Y-axis metric**: {cfg['y_label']}
- **numpy seed**: {cfg['seed']}

## Data

```json
{json_str}
```

## Notes

{notes_text}
"""
    filepath = os.path.join(outdir, f"stacked_barplot{num}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)


def generate_plot(cfg, outdir):
    """Generate a single stacked bar chart and its metadata."""
    num = cfg["num"]
    rng = np.random.RandomState(cfg["seed"])

    # Generate data
    if cfg["metric_type"] == "percentage":
        data = generate_percentage_data(rng, cfg["n_groups"], cfg["n_segments"])
    else:
        data = generate_absolute_data(rng, cfg["n_groups"], cfg["n_segments"],
                                      cfg["abs_total_range"])

    colors = get_colors(cfg["colormap"], cfg["n_colors"])

    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    apply_common_style(ax)

    cats = cfg["categories"]
    n_groups = cfg["n_groups"]
    n_segments = cfg["n_segments"]

    if cfg["orientation"] == "vertical":
        x = np.arange(n_groups)
        bottoms = np.zeros(n_groups)
        for s in range(n_segments):
            ax.bar(x, data[:, s], width=BAR_WIDTH_V, bottom=bottoms,
                   color=colors[s], edgecolor=EDGE_COLOR, linewidth=EDGE_LW,
                   label=cfg["segments"][s])
            bottoms += data[:, s]

        ax.set_xticks(x)
        if cfg["rotate_x"]:
            ax.set_xticklabels(cats, fontsize=TICK_LABEL_FONTSIZE,
                               rotation=45, ha='right')
        else:
            ax.set_xticklabels(cats, fontsize=TICK_LABEL_FONTSIZE)
        ax.set_ylim(cfg["y_range"])
        ax.set_xlabel(cfg["x_label"], fontsize=AXIS_LABEL_FONTSIZE)
        ax.set_ylabel(cfg["y_label"], fontsize=AXIS_LABEL_FONTSIZE)
    else:
        # Horizontal
        y = np.arange(n_groups)
        lefts = np.zeros(n_groups)
        for s in range(n_segments):
            ax.barh(y, data[:, s], height=BAR_WIDTH_H, left=lefts,
                    color=colors[s], edgecolor=EDGE_COLOR, linewidth=EDGE_LW,
                    label=cfg["segments"][s])
            lefts += data[:, s]

        ax.set_yticks(y)
        ax.set_yticklabels(cats, fontsize=TICK_LABEL_FONTSIZE)
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

    # Legend — all plots have legends
    ax.legend(loc='upper right', frameon=True, edgecolor='lightgray',
              fancybox=False, fontsize=TICK_LABEL_FONTSIZE)

    # Save with exact dimensions
    fig.set_size_inches(8, 6)
    fig.subplots_adjust(left=0.12, right=0.95, top=0.92, bottom=0.12)
    if cfg["rotate_x"]:
        fig.subplots_adjust(bottom=0.20)
    if cfg["orientation"] == "horizontal":
        fig.subplots_adjust(left=0.18)

    png_path = os.path.join(outdir, f"stacked_barplot{num}.png")
    fig.savefig(png_path, dpi=DPI, facecolor='white')
    plt.close(fig)

    # Write metadata
    write_metadata(cfg, data, outdir)
    print(f"  Generated stacked_barplot{num}.png and stacked_barplot{num}.md")


def validate(outdir):
    """Validate all outputs."""
    from PIL import Image
    all_ok = True
    for i in range(1, 11):
        png = os.path.join(outdir, f"stacked_barplot{i}.png")
        md = os.path.join(outdir, f"stacked_barplot{i}.md")

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
                print(f"  stacked_barplot{i}.png: size {w}x{h} (expected 2400x1800)")

        # Check MD contains valid JSON
        if os.path.isfile(md):
            with open(md, 'r', encoding='utf-8') as f:
                content = f.read()
            try:
                json_start = content.index('```json\n') + 8
                json_end = content.index('\n```', json_start)
                parsed = json.loads(content[json_start:json_end])
                # Verify percentage sums
                for bar in parsed["bars"]:
                    total = sum(seg["value"] for seg in bar["segments"])
                    if "%" in parsed["y_label"] and abs(total - 100.0) > 0.2:
                        print(f"  stacked_barplot{i}.md: bar '{bar['label']}' sums to {total:.1f}%, expected 100%")
                        all_ok = False
            except (ValueError, json.JSONDecodeError) as e:
                print(f"  stacked_barplot{i}.md: JSON parse error — {e}")
                all_ok = False

    return all_ok


def main():
    outdir = os.path.dirname(os.path.abspath(__file__))
    print(f"Output directory: {outdir}")
    print(f"Generating 10 stacked bar charts...\n")

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
                   if f.startswith('stacked_barplot') and (f.endswith('.png') or f.endswith('.md')))
    print(f"\nGenerated files ({len(files)}):")
    for f in files:
        full = os.path.join(outdir, f)
        size = os.path.getsize(full)
        print(f"  {full}  ({size:,} bytes)")


if __name__ == "__main__":
    main()
