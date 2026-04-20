import io
import random
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from config import REE_ELEMENTS

plt.rcParams.update({
    'font.family':       'serif',
    'font.size':         8,
    'axes.spines.top':   False,
    'axes.spines.right': False,
    'axes.linewidth':    0.7,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'lines.linewidth':   1.4,
    'figure.dpi':        100,
})

# ── Helpers ───────────────────────────────────────────────────────────────────

def _ree_sample(n=5):
    return random.sample(REE_ELEMENTS, min(n, len(REE_ELEMENTS)))

def _save(fig, dpi, is_vector):
    buf = io.BytesIO()
    fmt = "svg" if is_vector else "png"
    fig.savefig(buf, dpi=dpi, format=fmt, bbox_inches="tight", facecolor='white')
    plt.close(fig)
    buf.seek(0)
    return buf

def _new_fig(w, h):
    return plt.subplots(figsize=(w, h), layout='constrained')

def _new_fig_polar(w, h):
    fig = plt.figure(figsize=(w, h), layout='constrained')
    ax  = fig.add_subplot(111, polar=True)
    return fig, ax

def _r2(v):
    """Round to 2 dp for compact JSON storage."""
    if isinstance(v, (list, np.ndarray)):
        return [round(float(x), 2) for x in v]
    return round(float(v), 2)

# ── Individual generators — each returns (buf, data_gt) ──────────────────────

def _bar_plain(w, h, dpi, is_vector):
    fig, ax = _new_fig(w, h)
    elements = _ree_sample(random.randint(4, 8))
    values   = np.random.uniform(30, 98, len(elements))
    ax.bar(elements, values, color=plt.cm.tab10(np.linspace(0, 1, len(elements))))
    ax.set_ylabel("Recovery (%)"); ax.set_xlabel("REE"); ax.set_ylim(0, 105)
    ax.tick_params(axis='x', rotation=30)
    data_gt = {"chart_type": "bar", "x": elements, "y": _r2(values),
               "xlabel": "REE", "ylabel": "Recovery (%)"}
    return _save(fig, dpi, is_vector), data_gt


def _bar_grouped(w, h, dpi, is_vector):
    fig, ax = _new_fig(w, h)
    elements = _ree_sample(random.randint(3, 6))
    solvents = random.sample(["D2EHPA", "Cyanex 272", "TBP", "EHEHPA", "PC88A"],
                             random.randint(2, 3))
    x     = np.arange(len(elements))
    width = 0.8 / len(solvents)
    groups = {}
    for i, s in enumerate(solvents):
        vals = np.random.uniform(20, 95, len(elements))
        ax.bar(x + i * width - 0.4 + width / 2, vals, width, label=s)
        groups[s] = _r2(vals)
    ax.set_xticks(x); ax.set_xticklabels(elements, rotation=30)
    ax.set_ylabel("Extraction (%)"); ax.legend(fontsize=7)
    data_gt = {"chart_type": "grouped_bar", "x": elements, "groups": groups,
               "xlabel": "REE", "ylabel": "Extraction (%)"}
    return _save(fig, dpi, is_vector), data_gt


def _bar_stacked(w, h, dpi, is_vector):
    fig, ax = _new_fig(w, h)
    elements = _ree_sample(random.randint(4, 7))
    phases   = ["Aqueous", "Organic", "Precipitate"]
    bottoms  = np.zeros(len(elements))
    stacks   = {}
    for ph in phases:
        vals = np.random.uniform(5, 50, len(elements))
        ax.bar(elements, vals, bottom=bottoms, label=ph)
        stacks[ph] = _r2(vals)
        bottoms += vals
    ax.set_ylabel("Concentration (mg/L)"); ax.legend(fontsize=7)
    ax.tick_params(axis='x', rotation=30)
    data_gt = {"chart_type": "stacked_bar", "x": elements, "stacks": stacks,
               "xlabel": "REE", "ylabel": "Concentration (mg/L)"}
    return _save(fig, dpi, is_vector), data_gt


