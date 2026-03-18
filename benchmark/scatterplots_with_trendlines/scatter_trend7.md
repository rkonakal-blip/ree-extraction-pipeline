# Ground Truth: scatter_trend7

## Plot Configuration

- **Plot type**: Scatter plot with multiple trend lines
- **Trend line type**: Polynomial degree 2
- **Number of series**: 3
- **Points per series**: 8
- **R² shown on plot**: No
- **numpy seed**: 407

## Data

```json
{
  "title": "Distribution Ratio vs Temperature (Polynomial Fit)",
  "x_label": "Temperature (\u00b0C)",
  "y_label": "Distribution Ratio (D)",
  "y_axis_range": [
    0,
    20
  ],
  "trend_type": "polynomial_deg2",
  "series": [
    {
      "name": "D2EHPA",
      "points": [
        {
          "x": 20.705,
          "y": 8.12
        },
        {
          "x": 27.15,
          "y": 9.47
        },
        {
          "x": 33.731,
          "y": 11.71
        },
        {
          "x": 41.544,
          "y": 14.09
        },
        {
          "x": 49.262,
          "y": 16.71
        },
        {
          "x": 55.042,
          "y": 16.92
        },
        {
          "x": 62.439,
          "y": 15.55
        },
        {
          "x": 69.94,
          "y": 15.1
        }
      ],
      "trend_coefficients": [
        -0.00648,
        0.749215,
        -5.43404
      ],
      "r_squared": null
    },
    {
      "name": "Cyanex 272",
      "points": [
        {
          "x": 20.997,
          "y": 9.34
        },
        {
          "x": 27.25,
          "y": 9.63
        },
        {
          "x": 34.451,
          "y": 13.89
        },
        {
          "x": 41.892,
          "y": 13.78
        },
        {
          "x": 47.993,
          "y": 15.26
        },
        {
          "x": 56.239,
          "y": 16.63
        },
        {
          "x": 62.605,
          "y": 16.56
        },
        {
          "x": 70.0,
          "y": 18.11
        }
      ],
      "trend_coefficients": [
        -0.002372,
        0.393954,
        1.809795
      ],
      "r_squared": null
    },
    {
      "name": "PC88A",
      "points": [
        {
          "x": 20.634,
          "y": 9.03
        },
        {
          "x": 27.6,
          "y": 9.59
        },
        {
          "x": 34.368,
          "y": 13.02
        },
        {
          "x": 42.097,
          "y": 13.05
        },
        {
          "x": 49.016,
          "y": 11.89
        },
        {
          "x": 56.33,
          "y": 13.97
        },
        {
          "x": 63.596,
          "y": 14.31
        },
        {
          "x": 70.0,
          "y": 15.48
        }
      ],
      "trend_coefficients": [
        -0.001194,
        0.225787,
        5.064378
      ],
      "r_squared": null
    }
  ]
}
```

## Notes

Color scheme: Set1 with 3 colors. Marker styles: D2EHPA: 'o', Cyanex 272: 's', PC88A: '^'. Trend lines: solid, linewidth 1.8, alpha 0.8. Horizontal gridlines only (light gray, alpha 0.3). Legend placed at best location to avoid data overlap.
