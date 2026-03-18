# Ground Truth: contour1

## Plot Configuration

- **Plot type**: Contour map
- **Style**: Filled
- **Z metric**: Extraction Efficiency (%)
- **X variable**: pH (1.0–4.0)
- **Y variable**: Extractant Concentration (M) (0.1–2.0)
- **Grid resolution**: 50 × 50
- **Number of contour levels**: 10
- **Colormap**: viridis
- **Contour line labels shown**: No
- **numpy seed**: 601

## Data

```json
{
  "title": "Effect of pH and Extractant Concentration on Nd Extraction",
  "x_label": "pH",
  "y_label": "Extractant Concentration (M)",
  "colorbar_label": "Extraction Efficiency (%)",
  "x_range": [
    1.0,
    4.0
  ],
  "y_range": [
    0.1,
    2.0
  ],
  "z_range": [
    11.29,
    81.46
  ],
  "grid_resolution": 50,
  "polynomial_coefficients": {
    "a0": -45.3,
    "a1": 62.8,
    "a2": 55.4,
    "a3": 2.7,
    "a4": -12.3,
    "a5": -22.1
  },
  "contour_levels": [
    8.0,
    16.0,
    24.0,
    32.0,
    40.0,
    48.0,
    56.0,
    64.0,
    72.0,
    80.0,
    88.0
  ],
  "optimal_point": {
    "x": 2.7143,
    "y": 1.4184,
    "z": 81.46
  }
}
```

## Notes

Colormap: viridis. Noise std: 1.5. Filled contour with colorbar.
