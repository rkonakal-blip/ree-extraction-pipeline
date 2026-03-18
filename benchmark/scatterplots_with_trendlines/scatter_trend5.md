# Ground Truth: scatter_trend5

## Plot Configuration

- **Plot type**: Scatter plot with multiple trend lines
- **Trend line type**: Linear
- **Number of series**: 3
- **Points per series**: 8
- **R² shown on plot**: No
- **numpy seed**: 405

## Data

```json
{
  "title": "REE Recovery vs Contact Time",
  "x_label": "Contact Time (min)",
  "y_label": "Recovery (%)",
  "y_axis_range": [
    40,
    100
  ],
  "trend_type": "linear",
  "series": [
    {
      "name": "D2EHPA",
      "points": [
        {
          "x": 5.443,
          "y": 57.12
        },
        {
          "x": 12.369,
          "y": 63.03
        },
        {
          "x": 20.026,
          "y": 62.71
        },
        {
          "x": 28.072,
          "y": 69.94
        },
        {
          "x": 35.588,
          "y": 70.33
        },
        {
          "x": 43.37,
          "y": 78.31
        },
        {
          "x": 52.69,
          "y": 84.19
        },
        {
          "x": 59.366,
          "y": 90.05
        }
      ],
      "trend_coefficients": [
        0.584995,
        53.172582
      ],
      "r_squared": null
    },
    {
      "name": "Cyanex 272",
      "points": [
        {
          "x": 5.255,
          "y": 56.44
        },
        {
          "x": 13.743,
          "y": 63.97
        },
        {
          "x": 20.207,
          "y": 64.23
        },
        {
          "x": 29.138,
          "y": 70.74
        },
        {
          "x": 37.136,
          "y": 78.33
        },
        {
          "x": 43.432,
          "y": 77.8
        },
        {
          "x": 52.297,
          "y": 80.07
        },
        {
          "x": 59.109,
          "y": 82.2
        }
      ],
      "trend_coefficients": [
        0.479809,
        56.109681
      ],
      "r_squared": null
    },
    {
      "name": "PC88A",
      "points": [
        {
          "x": 5.0,
          "y": 46.81
        },
        {
          "x": 12.354,
          "y": 50.09
        },
        {
          "x": 20.01,
          "y": 60.77
        },
        {
          "x": 28.888,
          "y": 65.95
        },
        {
          "x": 35.699,
          "y": 76.11
        },
        {
          "x": 43.872,
          "y": 82.54
        },
        {
          "x": 52.997,
          "y": 90.2
        },
        {
          "x": 59.662,
          "y": 99.5
        }
      ],
      "trend_coefficients": [
        0.969622,
        40.167523
      ],
      "r_squared": null
    }
  ]
}
```

## Notes

Color scheme: Set2 with 3 colors. Marker styles: D2EHPA: 'o', Cyanex 272: 's', PC88A: '^'. Trend lines: solid, linewidth 1.8, alpha 0.8. Horizontal gridlines only (light gray, alpha 0.3). Legend placed at best location to avoid data overlap.
