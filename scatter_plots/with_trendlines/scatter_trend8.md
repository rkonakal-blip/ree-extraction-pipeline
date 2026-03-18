# Ground Truth: scatter_trend8

## Plot Configuration

- **Plot type**: Scatter plot with multiple trend lines
- **Trend line type**: Polynomial degree 2
- **Number of series**: 2
- **Points per series**: 9
- **R² shown on plot**: Yes
- **numpy seed**: 408

## Data

```json
{
  "title": "Extraction Efficiency vs Extractant Concentration",
  "x_label": "Extractant Concentration (M)",
  "y_label": "Extraction Efficiency (%)",
  "y_axis_range": [
    10,
    100
  ],
  "trend_type": "polynomial_deg2",
  "series": [
    {
      "name": "La",
      "points": [
        {
          "x": 0.05,
          "y": 25.93
        },
        {
          "x": 0.32,
          "y": 38.63
        },
        {
          "x": 0.575,
          "y": 57.12
        },
        {
          "x": 0.78,
          "y": 61.48
        },
        {
          "x": 1.018,
          "y": 68.02
        },
        {
          "x": 1.251,
          "y": 80.25
        },
        {
          "x": 1.544,
          "y": 81.82
        },
        {
          "x": 1.786,
          "y": 88.73
        },
        {
          "x": 1.962,
          "y": 81.52
        }
      ],
      "trend_coefficients": [
        -17.716694,
        66.983504,
        21.44672
      ],
      "r_squared": 0.9824
    },
    {
      "name": "Ce",
      "points": [
        {
          "x": 0.067,
          "y": 17.07
        },
        {
          "x": 0.302,
          "y": 42.45
        },
        {
          "x": 0.517,
          "y": 54.53
        },
        {
          "x": 0.809,
          "y": 70.12
        },
        {
          "x": 1.018,
          "y": 73.51
        },
        {
          "x": 1.241,
          "y": 75.64
        },
        {
          "x": 1.542,
          "y": 73.23
        },
        {
          "x": 1.773,
          "y": 77.22
        },
        {
          "x": 1.973,
          "y": 79.47
        }
      ],
      "trend_coefficients": [
        -27.464895,
        83.654227,
        16.374219
      ],
      "r_squared": 0.962
    }
  ]
}
```

## Notes

Color scheme: Paired with 2 colors. Marker styles: La: 'o', Ce: 's'. Trend lines: solid, linewidth 1.8, alpha 0.8. R² annotations shown near end of each trend line. Horizontal gridlines only (light gray, alpha 0.3). Legend placed at best location to avoid data overlap.