def _scatter(w, h, dpi, is_vector):
    fig, ax = _new_fig(w, h)
    n   = random.randint(20, 60)
    x   = np.random.uniform(1, 6, n)
    y   = 100 / (1 + np.exp(-(x - 3.5))) + np.random.normal(0, 5, n)
    y   = np.clip(y, 0, 100)
    ree = random.choice(REE_ELEMENTS)
    ax.scatter(x, y, alpha=0.7, color=plt.cm.tab10(random.random()))
    ax.set_xlabel("pH"); ax.set_ylabel(f"{ree} Recovery (%)")
    data_gt = {"chart_type": "scatter", "x": _r2(x), "y": _r2(y),
               "xlabel": "pH", "ylabel": f"{ree} Recovery (%)"}
    return _save(fig, dpi, is_vector), data_gt


def _scatter_line(w, h, dpi, is_vector):
    fig, ax = _new_fig(w, h)
    n = random.randint(15, 40)
    x = np.sort(np.random.uniform(0, 10, n))
    y = 2.5 * x + np.random.normal(0, 3, n)
    ax.scatter(x, y, alpha=0.6, zorder=3)
    m, b = np.polyfit(x, y, 1)
    ax.plot(x, m * x + b, color="red", linewidth=1.5,
            label=f"y={m:.2f}x+{b:.2f}")
    ax.set_xlabel("Contact time (min)"); ax.set_ylabel("Amount adsorbed (mg/g)")
    ax.legend(fontsize=7)
    data_gt = {"chart_type": "scatter_line",
               "x": _r2(x), "y": _r2(y),
               "fit": {"slope": _r2(m), "intercept": _r2(b),
                       "equation": f"y={m:.3f}x+{b:.3f}"},
               "xlabel": "Contact time (min)",
               "ylabel": "Amount adsorbed (mg/g)"}
    return _save(fig, dpi, is_vector), data_gt


def _line(w, h, dpi, is_vector):
    fig, ax = _new_fig(w, h)
    t   = np.linspace(0, 120, 50)
    ree = random.choice(REE_ELEMENTS)
    tau = random.uniform(15, 40)
    y   = 95 * (1 - np.exp(-t / tau)) + np.random.normal(0, 1, 50)
    ax.plot(t, y, linewidth=1.8)
    ax.set_xlabel("Time (min)"); ax.set_ylabel(f"{ree} Recovery (%)")
    ax.set_ylim(0, 105)
    data_gt = {"chart_type": "line",
               "x": _r2(t), "y": _r2(y),
               "xlabel": "Time (min)", "ylabel": f"{ree} Recovery (%)",
               "fit_params": {"plateau": 95.0, "tau_min": _r2(tau)}}
    return _save(fig, dpi, is_vector), data_gt


def _line_multiaxis(w, h, dpi, is_vector):
    fig, ax1 = _new_fig(w, h)
    t  = np.linspace(0, 60, 40)
    y1 = 80 * (1 - np.exp(-t / 20)) + np.random.normal(0, 2, 40)
    y2 = 0.05 * t ** 1.2 + np.random.normal(0, 0.5, 40)
    ax1.plot(t, y1, color="tab:blue");  ax1.set_xlabel("Time (min)")
    ax1.set_ylabel("Recovery (%)", color="tab:blue")
    ax1.tick_params(axis='y', labelcolor="tab:blue")
    ax2 = ax1.twinx()
    ax2.plot(t, y2, color="tab:red", linestyle="--")
    ax2.set_ylabel("Distribution coefficient (D)", color="tab:red")
    ax2.tick_params(axis='y', labelcolor="tab:red")
    data_gt = {"chart_type": "line_multiaxis",
               "x": _r2(t),
               "y1": _r2(y1), "y1_label": "Recovery (%)",
               "y2": _r2(y2), "y2_label": "Distribution coefficient (D)",
               "xlabel": "Time (min)"}
    return _save(fig, dpi, is_vector), data_gt


