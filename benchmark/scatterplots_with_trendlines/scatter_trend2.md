# Ground Truth: scatter_trend2

## Plot Configuration

- **Plot type**: Scatter plot with multiple trend lines
- **Trend line type**: Linear
- **Number of series**: 2
- **Points per series**: 10
- **R² shown on plot**: Yes
- **numpy seed**: 402

## Data

```json
{
  "title": "Distribution Ratio vs Extractant Concentration",
  "x_label": "Extractant Concentration (M)",
  "y_label": "Distribution Ratio (D)",
  "y_axis_range": [
    0,
    15
  ],
  "trend_type": "linear",
  "series": [
    {
      "name": "La",
      "points": [
        {
          "x": 0.05,
          "y": 1.94
        },
        {
          "x": 0.265,
          "y": 2.15
        },
        {
          "x": 0.469,
          "y": 4.4
        },
        {
          "x": 0.731,
          "y": 4.75
        },
        {
          "x": 0.916,
          "y": 6.42
        },
        {
          "x": 1.133,
          "y": 8.19
        },
        {
          "x": 1.382,
          "y": 9.16
        },
        {
          "x": 1.602,
          "y": 10.65
        },
        {
          "x": 1.771,
          "y": 11.09
        },
        {
          "x": 2.0,
          "y": 11.52
        }
      ],
      "trend_coefficients": [
        5.429151,
        1.424659
      ],
      "r_squared": 0.9791
    },
    {
      "name": "Nd",
      "points": [
        {
          "x": 0.066,
          "y": 3.24
        },
        {
          "x": 0.252,
          "y": 2.98
        },
        {
          "x": 0.485,
          "y": 4.1
        },
        {
          "x": 0.712,
          "y": 5.04
        },
        {
          "x": 0.923,
          "y": 6.22
        },
        {
          "x": 1.154,
          "y": 6.94
        },
        {
          "x": 1.336,
          "y": 7.29
        },
        {
          "x": 1.554,
          "y": 8.34
        },
        {
          "x": 1.811,
          "y": 8.85
        },
        {
          "x": 1.993,
          "y": 8.87
        }
      ],
      "trend_coefficients": [
        3.378246,
        2.712136
      ],
      "r_squared": 0.9726
    }
  ]
}
```

## Notes

Color scheme: Set1 with 2 colors. Marker styles: La: 'o', Nd: 's'. Trend lines: solid, linewidth 1.8, alpha 0.8. R² annotations shown near end of each trend line. Horizontal gridlines only (light gray, alpha 0.3). Legend placed at best location to avoid data overlap.
