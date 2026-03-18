# Ground Truth: scatter_trend4

## Plot Configuration

- **Plot type**: Scatter plot with multiple trend lines
- **Trend line type**: Linear
- **Number of series**: 2
- **Points per series**: 9
- **R² shown on plot**: Yes
- **numpy seed**: 404

## Data

```json
{
  "title": "Stripping Efficiency vs HCl Concentration",
  "x_label": "HCl Concentration (M)",
  "y_label": "Stripping Efficiency (%)",
  "y_axis_range": [
    20,
    100
  ],
  "trend_type": "linear",
  "series": [
    {
      "name": "D2EHPA",
      "points": [
        {
          "x": 0.524,
          "y": 34.94
        },
        {
          "x": 0.917,
          "y": 41.39
        },
        {
          "x": 1.43,
          "y": 40.75
        },
        {
          "x": 1.781,
          "y": 45.52
        },
        {
          "x": 2.187,
          "y": 61.8
        },
        {
          "x": 2.746,
          "y": 71.78
        },
        {
          "x": 3.121,
          "y": 78.73
        },
        {
          "x": 3.493,
          "y": 80.5
        },
        {
          "x": 3.998,
          "y": 80.12
        }
      ],
      "trend_coefficients": [
        15.395051,
        24.955129
      ],
      "r_squared": 0.9296
    },
    {
      "name": "PC88A",
      "points": [
        {
          "x": 0.568,
          "y": 46.47
        },
        {
          "x": 0.989,
          "y": 42.34
        },
        {
          "x": 1.409,
          "y": 55.28
        },
        {
          "x": 1.792,
          "y": 56.64
        },
        {
          "x": 2.221,
          "y": 62.47
        },
        {
          "x": 2.621,
          "y": 64.21
        },
        {
          "x": 3.077,
          "y": 70.41
        },
        {
          "x": 3.607,
          "y": 80.48
        },
        {
          "x": 3.951,
          "y": 82.53
        }
      ],
      "trend_coefficients": [
        11.638479,
        36.147264
      ],
      "r_squared": 0.9585
    }
  ]
}
```

## Notes

Color scheme: Paired with 2 colors. Marker styles: D2EHPA: 'o', PC88A: 's'. Trend lines: solid, linewidth 1.8, alpha 0.8. R² annotations shown near end of each trend line. Horizontal gridlines only (light gray, alpha 0.3). Legend placed at best location to avoid data overlap.