def _spectra(w, h, dpi, is_vector):
    fig, ax   = _new_fig(w, h)
    spec_type = random.choice(["XRD", "FTIR", "Raman"])
    peaks_info = []

    if spec_type == "XRD":
        x    = np.linspace(10, 80, 500)
        y    = np.random.exponential(0.3, 500)
        idxs = np.random.choice(range(50, 450), size=random.randint(4, 10), replace=False)
        for p in idxs:
            sigma = random.uniform(1.5, 4)
            amp   = random.uniform(2, 8)
            y    += amp * np.exp(-0.5 * ((np.arange(500) - p) / sigma) ** 2)
            peaks_info.append({"position": _r2(x[p]), "amplitude": _r2(amp),
                               "sigma": _r2(sigma * (70 / 500))})
        ax.set_xlabel("2\u03b8 (degrees)"); ax.set_ylabel("Intensity (a.u.)")

    elif spec_type == "FTIR":
        x    = np.linspace(400, 4000, 500)
        y    = np.ones(500) * 0.9 + np.random.normal(0, 0.02, 500)
        idxs = np.random.choice(range(50, 450), size=random.randint(5, 12), replace=False)
        for d in idxs:
            sigma = random.uniform(3, 10)
            depth = random.uniform(0.1, 0.5)
            y    -= depth * np.exp(-0.5 * ((np.arange(500) - d) / sigma) ** 2)
            peaks_info.append({"wavenumber": _r2(x[d]), "depth": _r2(depth),
                               "sigma_cm": _r2(sigma * (3600 / 500))})
        ax.set_xlabel("Wavenumber (cm\u207b\u00b9)"); ax.set_ylabel("Transmittance")
        ax.invert_xaxis()

    else:  # Raman
        x    = np.linspace(100, 3500, 500)
        y    = np.random.exponential(0.2, 500)
        idxs = np.random.choice(range(30, 470), size=random.randint(3, 8), replace=False)
        for p in idxs:
            sigma = random.uniform(2, 6)
            amp   = random.uniform(1, 5)
            y    += amp * np.exp(-0.5 * ((np.arange(500) - p) / sigma) ** 2)
            peaks_info.append({"shift_cm": _r2(x[p]), "amplitude": _r2(amp),
                               "sigma": _r2(sigma * (3400 / 500))})
        ax.set_xlabel("Raman shift (cm\u207b\u00b9)"); ax.set_ylabel("Intensity (a.u.)")

    ax.plot(x, y, linewidth=0.9, color="black")
    ax.set_title(spec_type, fontsize=9)
    data_gt = {"chart_type": "spectra", "spectra_type": spec_type,
               "x": _r2(x), "y": _r2(y), "peaks": peaks_info,
               "xlabel": ax.get_xlabel(), "ylabel": ax.get_ylabel()}
    return _save(fig, dpi, is_vector), data_gt


def _contour_filled(w, h, dpi, is_vector):
    fig, ax = _new_fig(w, h)
    xv = np.linspace(1, 5, 40); yv = np.linspace(20, 60, 40)
    xg, yg = np.meshgrid(xv, yv)
    z  = 80 - 15 * (xg - 3) ** 2 - 0.05 * (yg - 40) ** 2 + np.random.normal(0, 1, xg.shape)
    cf = ax.contourf(xg, yg, z, levels=10, cmap="viridis")
    plt.colorbar(cf, ax=ax, label="Recovery (%)")
    ax.set_xlabel("pH"); ax.set_ylabel("Temperature (\u00b0C)")
    data_gt = {"chart_type": "contour", "x": _r2(xv), "y": _r2(yv),
               "z": [[_r2(v) for v in row] for row in z],
               "xlabel": "pH", "ylabel": "Temperature (\u00b0C)",
               "colorbar_label": "Recovery (%)"}
    return _save(fig, dpi, is_vector), data_gt


def _contour_line(w, h, dpi, is_vector):
    fig, ax = _new_fig(w, h)
    xv = np.linspace(0, 1, 40); yv = np.linspace(0, 1, 40)
    xg, yg = np.meshgrid(xv, yv)
    z  = np.sin(3 * xg) * np.cos(3 * yg) + np.random.normal(0, 0.05, xg.shape)
    cs = ax.contour(xg, yg, z, levels=8, cmap="RdBu")
    ax.clabel(cs, inline=True, fontsize=7)
    ax.set_xlabel("[Extractant] (M)"); ax.set_ylabel("[REE] (mg/L)")
    data_gt = {"chart_type": "contour_line", "x": _r2(xv), "y": _r2(yv),
               "z": [[_r2(v) for v in row] for row in z],
               "xlabel": "[Extractant] (M)", "ylabel": "[REE] (mg/L)"}
    return _save(fig, dpi, is_vector), data_gt


