# Ground Truth: contour10

## Plot Configuration

- **Plot type**: Contour map
- **Style**: Overlaid
- **Z metric**: Recovery (%)
- **X variable**: Extractant Concentration (M) (0.1–2.0)
- **Y variable**: Contact Time (min) (5–60)
- **Grid resolution**: 50 × 50
- **Number of contour levels**: 10
- **Colormap**: RdYlGn
- **Contour line labels shown**: Yes
- **numpy seed**: 610

## Data

```json
{
  "title": "RSM Surface: Extractant Concentration and Contact Time for Ce Recovery",
  "x_label": "Extractant Concentration (M)",
  "y_label": "Contact Time (min)",
  "colorbar_label": "Recovery (%)",
  "x_range": [
    0.1,
    2.0
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
    "a0": -42.8,
    "a1": 82.5,
    "a2": 3.45,
    "a3": 0.95,
    "a4": -35.2,
    "a5": -0.046
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
    "x": 1.5735,
    "y": 26.3265,
    "z": 100.0
  }
}
```

## Notes

Colormap: RdYlGn. Noise std: 1.6. Filled contour with black contour lines overlaid (linewidth 0.8).
