# Ground Truth: contour5

## Plot Configuration

- **Plot type**: Contour map
- **Style**: Filled
- **Z metric**: Distribution Ratio (D)
- **X variable**: pH (1.0–5.0)
- **Y variable**: Temperature (°C) (20–60)
- **Grid resolution**: 50 × 50
- **Number of contour levels**: 10
- **Colormap**: YlOrRd
- **Contour line labels shown**: No
- **numpy seed**: 605

## Data

```json
{
  "title": "Distribution Ratio of Nd vs pH and Temperature",
  "x_label": "pH",
  "y_label": "Temperature (\u00b0C)",
  "colorbar_label": "Distribution Ratio (D)",
  "x_range": [
    1.0,
    5.0
  ],
  "y_range": [
    20,
    60
  ],
  "z_range": [
    0.0,
    20.0
  ],
  "grid_resolution": 50,
  "polynomial_coefficients": {
    "a0": -25.8,
    "a1": 12.3,
    "a2": 0.68,
    "a3": 0.05,
    "a4": -1.72,
    "a5": -0.008
  },
  "contour_levels": [
    0.0,
    2.0,
    4.0,
    6.0,
    8.0,
    10.0,
    12.0,
    14.0,
    16.0,
    18.0,
    20.0
  ],
  "optimal_point": {
    "x": 4.2653,
    "y": 46.9388,
    "z": 20.0
  }
}
```

## Notes

Colormap: YlOrRd. Noise std: 0.3. Filled contour with colorbar.