def _contour_overlaid(w, h, dpi, is_vector):
    fig, ax = _new_fig(w, h)
    xv = np.linspace(1, 6, 40); yv = np.linspace(0.1, 1.0, 40)
    xg, yg = np.meshgrid(xv, yv)
    z  = 90 - 20 * (xg - 3.5) ** 2 - 30 * (yg - 0.5) ** 2 + np.random.normal(0, 1, xg.shape)
    cf = ax.contourf(xg, yg, z, levels=10, cmap="plasma", alpha=0.7)
    ax.contour(xg, yg, z, levels=10, colors="black", linewidths=0.5)
    plt.colorbar(cf, ax=ax, label="Extraction (%)")
    ax.set_xlabel("pH"); ax.set_ylabel("[D2EHPA] (M)")
    data_gt = {"chart_type": "contour_overlaid", "x": _r2(xv), "y": _r2(yv),
               "z": [[_r2(v) for v in row] for row in z],
               "xlabel": "pH", "ylabel": "[D2EHPA] (M)",
               "colorbar_label": "Extraction (%)"}
    return _save(fig, dpi, is_vector), data_gt


def _box_plot(w, h, dpi, is_vector):
    fig, ax   = _new_fig(w, h)
    elements  = _ree_sample(random.randint(3, 6))
    raw_data  = [np.random.normal(random.uniform(40, 90),
                                  random.uniform(3, 15), 30) for _ in elements]
    ax.boxplot(raw_data, labels=elements, patch_artist=True,
               boxprops=dict(facecolor="lightblue"))
    ax.set_ylabel("Recovery (%)"); ax.tick_params(axis='x', rotation=20)
    data_gt = {"chart_type": "box_plot",
               "groups": {el: _r2(d) for el, d in zip(elements, raw_data)},
               "ylabel": "Recovery (%)"}
    return _save(fig, dpi, is_vector), data_gt


def _pie(w, h, dpi, is_vector):
    fig, ax  = _new_fig(w, h)
    elements = _ree_sample(random.randint(4, 7))
    sizes    = np.random.dirichlet(np.ones(len(elements))) * 100
    ax.pie(sizes, labels=elements, autopct="%1.1f%%", startangle=90,
           textprops={"fontsize": 7})
    ax.set_title("REE Composition", fontsize=9)
    data_gt = {"chart_type": "pie",
               "labels": elements, "values": _r2(sizes), "unit": "%"}
    return _save(fig, dpi, is_vector), data_gt


def _heatmap(w, h, dpi, is_vector):
    fig, ax = _new_fig(w, h)
    rows    = _ree_sample(random.randint(4, 8))
    cols    = random.sample(["D2EHPA", "Cyanex 272", "TBP", "PC88A", "EHEHPA"],
                            random.randint(3, 5))
    data    = np.random.uniform(10, 99, (len(rows), len(cols)))
    im = ax.imshow(data, aspect="auto", cmap="YlOrRd", vmin=0, vmax=100)
    ax.set_xticks(range(len(cols))); ax.set_xticklabels(cols, rotation=45, ha="right", fontsize=7)
    ax.set_yticks(range(len(rows))); ax.set_yticklabels(rows, fontsize=7)
    plt.colorbar(im, ax=ax, label="Extraction (%)")
    for i in range(len(rows)):
        for j in range(len(cols)):
            ax.text(j, i, f"{data[i,j]:.0f}", ha="center", va="center",
                    fontsize=6, color="black")
    data_gt = {"chart_type": "heatmap",
               "rows": rows, "cols": cols,
               "data": [[_r2(v) for v in row] for row in data],
               "colorbar_label": "Extraction (%)"}
    return _save(fig, dpi, is_vector), data_gt


def _radar(w, h, dpi, is_vector):
    fig, ax    = _new_fig_polar(w, h)
    categories = random.sample(["Recovery", "Selectivity", "Purity", "Kinetics",
                                 "pH range", "D value", "Efficiency"],
                               random.randint(4, 6))
    N      = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]
    solvents = random.sample(["D2EHPA", "Cyanex 272", "TBP", "EHEHPA"],
                             random.randint(2, 3))
    series = {}
    for s in solvents:
        vals = np.random.uniform(40, 100, N).tolist()
        ax.plot(angles, vals + [vals[0]], label=s)
        ax.fill(angles, vals + [vals[0]], alpha=0.15)
        series[s] = _r2(vals)
    ax.set_thetagrids(np.degrees(angles[:-1]), categories, fontsize=7)
    ax.set_ylim(0, 100)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1), fontsize=7)
    data_gt = {"chart_type": "radar",
               "categories": categories, "series": series}
    return _save(fig, dpi, is_vector), data_gt


