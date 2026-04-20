"""
Generates raw table data (list of lists) for use by the layout engine.
Returns (data, content_type, orientation) — no ReportLab objects.
"""

import random
import numpy as np
from config import (
    TABLE_CONTENT_TYPES, TABLE_CONTENT_WEIGHTS,
    TABLE_ORIENTATIONS, TABLE_ORIENTATION_WEIGHTS,
    REE_ELEMENTS, TABLE_COL_HEADERS, MOLECULAR_FORMULAS,
)

_EXTRACTANTS = ["D2EHPA", "Cyanex 272", "TBP", "EHEHPA", "PC88A", "Aliquat 336", "TOPO"]
_DILUENTS    = ["kerosene", "n-heptane", "toluene", "dodecane", "isodecanol"]
_MODIFIERS   = ["isodecanol", "TBP", "2-ethylhexanol", "none", "decanol"]
_CONDITIONS  = ["room temp.", "40 \u00b0C", "60 \u00b0C", "25 \u00b0C", "50 \u00b0C"]


def _numerical(n_rows):
    rows = [TABLE_COL_HEADERS["numerical"]]
    for ree in random.sample(REE_ELEMENTS, min(n_rows, len(REE_ELEMENTS))):
        rows.append([
            ree,
            f"{np.random.uniform(1, 500):.2f}",
            f"{np.random.uniform(10, 99.9):.1f}",
            f"{np.random.uniform(0.1, 50):.2f}",
            f"{np.random.uniform(1, 20):.2f}",
        ])
    return rows


def _text_numerical(n_rows):
    rows = [TABLE_COL_HEADERS["text+numerical"]]
    for ext in random.sample(_EXTRACTANTS, min(n_rows, len(_EXTRACTANTS))):
        rows.append([
            ext,
            f"{np.random.uniform(1, 6):.1f}",
            f"{np.random.uniform(30, 99):.1f}",
            f"{np.random.uniform(1, 15):.1f}",
            random.choice(["Good", "Excellent", "Moderate", "High", "Low"]),
        ])
    return rows


def _text(n_rows):
    rows = [TABLE_COL_HEADERS["text"]]
    for _ in range(n_rows):
        rows.append([
            random.choice(_CONDITIONS),
            random.choice(_EXTRACTANTS),
            random.choice(_DILUENTS),
            random.choice(_MODIFIERS),
            random.choice(["Phase split", "Emulsion", "Clean sep.", "Precipitation", "Stable"]),
        ])
    return rows


def _molecular(n_rows):
    rows = [TABLE_COL_HEADERS["molecular"]]
    for name, formula, mw in random.sample(MOLECULAR_FORMULAS, min(n_rows, len(MOLECULAR_FORMULAS))):
        rows.append([
            name, formula,
            f"{mw:.2f}",
            f"{np.random.uniform(95, 99.9):.1f}",
            random.choice(["Sigma-Aldrich", "Merck", "Aladdin", "Alfa Aesar", "TCI"]),
        ])
    return rows


_BUILDERS = {
    "numerical":     _numerical,
    "text+numerical": _text_numerical,
    "text":          _text,
    "molecular":     _molecular,
}


def generate_table_data(content_type=None, orientation=None,
                        allow_across_2_pages=False):
    """Return (data, content_type, orientation).

    data is a list-of-lists (header row first).
    """
    if content_type is None:
        content_type = random.choices(
            TABLE_CONTENT_TYPES, weights=TABLE_CONTENT_WEIGHTS, k=1)[0]
    if orientation is None:
        orientation = random.choices(
            TABLE_ORIENTATIONS, weights=TABLE_ORIENTATION_WEIGHTS, k=1)[0]
    if not allow_across_2_pages and orientation == 'across_2_pages':
        orientation = 'across_2_col'

    n_rows = random.randint(3, 8)
    data   = _BUILDERS[content_type](n_rows)
    return data, content_type, orientation
