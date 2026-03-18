# Ground Truth: contour4

## Plot Configuration

- **Plot type**: Contour map
- **Style**: Filled
- **Z metric**: Extraction Efficiency (%)
- **X variable**: Extractant Concentration (M) (0.1–2.0)
- **Y variable**: A:O Ratio (0.5–3.0)
- **Grid resolution**: 50 × 50
- **Number of contour levels**: 8
- **Colormap**: coolwarm
- **Contour line labels shown**: No
- **numpy seed**: 604

## Data

```json
{
  "title": "Extraction Efficiency vs Extractant Concentration and A:O Ratio",
  "x_label": "Extractant Concentration (M)",
  "y_label": "A:O Ratio",
  "colorbar_label": "Extraction Efficiency (%)",
  "x_range": [
    0.1,
    2.0
  ],
  "y_range": [
    0.5,
    3.0
  ],
  "z_range": [
    0.0,
    69.73
  ],
  "grid_resolution": 50,
  "polynomial_coefficients": {
    "a0": -32.6,
    "a1": 78.3,
    "a2": 42.5,
    "a3": 5.1,
    "a4": -33.7,
    "a5": -11.2
  },
  "contour_levels": [
    0.0,
    8.0,
    16.0,
    24.0,
    32.0,
    40.0,
    48.0,
    56.0,
    64.0,
    72.0
  ],
  "optimal_point": {
    "x": 1.302,
    "y": 1.9796,
    "z": 69.73
  }
}
```

## Notes

Colormap: coolwarm. Noise std: 1.5. Filled contour with colorbar.