def _unknown(w, h, dpi, is_vector):
    variant = random.choice(["sem", "tem", "schematic"])
    fig, ax = _new_fig(w, h)
    if variant in ("sem", "tem"):
        noise = np.random.exponential(0.5, (200, 200))
        noise = (noise - noise.min()) / (noise.max() - noise.min())
        if variant == "tem":
            for _ in range(random.randint(3, 8)):
                cx, cy = random.randint(20, 180), random.randint(20, 180)
                r = random.randint(5, 20)
                gy, gx = np.ogrid[:200, :200]
                noise[(gx - cx)**2 + (gy - cy)**2 < r**2] = np.random.uniform(0.8, 1.0)
        ax.imshow(noise, cmap="gray", interpolation="nearest")
        label = "500 nm" if variant == "sem" else "20 nm"
        ax.set_xlabel(f"Scale bar: {label}", fontsize=7)
        ax.set_xticks([]); ax.set_yticks([])
        data_gt = {"chart_type": "unknown", "subtype": variant,
                   "scale_bar": label, "note": "non-quantitative microscopy image"}
    else:
        steps = random.sample(["Leaching", "Extraction", "Stripping", "Precipitation",
                                "Filtration", "Calcination", "Washing"],
                              random.randint(3, 5))
        ax.set_xlim(0, 10); ax.set_ylim(0, 4); ax.axis("off")
        x = np.linspace(0.5, 9.5, len(steps))
        for i, (xi, step) in enumerate(zip(x, steps)):
            ax.add_patch(plt.Rectangle((xi - 0.6, 1.5), 1.2, 0.9,
                                       color="lightsteelblue", ec="black", lw=0.8))
            ax.text(xi, 1.95, step, ha="center", va="center", fontsize=7)
            if i < len(steps) - 1:
                ax.annotate("", xy=(x[i+1] - 0.6, 1.95), xytext=(xi + 0.6, 1.95),
                            arrowprops=dict(arrowstyle="->", lw=0.8))
        data_gt = {"chart_type": "unknown", "subtype": "schematic",
                   "steps": steps, "note": "non-quantitative process diagram"}
    return _save(fig, dpi, is_vector), data_gt


# ── Multipanel helper — draws on existing Axes, returns data_gt ───────────────

