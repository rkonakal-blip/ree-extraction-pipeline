# Ground Truth: scatter_trend9

## Plot Configuration

- **Plot type**: Scatter plot with multiple trend lines
- **Trend line type**: Polynomial degree 2
- **Number of series**: 4
- **Points per series**: 7
- **R² shown on plot**: No
- **numpy seed**: 409

## Data

```json
{
  "title": "REE Recovery Kinetics with Polynomial Fitting",
  "x_label": "Contact Time (min)",
  "y_label": "Recovery (%)",
  "y_axis_range": [
    20,
    100
  ],
  "trend_type": "polynomial_deg2",
  "series": [
    {
      "name": "La",
      "points": [
        {
          "x": 5.0,
          "y": 37.62
        },
        {
          "x": 15.024,
          "y": 48.35
        },
        {
          "x": 22.306,
          "y": 58.91
        },
        {
          "x": 33.258,
          "y": 70.66
        },
        {
          "x": 40.982,
          "y": 74.14
        },
        {
          "x": 50.301,
          "y": 77.36
        },
        {
          "x": 59.275,
          "y": 82.11
        }
      ],
      "trend_coefficients": [
        -0.011855,
        1.584683,
        29.189069
      ],
      "r_squared": null
    },
    {
      "name": "Ce",
      "points": [
        {
          "x": 5.71,
          "y": 39.72
        },
        {
          "x": 14.942,
          "y": 51.3
        },
        {
          "x": 22.905,
          "y": 59.23
        },
        {
          "x": 31.507,
          "y": 65.45
        },
        {
          "x": 40.964,
          "y": 71.24
        },
        {
          "x": 50.333,
          "y": 72.85
        },
        {
          "x": 60.0,
          "y": 79.56
        }
      ],
      "trend_coefficients": [
        -0.009254,
        1.29968,
        33.407647
      ],
      "r_squared": null
    },
    {
      "name": "Nd",
      "points": [
        {
          "x": 5.0,
          "y": 28.32
        },
        {
          "x": 13.797,
          "y": 40.97
        },
        {
          "x": 22.889,
          "y": 58.75
        },
        {
          "x": 32.799,
          "y": 71.95
        },
        {
          "x": 41.161,
          "y": 72.75
        },
        {
          "x": 49.963,
          "y": 73.61
        },
        {
          "x": 59.689,
          "y": 73.73
        }
      ],
      "trend_coefficients": [
        -0.024658,
        2.435285,
        15.335275
      ],
      "r_squared": null
    },
    {
      "name": "Pr",
      "points": [
        {
          "x": 5.0,
          "y": 40.61
        },
        {
          "x": 15.058,
          "y": 47.69
        },
        {
          "x": 22.372,
          "y": 57.84
        },
        {
          "x": 31.962,
          "y": 61.15
        },
        {
          "x": 41.526,
          "y": 65.73
        },
        {
          "x": 50.71,
          "y": 75.91
        },
        {
          "x": 59.349,
          "y": 73.02
        }
      ],
      "trend_coefficients": [
        -0.006846,
        1.079378,
        34.815034
      ],
      "r_squared": null
    }
  ]
}
```

## Notes

Color scheme: tab10 with 4 colors. Marker styles: La: 'o', Ce: 's', Nd: '^', Pr: 'D'. Trend lines: solid, linewidth 1.8, alpha 0.8. Horizontal gridlines only (light gray, alpha 0.3). Legend placed at best location to avoid data overlap.
