# Ground Truth: contour9

## Plot Configuration

- **Plot type**: Contour map
- **Style**: Overlaid
- **Z metric**: Extraction Efficiency (%)
- **X variable**: pH (1.0–4.0)
- **Y variable**: Temperature (°C) (25–65)
- **Grid resolution**: 50 × 50
- **Number of contour levels**: 12
- **Colormap**: viridis
- **Contour line labels shown**: Yes
- **numpy seed**: 609

## Data

```json
{
  "title": "RSM Surface: pH and Temperature Optimization for La Extraction",
  "x_label": "pH",
  "y_label": "Temperature (\u00b0C)",
  "colorbar_label": "Extraction Efficiency (%)",
  "x_range": [
    1.0,
    4.0
  ],
  "y_range": [
    25,
    65
  ],
  "z_range": [
    18.67,
    100.0
  ],
  "grid_resolution": 50,
  "polynomial_coefficients": {
    "a0": -178.5,
    "a1": 95.3,
    "a2": 5.92,
    "a3": 0.42,
    "a4": -17.2,
    "a5": -0.062
  },
  "contour_levels": [
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
    "x": 2.898,
    "y": 26.6327,
    "z": 100.0
  }
}
```

## Notes

Colormap: viridis. Noise std: 1.5. Filled contour with black contour lines overlaid (linewidth 0.8).
