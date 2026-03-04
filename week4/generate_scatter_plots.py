"""
Generate 7 synthetic REE (Rare Earth Element) scatter plots with ground truth JSON files.
Themed around rare earth element extraction science.
"""

import json
import os
import numpy as np

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
np.random.seed(42)
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

COLORS = ['#2b6ca3', '#d45e00', '#2ca02c']
MARKERS = ['o', 's', '^']

PLOT_SPECS = [
    {
        "id": "scatter_01",
        "title": "Effect of HCl Concentration on Nd Extraction",
        "x_label": "HCl Concentration (mol/L)",
        "y_label": "Nd Extraction Efficiency (%)",
        "x_range": (0.5, 6.0),
        "y_range": (20, 98),
        "correlation": "strong_positive",
        "series": [{"name": "Nd"}],
        "n_points": 20,
    },
    {
        "id": "scatter_02",
        "title": "Temperature Dependence of Ce Recovery",
        "x_label": "Temperature (\u00b0C)",
        "y_label": "Ce Recovery Rate (%)",
        "x_range": (25, 90),
        "y_range": (15, 95),
        "correlation": "strong_positive",
        "series": [{"name": "Ce"}],
        "n_points": 20,
    },
    {
        "id": "scatter_03",
        "title": "La Leaching Yield vs Contact Time",
        "x_label": "Contact Time (min)",
        "y_label": "La Leaching Yield (%)",
        "x_range": (10, 180),
        "y_range": (30, 95),
        "correlation": "strong_positive",
        "series": [{"name": "La"}],
        "n_points": 20,
    },
    {
        "id": "scatter_04",
        "title": "Ore Particle Size Effect on Dy Extraction",
        "x_label": "Ore Particle Size (\u03bcm)",
        "y_label": "Dy Extraction Efficiency (%)",
        "x_range": (50, 500),
        "y_range": (30, 80),
        "correlation": "weak_noisy",
        "series": [{"name": "Dy"}],
        "n_points": 20,
    },
    {
        "id": "scatter_05",
        "title": "pH Influence on Eu Distribution Coefficient",
        "x_label": "pH",
        "y_label": "Eu Distribution Coefficient (Kd)",
        "x_range": (1.0, 5.0),
        "y_range": (0.5, 15),
        "correlation": "weak_noisy",
        "series": [{"name": "Eu"}],
        "n_points": 20,
    },
    {
        "id": "scatter_06",
        "title": "D2EHPA Concentration vs Separation Factor",
        "x_label": "D2EHPA Concentration (mol/L)",
        "y_label": "Separation Factor (\u03b2)",
        "x_range": (0.1, 1.0),
        "y_range": (1.0, 8.0),
        "correlation": "positive_varies",
        "series": [{"name": "Nd/Pr"}, {"name": "La/Ce"}],
        "n_points": 18,
    },
    {
        "id": "scatter_07",
        "title": "REE Recovery During Acid Leaching",
        "x_label": "Leaching Time (h)",
        "y_label": "Recovery (%)",
        "x_range": (0.5, 8.0),
        "y_range": (10, 95),
        "correlation": "mixed",
        "series": [{"name": "La"}, {"name": "Ce"}, {"name": "Nd"}],
        "n_points": 15,
    },
]


# ---------------------------------------------------------------------------
# Data generation helpers
# ---------------------------------------------------------------------------

def _generate_x(x_lo, x_hi, n):
    """Uniformly spaced x values with slight jitter."""
    base = np.linspace(x_lo, x_hi, n)
    jitter = np.random.uniform(-0.3, 0.3, n) * (x_hi - x_lo) / n
    x = np.clip(base + jitter, x_lo, x_hi)
    return np.sort(x)


def _strong_positive(x, y_lo, y_hi):
    """Linear with small noise, targeting r > 0.9."""
    x_lo, x_hi = x.min(), x.max()
    slope = (y_hi - y_lo) * 0.85 / (x_hi - x_lo)
    intercept = y_lo + (y_hi - y_lo) * 0.05
    y_range = y_hi - y_lo
    noise = np.random.normal(0, y_range * 0.04, len(x))
    y = intercept + slope * (x - x_lo) + noise
    return np.clip(y, y_lo, y_hi)


def _weak_noisy(x, y_lo, y_hi):
    """Linear with large noise, targeting r ~ 0.3-0.6."""
    x_lo, x_hi = x.min(), x.max()
    slope = (y_hi - y_lo) * 0.35 / (x_hi - x_lo)
    intercept = y_lo + (y_hi - y_lo) * 0.25
    y_range = y_hi - y_lo
    noise = np.random.normal(0, y_range * 0.20, len(x))
    y = intercept + slope * (x - x_lo) + noise
    return np.clip(y, y_lo, y_hi)


