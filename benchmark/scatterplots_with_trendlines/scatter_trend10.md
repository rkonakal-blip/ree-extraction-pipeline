# Ground Truth: scatter_trend10

## Plot Configuration

- **Plot type**: Scatter plot with multiple trend lines
- **Trend line type**: Polynomial degree 2
- **Number of series**: 3
- **Points per series**: 8
- **R² shown on plot**: Yes
- **numpy seed**: 410

## Data

```json
{
  "title": "Separation Factor vs pH for REE Pairs",
  "x_label": "pH",
  "y_label": "Separation Factor (\u03b1)",
  "y_axis_range": [
    0,
    5
  ],
  "trend_type": "polynomial_deg2",
  "series": [
    {
      "name": "D2EHPA",
      "points": [
        {
          "x": 1.062,
          "y": 1.01
        },
        {
          "x": 1.594,
          "y": 1.71
        },
        {
          "x": 2.217,
          "y": 2.57
        },
        {
          "x": 2.765,
          "y": 3.36
        },
        {
          "x": 3.351,
          "y": 3.57
        },
        {
          "x": 3.92,
          "y": 3.52
        },
        {
          "x": 4.373,
          "y": 3.43
        },
        {
          "x": 5.0,
          "y": 3.46
        }
      ],
      "trend_coefficients": [
        -0.304041,
        2.449249,
        -1.300877
      ],
      "r_squared": 0.9813
    },
    {
      "name": "Cyanex 272",
      "points": [
        {
          "x": 1.056,
          "y": 1.07
        },
        {
          "x": 1.607,
          "y": 1.57
        },
        {
          "x": 2.069,
          "y": 2.44
        },
        {
          "x": 2.642,
          "y": 3.09
        },
        {
          "x": 3.262,
          "y": 2.96
        },
        {
          "x": 3.902,
          "y": 3.11
        },
        {
          "x": 4.463,
          "y": 3.06
        },
        {
          "x": 4.965,
          "y": 2.94
        }
      ],
      "trend_coefficients": [
        -0.281548,
        2.163751,
        -0.946736
      ],
      "r_squared": 0.9553
    },
    {
      "name": "PC88A",
      "points": [
        {
          "x": 1.0,
          "y": 1.13
        },
        {
          "x": 1.604,
          "y": 1.55
        },
        {
          "x": 2.154,
          "y": 2.13
        },
        {
          "x": 2.774,
          "y": 3.19
        },
        {
          "x": 3.273,
          "y": 3.4
        },
        {
          "x": 3.884,
          "y": 3.76
        },
        {
          "x": 4.436,
          "y": 3.57
        },
        {
          "x": 4.966,
          "y": 3.5
        }
      ],
      "trend_coefficients": [
        -0.233731,
        2.069797,
        -0.940265
      ],
      "r_squared": 0.9611
    }
  ]
}
```

## Notes

Color scheme: Set2 with 3 colors. Marker styles: D2EHPA: 'o', Cyanex 272: 's', PC88A: '^'. Trend lines: solid, linewidth 1.8, alpha 0.8. R² annotations shown near end of each trend line. Horizontal gridlines only (light gray, alpha 0.3). Legend placed at best location to avoid data overlap.
