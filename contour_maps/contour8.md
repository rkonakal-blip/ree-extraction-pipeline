# Ground Truth: contour8

## Plot Configuration

- **Plot type**: Contour map
- **Style**: Line only
- **Z metric**: Extraction Efficiency (%)
- **X variable**: pH (1.5–4.5)
- **Y variable**: A:O Ratio (0.5–3.0)
- **Grid resolution**: 50 × 50
- **Number of contour levels**: 8
- **Colormap**: None (black lines)
- **Contour line labels shown**: Yes
- **numpy seed**: 608

## Data

```json
{
  "title": "Contour Lines: pH and A:O Ratio Effect on Sm Extraction",
  "x_label": "pH",
  "y_label": "A:O Ratio",
  "colorbar_label": null,
  "x_range": [
    1.5,
    4.5
  ],
  "y_range": [
    0.5,
    3.0
  ],
  "z_range": [
    30.72,
    94.66
  ],
  "grid_resolution": 50,
  "polynomial_coefficients": {
    "a0": -68.3,
    "a1": 72.1,
    "a2": 38.6,
    "a3": 1.8,
    "a4": -11.5,
    "a5": -10.3
  },
  "contour_levels": [
    24.0,
    32.0,
    40.0,
    48.0,
    56.0,
    64.0,
    72.0,
    80.0,
    88.0,
    96.0
  ],
  "optimal_point": {
    "x": 3.1531,
    "y": 2.2857,
    "z": 94.66
  }
}
```

## Notes

Black contour lines, no fill. Noise std: 1.3. Line-only contour with inline labels (linewidth 1.0).
