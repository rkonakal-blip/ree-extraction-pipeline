# Ground Truth: scatter_trend3

## Plot Configuration

- **Plot type**: Scatter plot with multiple trend lines
- **Trend line type**: Linear
- **Number of series**: 4
- **Points per series**: 7
- **R² shown on plot**: No
- **numpy seed**: 403

## Data

```json
{
  "title": "Temperature Effect on REE Extraction Efficiency",
  "x_label": "Temperature (\u00b0C)",
  "y_label": "Extraction Efficiency (%)",
  "y_axis_range": [
    30,
    100
  ],
  "trend_type": "linear",
  "series": [
    {
      "name": "La",
      "points": [
        {
          "x": 20.0,
          "y": 45.99
        },
        {
          "x": 28.496,
          "y": 49.8
        },
        {
          "x": 36.856,
          "y": 63.92
        },
        {
          "x": 44.735,
          "y": 69.29
        },
        {
          "x": 52.938,
          "y": 76.32
        },
        {
          "x": 61.773,
          "y": 78.84
        },
        {
          "x": 70.0,
          "y": 86.07
        }
      ],
      "trend_coefficients": [
        0.818862,
        30.350559
      ],
      "r_squared": null
    },
    {
      "name": "Ce",
      "points": [
        {
          "x": 20.0,
          "y": 61.99
        },
        {
          "x": 27.787,
          "y": 67.47
        },
        {
          "x": 36.751,
          "y": 65.54
        },
        {
          "x": 44.104,
          "y": 77.13
        },
        {
          "x": 53.887,
          "y": 73.76
        },
        {
          "x": 60.811,
          "y": 83.96
        },
        {
          "x": 70.0,
          "y": 87.28
        }
      ],
      "trend_coefficients": [
        0.497385,
        51.61135
      ],
      "r_squared": null
    },
    {
      "name": "Nd",
      "points": [
        {
          "x": 20.0,
          "y": 49.52
        },
        {
          "x": 27.763,
          "y": 55.98
        },
        {
          "x": 37.31,
          "y": 65.55
        },
        {
          "x": 45.076,
          "y": 81.54
        },
        {
          "x": 53.317,
          "y": 85.29
        },
        {
          "x": 62.294,
          "y": 90.1
        },
        {
          "x": 69.201,
          "y": 89.97
        }
      ],
      "trend_coefficients": [
        0.902742,
        33.374479
      ],
      "r_squared": null
    },
    {
      "name": "Pr",
      "points": [
        {
          "x": 20.539,
          "y": 59.83
        },
        {
          "x": 29.138,
          "y": 64.5
        },
        {
          "x": 37.447,
          "y": 75.03
        },
        {
          "x": 44.937,
          "y": 70.61
        },
        {
          "x": 53.325,
          "y": 69.95
        },
        {
          "x": 62.25,
          "y": 79.35
        },
        {
          "x": 70.0,
          "y": 84.84
        }
      ],
      "trend_coefficients": [
        0.434454,
        52.301691
      ],
      "r_squared": null
    }
  ]
}
```

## Notes

Color scheme: tab10 with 4 colors. Marker styles: La: 'o', Ce: 's', Nd: '^', Pr: 'D'. Trend lines: solid, linewidth 1.8, alpha 0.8. Horizontal gridlines only (light gray, alpha 0.3). Legend placed at best location to avoid data overlap.
