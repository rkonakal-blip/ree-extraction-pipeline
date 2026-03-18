# Ground Truth: contour2

## Plot Configuration

- **Plot type**: Contour map
- **Style**: Filled
- **Z metric**: Extraction Efficiency (%)
- **X variable**: Temperature (°C) (20–70)
- **Y variable**: Contact Time (min) (5–60)
- **Grid resolution**: 50 × 50
- **Number of contour levels**: 12
- **Colormap**: RdYlGn
- **Contour line labels shown**: No
- **numpy seed**: 602

## Data

```json
{
  "title": "RSM Contour Plot: Temperature and Contact Time Effect on La Extraction",
  "x_label": "Temperature (\u00b0C)",
  "y_label": "Contact Time (min)",
  "colorbar_label": "Extraction Efficiency (%)",
  "x_range": [
    20,
    70
  ],
  "y_range": [
    5,
    60
  ],
  "z_range": [
    0.0,
    100.0
  ],
  "grid_resolution": 50,
  "polynomial_coefficients": {
    "a0": -120.7,
    "a1": 6.13,
    "a2": 3.82,
    "a3": 0.012,
    "a4": -0.063,
    "a5": -0.048
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
    72.0,
    80.0,
    88.0,
    96.0,
    104.0
  ],
  "optimal_point": {
    "x": 52.6531,
    "y": 20.7143,
    "z": 100.0
  }
}
```

## Notes

Colormap: RdYlGn. Noise std: 2.0. Filled contour with colorbar.