def _draw_on_ax(ax, figure_type):
    """Lightweight draw for a panel inside a multipanel figure. Returns data_gt."""
    if figure_type in ("bar_plain", "bar_grouped", "bar_stacked"):
        els  = _ree_sample(random.randint(3, 5))
        vals = np.random.uniform(20, 95, len(els))
        ax.bar(els, vals); ax.set_ylabel("Recovery (%)")
        ax.tick_params(axis='x', rotation=30, labelsize=6)
        return {"chart_type": "bar", "x": els, "y": _r2(vals),
                "xlabel": "REE", "ylabel": "Recovery (%)"}

    elif figure_type in ("scatter", "scatter_line"):
        x = np.random.uniform(1, 6, 25)
        y = np.clip(80 / (1 + np.exp(-(x - 3))) + np.random.normal(0, 4, 25), 0, 100)
        ax.scatter(x, y, s=15, alpha=0.7)
        ax.set_xlabel("pH"); ax.set_ylabel("Recovery (%)")
        return {"chart_type": "scatter", "x": _r2(x), "y": _r2(y),
                "xlabel": "pH", "ylabel": "Recovery (%)"}

    elif figure_type in ("line", "line_multiaxis"):
        t = np.linspace(0, 60, 40)
        y = 90 * (1 - np.exp(-t / 20)) + np.random.normal(0, 1, 40)
        ax.plot(t, y); ax.set_xlabel("Time (min)"); ax.set_ylabel("Recovery (%)")
        return {"chart_type": "line", "x": _r2(t), "y": _r2(y),
                "xlabel": "Time (min)", "ylabel": "Recovery (%)"}

    elif figure_type == "spectra":
        x  = np.linspace(10, 80, 300)
        y  = np.random.exponential(0.2, 300)
        pk = []
        for p in random.sample(range(30, 270), 5):
            amp = random.uniform(2, 6)
            y  += amp * np.exp(-0.5 * ((np.arange(300) - p) / 4) ** 2)
            pk.append({"position": _r2(x[p]), "amplitude": _r2(amp)})
        ax.plot(x, y, color='black', lw=0.8)
        ax.set_xlabel("2\u03b8 (\u00b0)"); ax.set_ylabel("Intensity (a.u.)")
        return {"chart_type": "spectra", "spectra_type": "XRD",
                "x": _r2(x), "y": _r2(y), "peaks": pk}

    elif figure_type in ("contour_filled", "contour_line", "contour_overlaid"):
        xv = np.linspace(1, 5, 30); yv = np.linspace(20, 60, 30)
        xg, yg = np.meshgrid(xv, yv)
        z  = 80 - 12 * (xg - 3)**2 - 0.04 * (yg - 40)**2
        ax.contourf(xg, yg, z, levels=8, cmap="viridis")
        ax.set_xlabel("pH"); ax.set_ylabel("Temp (\u00b0C)")
        return {"chart_type": "contour", "x": _r2(xv), "y": _r2(yv),
                "z": [[_r2(v) for v in row] for row in z]}

    elif figure_type == "heatmap":
        data = np.random.uniform(10, 99, (5, 4))
        ax.imshow(data, aspect='auto', cmap='YlOrRd', vmin=0, vmax=100)
        ax.set_xticks([]); ax.set_yticks([])
        return {"chart_type": "heatmap",
                "data": [[_r2(v) for v in row] for row in data]}

    elif figure_type == "box_plot":
        els = _ree_sample(4)
        raw = [np.random.normal(random.uniform(50, 90), 10, 25) for _ in els]
        ax.boxplot(raw, labels=els, patch_artist=True,
                   boxprops=dict(facecolor='lightblue'))
        ax.tick_params(axis='x', labelsize=6)
        return {"chart_type": "box_plot",
                "groups": {e: _r2(d) for e, d in zip(els, raw)},
                "ylabel": "Recovery (%)"}

    elif figure_type == "pie":
        els  = _ree_sample(4)
        vals = np.random.dirichlet(np.ones(4)) * 100
        ax.pie(vals, labels=els, autopct='%1.0f%%', textprops={'fontsize': 6})
        return {"chart_type": "pie", "labels": els, "values": _r2(vals)}

    else:
        y = np.random.randn(50).cumsum()
        ax.plot(y); ax.set_xlabel("x"); ax.set_ylabel("y")
        return {"chart_type": "unknown", "y": _r2(y)}


# ── Dispatcher ────────────────────────────────────────────────────────────────

_GENERATORS = {
    "bar_plain":        _bar_plain,
    "bar_grouped":      _bar_grouped,
    "bar_stacked":      _bar_stacked,
    "scatter":          _scatter,
    "scatter_line":     _scatter_line,
    "line":             _line,
    "line_multiaxis":   _line_multiaxis,
    "spectra":          _spectra,
    "contour_filled":   _contour_filled,
    "contour_line":     _contour_line,
    "contour_overlaid": _contour_overlaid,
    "box_plot":         _box_plot,
    "pie":              _pie,
    "heatmap":          _heatmap,
    "radar":            _radar,
    "unknown":          _unknown,
}


def generate_figure(figure_type, width_inches, height_inches, dpi, is_vector,
                    is_multipanel=False, panel_count=1):
    """Return (BytesIO, data_gt dict) for the rendered figure."""
    w, h = width_inches, height_inches

    if is_multipanel and panel_count > 1:
        ncols = min(panel_count, 2)
        nrows = (panel_count + ncols - 1) // ncols
        fig, axes = plt.subplots(nrows, ncols, figsize=(w, h), layout='constrained')
        axes_flat = np.array(axes).flatten()
        panels = []
        for idx, ax in enumerate(axes_flat[:panel_count]):
            panel_gt = _draw_on_ax(ax, figure_type)
            panels.append({"panel_index": idx, "figure_type": figure_type,
                           "data": panel_gt})
        for ax in axes_flat[panel_count:]:
            ax.set_visible(False)
        buf = io.BytesIO()
        fmt = "svg" if is_vector else "png"
        fig.savefig(buf, dpi=dpi, format=fmt, bbox_inches="tight", facecolor='white')
        plt.close(fig)
        buf.seek(0)
        data_gt = {"chart_type": "multipanel", "panel_count": panel_count,
                   "panels": panels}
        return buf, data_gt

    gen = _GENERATORS.get(figure_type, _bar_plain)
    return gen(w, h, dpi, is_vector)
