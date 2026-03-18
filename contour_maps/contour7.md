# Ground Truth: contour7

## Plot Configuration

- **Plot type**: Contour map
- **Style**: Line only
- **Z metric**: Recovery (%)
- **X variable**: Temperature (°C) (20–70)
- **Y variable**: Contact Time (min) (5–60)
- **Grid resolution**: 50 × 50
- **Number of contour levels**: 10
- **Colormap**: None (black lines)
- **Contour line labels shown**: Yes
- **numpy seed**: 607

## Data

```json
{
  "title": "Contour Lines: Temperature and Contact Time Effect on Recovery",
  "x_label": "Temperature (\u00b0C)",
  "y_label": "Contact Time (min)",
  "colorbar_label": null,
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
    "a0": -135.2,
    "a1": 6.85,
    "a2": 4.12,
    "a3": 0.008,
    "a4": -0.068,
    "a5": -0.055
  },
  "contour_levels": [
    0.0,
    10.0,
    20.0,
    30.0,
    40.0,
    50.0,
    60.0,
    70.0,
    80.0,
    90.0,
    100.0
  ],
  "optimal_point": {
    "x": 52.6531,
    "y": 17.3469,
    "z": 100.0
  }
}
```

## Notes

Black contour lines, no fill. Noise std: 1.8. Line-only contour with inline labels (linewidth 1.0).
