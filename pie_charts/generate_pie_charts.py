"""
Generate 10 synthetic pie chart images with ground truth metadata
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
LABEL_FONTSIZE = 9
PCT_FONTSIZE = 9
PIE_RADIUS = 0.85
WEDGE_EDGE_COLOR = 'white'
WEDGE_EDGE_LW = 1.5
MIN_LABEL_PCT = 5.0  # Skip inside labels for slices < 5%

# ── Plot configurations ──────────────────────────────────────────────
PLOTS = [
    {  # Plot 1
        "num": 1, "seed": 701, "n_slices": 5,
        "labels": ["La", "Ce", "Nd", "Pr", "Others"],
        "title": "REE Elemental Composition of Leach Solution",
        "label_style": "slice_labels", "pct_position": "inside",
        "colormap": "tab10", "legend": False, "start_angle": 90,
        "alpha": [4, 6, 3, 2, 2],
    },
    {  # Plot 2
        "num": 2, "seed": 702, "n_slices": 6,
        "labels": ["La", "Ce", "Nd", "Pr", "Sm", "Others"],
        "title": "Composition of Leachate After Acid Digestion",
        "label_style": "legend_only", "pct_position": "inside",
        "colormap": "Set2", "legend": True, "start_angle": 90,
        "alpha": [3, 5, 4, 2, 1.5, 2],
    },
    {  # Plot 3
        "num": 3, "seed": 703, "n_slices": 4,
        "labels": ["Organic phase", "Aqueous phase", "Interfacial", "Precipitate"],
        "title": "Phase Distribution After Solvent Extraction",
        "label_style": "slice_labels", "pct_position": "outside",
        "colormap": "Paired", "legend": False, "start_angle": 0,
        "alpha": [5, 4, 2, 1.5],
    },
    {  # Plot 4
        "num": 4, "seed": 704, "n_slices": 7,
        "labels": ["La", "Ce", "Nd", "Pr", "Sm", "Eu", "Others"],
        "title": "Mineral Composition of REE Ore Sample",
        "label_style": "legend_only", "pct_position": "inside",
        "colormap": "tab10", "legend": True, "start_angle": 90,
        "alpha": [3, 5, 3, 2, 1.5, 1, 2],
    },
    {  # Plot 5
        "num": 5, "seed": 705, "n_slices": 5,
        "labels": ["D2EHPA fraction", "PC88A fraction", "Cyanex fraction", "Raffinate", "Losses"],
        "title": "Solvent Extraction Yield Distribution",
        "label_style": "both", "pct_position": "outside",
        "colormap": "Set1", "legend": False, "start_angle": 45,
        "alpha": [5, 3, 3, 2, 1],
    },
    {  # Plot 6
        "num": 6, "seed": 706, "n_slices": 4,
        "labels": ["La", "Ce", "Nd", "Pr"],
        "title": "REE Distribution in Leachate Solution",
        "label_style": "slice_labels", "pct_position": "inside",
        "colormap": "tab20", "legend": False, "start_angle": 90,
        "alpha": [3, 5, 4, 2],
    },
    {  # Plot 7
        "num": 7, "seed": 707, "n_slices": 6,
        "labels": ["Iron", "Calcium", "Magnesium", "Silica", "Aluminum", "Others"],
        "title": "Impurity Breakdown in Leach Solution",
        "label_style": "legend_only", "pct_position": "inside",
        "colormap": "Set2", "legend": True, "start_angle": 0,
        "alpha": [4, 3, 2.5, 3, 2, 2],
    },
    {  # Plot 8
        "num": 8, "seed": 708, "n_slices": 8,
        "labels": ["La", "Ce", "Nd", "Pr", "Sm", "Eu", "Gd", "Others"],
        "title": "Elemental Composition of REE Ore Sample",
        "label_style": "legend_only", "pct_position": "inside",
        "colormap": "tab10", "legend": True, "start_angle": 90,
        "alpha": [3, 5, 3, 2, 1.5, 1, 1, 2],
    },
    {  # Plot 9
        "num": 9, "seed": 709, "n_slices": 5,
        "labels": ["Extracted", "Stripped", "Scrubbed", "Raffinate", "Losses"],
        "title": "Mass Balance Distribution After Processing",
        "label_style": "both", "pct_position": "outside",
        "colormap": "Paired", "legend": False, "start_angle": 90,
        "alpha": [5, 4, 2, 2, 1],
    },
    {  # Plot 10
        "num": 10, "seed": 710, "n_slices": 6,
        "labels": ["La", "Ce", "Nd", "Pr", "Sm", "Others"],
        "title": "REE Concentrate Composition After Stripping",
        "label_style": "slice_labels", "pct_position": "inside",
        "colormap": "Set1", "legend": False, "start_angle": 45,
        "alpha": [3, 5, 4, 2, 1.5, 2],
    },
]


def get_colors(colormap_name, n):
    cmap = matplotlib.colormaps[colormap_name]
    return [cmap(i) for i in range(n)]


def generate_values(rng, alpha, n_slices):
    """Generate slice percentages summing to exactly 100.0 using Dirichlet."""
    raw = rng.dirichlet(alpha)
    pcts = raw * 100.0
    # Round to 1 decimal
    rounded = np.round(pcts, 1)
    # Adjust last slice to ensure sum = 100.0
    rounded[-1] = round(100.0 - rounded[:-1].sum(), 1)
    return rounded


def generate_plot(cfg, outdir):
    num = cfg["num"]
    rng = np.random.RandomState(cfg["seed"])

    values = generate_values(rng, cfg["alpha"], cfg["n_slices"])
    colors = get_colors(cfg["colormap"], cfg["n_slices"])
    labels = cfg["labels"]

    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    wedge_props = dict(edgecolor=WEDGE_EDGE_COLOR, linewidth=WEDGE_EDGE_LW)

    # Determine what to show
    show_labels_on_slice = cfg["label_style"] in ("slice_labels", "both")
    show_pct = True  # All plots show percentages

    # Build autopct function that hides labels for small slices (inside only)
    if cfg["pct_position"] == "inside":
        def autopct_func(pct):
            if pct < MIN_LABEL_PCT:
                return ''
            return f'{pct:.1f}%'
        pctdistance = 0.6
    else:
        # Outside percentage
        def autopct_func(pct):
            return f'{pct:.1f}%'
        pctdistance = 1.15

    # Labels to pass to pie()
    if show_labels_on_slice:
        pie_labels = labels
    else:
        pie_labels = [''] * cfg["n_slices"]

    # For "both" with outside: we use labels + autopct outside
    if cfg["label_style"] == "both" and cfg["pct_position"] == "outside":
        # Show labels outside, pct outside too
        # We'll combine label+pct in the label text and skip autopct
        combined_labels = [f'{labels[i]}\n({values[i]:.1f}%)' for i in range(cfg["n_slices"])]
        wedges, texts = ax.pie(
            values, labels=combined_labels, colors=colors,
            startangle=cfg["start_angle"], radius=PIE_RADIUS,
            wedgeprops=wedge_props, shadow=False,
            labeldistance=1.12,
        )
        for t in texts:
            t.set_fontsize(LABEL_FONTSIZE)
    elif cfg["pct_position"] == "outside" and cfg["label_style"] == "slice_labels":
        # Labels on slice, pct outside
        wedges, texts, autotexts = ax.pie(
            values, labels=pie_labels, autopct=autopct_func, colors=colors,
            startangle=cfg["start_angle"], radius=PIE_RADIUS,
            wedgeprops=wedge_props, shadow=False,
            pctdistance=pctdistance, labeldistance=1.12,
        )
        for t in texts:
            t.set_fontsize(LABEL_FONTSIZE)
        for t in autotexts:
            t.set_fontsize(PCT_FONTSIZE)
    else:
        # Standard: labels (or empty) + autopct inside
        wedges, texts, autotexts = ax.pie(
            values, labels=pie_labels, autopct=autopct_func, colors=colors,
            startangle=cfg["start_angle"], radius=PIE_RADIUS,
            wedgeprops=wedge_props, shadow=False,
            pctdistance=pctdistance,
        )
        for t in texts:
            t.set_fontsize(LABEL_FONTSIZE)
        for t in autotexts:
            t.set_fontsize(PCT_FONTSIZE)

    ax.set_title(cfg["title"], fontsize=TITLE_FONTSIZE, fontweight='bold', pad=20)
    ax.set_aspect('equal')

    # Legend
    if cfg["legend"]:
        ax.legend(wedges, labels, loc='center left', bbox_to_anchor=(1.0, 0.5),
                  frameon=True, edgecolor='lightgray', fancybox=False,
                  fontsize=LABEL_FONTSIZE)

    # Save with exact dimensions
    fig.set_size_inches(8, 6)
    if cfg["legend"]:
        fig.subplots_adjust(left=0.05, right=0.72, top=0.90, bottom=0.05)
    else:
        fig.subplots_adjust(left=0.05, right=0.95, top=0.90, bottom=0.05)

    png_path = os.path.join(outdir, f"piechart{num}.png")
    fig.savefig(png_path, dpi=DPI, facecolor='white')
    plt.close(fig)

    # Determine skipped labels
    skipped = [labels[i] for i in range(cfg["n_slices"])
               if values[i] < MIN_LABEL_PCT and cfg["pct_position"] == "inside"]

    write_metadata(cfg, values, skipped, outdir)
    print(f"  Generated piechart{num}.png and piechart{num}.md")


def write_metadata(cfg, values, skipped, outdir):
    num = cfg["num"]

    label_style_map = {
        "slice_labels": "Slice labels only",
        "legend_only": "Legend only",
        "both": "Both label and percentage",
    }
    pct_pos_map = {"inside": "Inside slice", "outside": "Outside slice"}

    slices_json = []
    for i in range(cfg["n_slices"]):
        slices_json.append({
            "label": cfg["labels"][i],
            "value": float(values[i]),
            "percentage": float(values[i]),
        })

    json_data = {
        "title": cfg["title"],
        "start_angle": cfg["start_angle"],
        "slices": slices_json,
        "total": 100.0,
    }
    json_str = json.dumps(json_data, indent=2)

    notes_parts = []
    notes_parts.append(f"Color scheme: {cfg['colormap']}.")
    if skipped:
        notes_parts.append(f"Labels skipped for small slices (< 5%): {', '.join(skipped)}.")
    if cfg["legend"]:
        notes_parts.append("Legend placed to the right of the pie chart.")
    notes_parts.append(f"Wedge edges: white, linewidth 1.5.")
    notes_text = " ".join(notes_parts)

    md = f"""# Ground Truth: piechart{num}