def _positive_varies(x, y_lo, y_hi, series_idx):
    """Positive trend with different slope per series."""
    x_lo, x_hi = x.min(), x.max()
    slopes = [0.75, 0.50]
    offsets = [0.0, 0.15]
    s = slopes[series_idx]
    o = offsets[series_idx]
    slope = (y_hi - y_lo) * s / (x_hi - x_lo)
    intercept = y_lo + (y_hi - y_lo) * (0.05 + o)
    y_range = y_hi - y_lo
    noise = np.random.normal(0, y_range * 0.06, len(x))
    y = intercept + slope * (x - x_lo) + noise
    return np.clip(y, y_lo, y_hi)


def _mixed(x, y_lo, y_hi, series_idx):
    """Different curves per series — some saturating, some linear."""
    x_lo, x_hi = x.min(), x.max()
    t = (x - x_lo) / (x_hi - x_lo)  # normalized 0..1
    y_range = y_hi - y_lo
    if series_idx == 0:  # La — saturating curve
        y = y_lo + y_range * 0.85 * (1 - np.exp(-3.0 * t))
    elif series_idx == 1:  # Ce — linear
        y = y_lo + y_range * 0.70 * t + y_range * 0.05
    else:  # Nd — slower rise
        y = y_lo + y_range * 0.55 * t ** 0.7
    noise = np.random.normal(0, y_range * 0.04, len(x))
    y = y + noise
    return np.clip(y, y_lo, y_hi)


def generate_series_data(spec, series_idx=0):
    """Generate (x, y) arrays for one series of a plot."""
    x = _generate_x(*spec["x_range"], spec["n_points"])
    y_lo, y_hi = spec["y_range"]
    corr = spec["correlation"]
    if corr == "strong_positive":
        y = _strong_positive(x, y_lo, y_hi)
    elif corr == "weak_noisy":
        y = _weak_noisy(x, y_lo, y_hi)
    elif corr == "positive_varies":
        y = _positive_varies(x, y_lo, y_hi, series_idx)
    elif corr == "mixed":
        y = _mixed(x, y_lo, y_hi, series_idx)
    else:
        raise ValueError(f"Unknown correlation type: {corr}")
    # Round
    x_dec = 2 if (spec["x_range"][1] - spec["x_range"][0]) < 20 else 1
    y_dec = 2 if (spec["y_range"][1] - spec["y_range"][0]) < 20 else 1
    x = np.round(x, x_dec)
    y = np.round(y, y_dec)
    return x.tolist(), y.tolist()


# ---------------------------------------------------------------------------
# Step 1: Generate ground truth JSON files
# ---------------------------------------------------------------------------

def generate_ground_truth():
    for spec in PLOT_SPECS:
        gt = {
            "plot_id": spec["id"],
            "plot_type": "scatter",
            "title": spec["title"],
            "x_label": spec["x_label"],
            "y_label": spec["y_label"],
            "series": [],
        }
        for i, s in enumerate(spec["series"]):
            x_vals, y_vals = generate_series_data(spec, series_idx=i)
            gt["series"].append({
                "name": s["name"],
                "x": x_vals,
                "y": y_vals,
            })
        path = os.path.join(OUT_DIR, f"{spec['id']}_gt.json")
        with open(path, "w") as f:
            json.dump(gt, f, indent=2)
        print(f"  Wrote {path}")


# ---------------------------------------------------------------------------
# Step 2: Plot from JSON files
# ---------------------------------------------------------------------------

def plot_all():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 10,
        "axes.titlesize": 11,
        "axes.labelsize": 10,
        "legend.fontsize": 9,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
    })

    for spec in PLOT_SPECS:
        json_path = os.path.join(OUT_DIR, f"{spec['id']}_gt.json")
        with open(json_path) as f:
            gt = json.load(f)

        fig, ax = plt.subplots(figsize=(6, 4.5))

        for i, series in enumerate(gt["series"]):
            color = COLORS[i % len(COLORS)]
            marker = MARKERS[i % len(MARKERS)]
            ax.scatter(
                series["x"], series["y"],
                marker=marker,
                facecolors="none",
                edgecolors=color,
                linewidths=1.2,
                s=40,
                label=series["name"],
                zorder=3,
            )

        ax.set_title(gt["title"])
        ax.set_xlabel(gt["x_label"])
        ax.set_ylabel(gt["y_label"])
        ax.legend(frameon=True, framealpha=0.9, edgecolor="#cccccc")
        ax.grid(True, linestyle="--", alpha=0.3, zorder=0)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        fig.patch.set_facecolor("white")
        ax.set_facecolor("white")

        img_path = os.path.join(OUT_DIR, f"{spec['id']}.jpg")
        fig.savefig(img_path, dpi=300, bbox_inches="tight",
                    facecolor="white", format="jpg")
        plt.close(fig)
        print(f"  Wrote {img_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Step 1: Generating ground truth JSON files...")
    generate_ground_truth()
    print("\nStep 2: Plotting from JSON files...")
    plot_all()
    print("\nDone.")
