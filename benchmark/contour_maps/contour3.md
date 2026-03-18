# Ground Truth: contour3

## Plot Configuration

- **Plot type**: Contour map
- **Style**: Filled
- **Z metric**: Recovery (%)
- **X variable**: pH (1.5–4.5)
- **Y variable**: Temperature (°C) (25–65)
- **Grid resolution**: 50 × 50
- **Number of contour levels**: 10
- **Colormap**: plasma
- **Contour line labels shown**: No
- **numpy seed**: 603

## Data

```json
{
  "title": "Recovery of Ce as a Function of pH and Temperature",
  "x_label": "pH",
  "y_label": "Temperature (\u00b0C)",
  "colorbar_label": "Recovery (%)",
  "x_range": [
    1.5,
    4.5
  ],
  "y_range": [
    25,
    65
  ],
  "z_range": [
    46.01,
    100.0
  ],
  "grid_resolution": 50,
  "polynomial_coefficients": {
    "a0": -185.4,
    "a1": 98.2,
    "a2": 5.73,
    "a3": 0.35,
    "a4": -15.8,
    "a5": -0.061
  },
  "contour_levels": [
    45.0,
    50.0,
    55.0,
    60.0,
    65.0,
    70.0,
    75.0,
    80.0,
    85.0,
    90.0,
    95.0,
    100.0
  ],
  "optimal_point": {
    "x": 2.9694,
    "y": 25.0,
    "z": 100.0
  }
}
```

## Notes

Colormap: plasma. Noise std: 1.8. Filled contour with colorbar.