## Plot Configuration

- **Plot type**: Pie chart
- **Number of slices**: {cfg['n_slices']}
- **Label style**: {label_style_map[cfg['label_style']]}
- **Percentage position**: {pct_pos_map[cfg['pct_position']]}
- **Start angle**: {cfg['start_angle']}
- **numpy seed**: {cfg['seed']}

## Data

```json
{json_str}
```

## Notes

{notes_text}
"""
    filepath = os.path.join(outdir, f"piechart{num}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)


def validate(outdir):
    from PIL import Image
    all_ok = True
    for i in range(1, 11):
        png = os.path.join(outdir, f"piechart{i}.png")
        md = os.path.join(outdir, f"piechart{i}.md")

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
                print(f"  piechart{i}.png: size {w}x{h} (expected 2400x1800)")

        if os.path.isfile(md):
            with open(md, 'r', encoding='utf-8') as f:
                content = f.read()
            try:
                json_start = content.index('```json\n') + 8
                json_end = content.index('\n```', json_start)
                parsed = json.loads(content[json_start:json_end])
                total = sum(s["percentage"] for s in parsed["slices"])
                if abs(total - 100.0) > 0.15:
                    print(f"  piechart{i}.md: slices sum to {total:.2f}%, expected 100.0%")
                    all_ok = False
            except (ValueError, json.JSONDecodeError) as e:
                print(f"  piechart{i}.md: JSON parse error — {e}")
                all_ok = False

    return all_ok


def main():
    outdir = os.path.dirname(os.path.abspath(__file__))
    print(f"Output directory: {outdir}")
    print(f"Generating 10 pie charts...\n")

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
                   if f.startswith('piechart') and (f.endswith('.png') or f.endswith('.md')))
    print(f"\nGenerated files ({len(files)}):")
    for f in files:
        full = os.path.join(outdir, f)
        size = os.path.getsize(full)
        print(f"  {full}  ({size:,} bytes)")


if __name__ == "__main__":
    main()
