# Ground Truth: contour6

## Plot Configuration

- **Plot type**: Contour map
- **Style**: Line only
- **Z metric**: Extraction Efficiency (%)
- **X variable**: pH (1.0–4.0)
- **Y variable**: Extractant Concentration (M) (0.1–2.0)
- **Grid resolution**: 50 × 50
- **Number of contour levels**: 8
- **Colormap**: None (black lines)
- **Contour line labels shown**: Yes
- **numpy seed**: 606

## Data

```json
{
  "title": "Contour Lines: pH and Extractant Concentration Effect on Pr Extraction",
  "x_label": "pH",
  "y_label": "Extractant Concentration (M)",
  "colorbar_label": null,
  "x_range": [
    1.0,
    4.0
  ],
  "y_range": [
    0.1,
    2.0
  ],
  "z_range": [
    7.42,
    85.01
  ],
  "grid_resolution": 50,
  "polynomial_coefficients": {
    "a0": -52.1,
    "a1": 65.4,
    "a2": 48.7,
    "a3": 3.2,
    "a4": -11.8,
    "a5": -18.9
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
    90.0
  ],
  "optimal_point": {
    "x": 2.898,
    "y": 1.5735,
    "z": 85.01
  }
}
```

## Notes

Black contour lines, no fill. Noise std: 1.2. Line-only contour with inline labels (linewidth 1.0).
