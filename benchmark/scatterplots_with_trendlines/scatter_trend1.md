# Ground Truth: scatter_trend1

## Plot Configuration

- **Plot type**: Scatter plot with multiple trend lines
- **Trend line type**: Linear
- **Number of series**: 3
- **Points per series**: 8
- **R² shown on plot**: Yes
- **numpy seed**: 401

## Data

```json
{
  "title": "Effect of pH on REE Extraction with Linear Fitting",
  "x_label": "pH",
  "y_label": "Extraction Efficiency (%)",
  "y_axis_range": [
    0,
    100
  ],
  "trend_type": "linear",
  "series": [
    {
      "name": "D2EHPA",
      "points": [
        {
          "x": 1.037,
          "y": 44.14
        },
        {
          "x": 1.546,
          "y": 42.05
        },
        {
          "x": 2.148,
          "y": 51.02
        },
        {
          "x": 2.649,
          "y": 53.42
        },
        {
          "x": 3.322,
          "y": 64.21
        },
        {
          "x": 3.814,
          "y": 78.52
        },
        {
          "x": 4.446,
          "y": 83.12
        },
        {
          "x": 5.0,
          "y": 90.93
        }
      ],
      "trend_coefficients": [
        13.094252,
        24.205691
      ],
      "r_squared": 0.9547
    },
    {
      "name": "Cyanex 272",
      "points": [
        {
          "x": 1.015,
          "y": 42.62
        },
        {
          "x": 1.525,
          "y": 54.1
        },
        {
          "x": 2.065,
          "y": 59.56
        },
        {
          "x": 2.714,
          "y": 57.22
        },
        {
          "x": 3.256,
          "y": 71.41
        },
        {
          "x": 3.888,
          "y": 63.67
        },
        {
          "x": 4.405,
          "y": 75.49
        },
        {
          "x": 4.938,
          "y": 76.88
        }
      ],
      "trend_coefficients": [
        7.733663,
        39.605302
      ],
      "r_squared": 0.8518
    },
    {
      "name": "PC88A",
      "points": [
        {
          "x": 1.032,
          "y": 25.5
        },
        {
          "x": 1.551,
          "y": 45.83
        },
        {
          "x": 2.079,
          "y": 36.11
        },
        {
          "x": 2.718,
          "y": 49.27
        },
        {
          "x": 3.334,
          "y": 60.27
        },
        {
          "x": 3.778,
          "y": 65.49
        },
        {
          "x": 4.357,
          "y": 76.99
        },
        {
          "x": 5.0,
          "y": 80.28
        }
      ],
      "trend_coefficients": [
        13.427177,
        14.939406
      ],
      "r_squared": 0.9315
    }
  ]
}
```

## Notes

Color scheme: tab10 with 3 colors. Marker styles: D2EHPA: 'o', Cyanex 272: 's', PC88A: '^'. Trend lines: solid, linewidth 1.8, alpha 0.8. R² annotations shown near end of each trend line. Horizontal gridlines only (light gray, alpha 0.3). Legend placed at best location to avoid data overlap.
