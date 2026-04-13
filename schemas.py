"""
JSON Schemas and validation for REE extraction pipeline benchmark data.
"""

import json
import re
from pathlib import Path


# --- Schema definitions ---

SCATTER_SCHEMA = {
    "required": ["title", "x_label", "y_label", "series"],
    "series_item": {
        "required": ["name", "points"],
        "point": {"required": ["x", "y"]}
    }
}

PLAIN_BAR_SCHEMA = {
    "required": ["title", "x_label", "y_label", "bars"],
    "bar_item": {"required": ["label", "value"]}
}

GROUPED_BAR_SCHEMA = {
    "required": ["title", "x_label", "y_label", "series", "groups"],
    "group_item": {"required": ["label", "bars"]},
    "bar_item": {"required": ["series", "value"]}
}

STACKED_BAR_SCHEMA = {
    "required": ["title", "x_label", "y_label", "segments", "bars"],
    "bar_item": {"required": ["label", "segments"]},
    "segment_item": {"required": ["name", "value"]}
}

BOX_PLOT_SCHEMA = {
    "required": ["title", "x_label", "y_label", "boxes"],
    "box_item": {
        "required": ["group_label", "stats"],
        "stats": {"required": ["minimum", "q1", "median", "q3", "maximum"]}
    }
}

CONTOUR_MAP_SCHEMA = {
    "required": ["title", "x_label", "y_label", "x_range", "y_range", "z_range",
                  "polynomial_coefficients", "contour_levels", "optimal_point"]
}

PIE_CHART_SCHEMA = {
    "required": ["title", "slices"],
    "slice_item": {"required": ["label", "value", "percentage"]}
}


def validate_scatter(data):
    errors = []
    for f in SCATTER_SCHEMA["required"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "series" in data:
        for i, s in enumerate(data["series"]):
            for f in SCATTER_SCHEMA["series_item"]["required"]:
                if f not in s:
                    errors.append(f"Series {i}: missing field '{f}'")
            if "points" in s:
                for j, p in enumerate(s["points"]):
                    for f in SCATTER_SCHEMA["series_item"]["point"]["required"]:
                        if f not in p:
                            errors.append(f"Series {i}, point {j}: missing '{f}'")
    return errors


def validate_plain_bar(data):
    errors = []
    for f in PLAIN_BAR_SCHEMA["required"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "bars" in data:
        for i, b in enumerate(data["bars"]):
            for f in PLAIN_BAR_SCHEMA["bar_item"]["required"]:
                if f not in b:
                    errors.append(f"Bar {i}: missing field '{f}'")
    return errors


def validate_grouped_bar(data):
    errors = []
    for f in GROUPED_BAR_SCHEMA["required"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "groups" in data:
        for i, g in enumerate(data["groups"]):
            for f in GROUPED_BAR_SCHEMA["group_item"]["required"]:
                if f not in g:
                    errors.append(f"Group {i}: missing field '{f}'")
            if "bars" in g:
                for j, b in enumerate(g["bars"]):
                    for f in GROUPED_BAR_SCHEMA["bar_item"]["required"]:
                        if f not in b:
                            errors.append(f"Group {i}, bar {j}: missing '{f}'")
    return errors


def validate_stacked_bar(data):
    errors = []
    for f in STACKED_BAR_SCHEMA["required"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "bars" in data:
        for i, b in enumerate(data["bars"]):
            for f in STACKED_BAR_SCHEMA["bar_item"]["required"]:
                if f not in b:
                    errors.append(f"Bar {i}: missing field '{f}'")
            if "segments" in b:
                for j, seg in enumerate(b["segments"]):
                    for f in STACKED_BAR_SCHEMA["segment_item"]["required"]:
                        if f not in seg:
                            errors.append(f"Bar {i}, segment {j}: missing '{f}'")
    return errors


def validate_box_plot(data):
    errors = []
    for f in BOX_PLOT_SCHEMA["required"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "boxes" in data:
        for i, box in enumerate(data["boxes"]):
            for f in BOX_PLOT_SCHEMA["box_item"]["required"]:
                if f not in box:
                    errors.append(f"Box {i}: missing field '{f}'")
            if "stats" in box:
                for f in BOX_PLOT_SCHEMA["box_item"]["stats"]["required"]:
                    if f not in box["stats"]:
                        errors.append(f"Box {i} stats: missing '{f}'")
    return errors


def validate_contour_map(data):
    errors = []
    for f in CONTOUR_MAP_SCHEMA["required"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    return errors


def validate_pie_chart(data):
    errors = []
    for f in PIE_CHART_SCHEMA["required"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "slices" in data:
        for i, s in enumerate(data["slices"]):
            for f in PIE_CHART_SCHEMA["slice_item"]["required"]:
                if f not in s:
                    errors.append(f"Slice {i}: missing field '{f}'")
        total = sum(s.get("percentage", 0) for s in data["slices"])
        if abs(total - 100.0) > 0.5:
            errors.append(f"Slice percentages sum to {total:.1f}, expected ~100.0")
    return errors


VALIDATORS = {
    "scatter": validate_scatter,
    "plain_bar": validate_plain_bar,
    "grouped_bar": validate_grouped_bar,
    "stacked_bar": validate_stacked_bar,
    "box_plot": validate_box_plot,
    "contour_map": validate_contour_map,
    "pie_chart": validate_pie_chart,
}


def validate(data, chart_type):
    """Validate extracted data against the appropriate schema."""
    if chart_type not in VALIDATORS:
        return [f"Unknown chart type: {chart_type}"]
    return VALIDATORS[chart_type](data)


def parse_ground_truth_md(md_path):
    """Extract JSON block from a ground truth .md file."""
    text = Path(md_path).read_text(encoding="utf-8")
    match = re.search(r"```json\s*\n(.*?)\n```", text, re.DOTALL)
    if not match:
        raise ValueError(f"No JSON block found in {md_path}")
    return json.loads(match.group(1))
