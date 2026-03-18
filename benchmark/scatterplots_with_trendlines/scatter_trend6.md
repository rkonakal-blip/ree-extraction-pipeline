# Ground Truth: scatter_trend6

## Plot Configuration

- **Plot type**: Scatter plot with multiple trend lines
- **Trend line type**: Polynomial degree 2
- **Number of series**: 2
- **Points per series**: 10
- **R² shown on plot**: Yes
- **numpy seed**: 406

## Data

```json
{
  "title": "Polynomial Fit of Extraction Efficiency vs pH",
  "x_label": "pH",
  "y_label": "Extraction Efficiency (%)",
  "y_axis_range": [
    0,
    100
  ],
  "trend_type": "polynomial_deg2",
  "series": [
    {
      "name": "La",
      "points": [
        {
          "x": 1.067,
          "y": 41.64
        },
        {
          "x": 1.451,
          "y": 53.92
        },
        {
          "x": 1.872,
          "y": 64.48
        },
        {
          "x": 2.383,
          "y": 79.03
        },
        {
          "x": 2.724,
          "y": 81.52
        },
        {
          "x": 3.274,
          "y": 89.43
        },
        {
          "x": 3.691,
          "y": 87.85
        },
        {
          "x": 4.119,
          "y": 81.38
        },
        {
          "x": 4.612,
          "y": 74.87
        },
        {
          "x": 5.0,
          "y": 61.84
        }
      ],
      "trend_coefficients": [
        -8.968856,
        60.438038,
        -14.535376
      ],
      "r_squared": 0.9873
    },
    {
      "name": "Nd",
      "points": [
        {
          "x": 1.028,
          "y": 43.56
        },
        {
          "x": 1.414,
          "y": 58.25
        },
        {
          "x": 1.869,
          "y": 64.5
        },
        {
          "x": 2.371,
          "y": 77.29
        },
        {
          "x": 2.757,
          "y": 83.63
        },
        {
          "x": 3.147,
          "y": 87.33
        },
        {
          "x": 3.607,
          "y": 90.67
        },
        {
          "x": 4.095,
          "y": 92.89
        },
        {
          "x": 4.594,
          "y": 89.58
        },
        {
          "x": 4.939,
          "y": 73.06
        }
      ],
      "trend_coefficients": [
        -6.823644,
        50.06014,
        -1.591696
      ],
      "r_squared": 0.9556
    }
  ]
}
```

## Notes

Color scheme: tab10 with 2 colors. Marker styles: La: 'o', Nd: 's'. Trend lines: solid, linewidth 1.8, alpha 0.8. R² annotations shown near end of each trend line. Horizontal gridlines only (light gray, alpha 0.3). Legend placed at best location to avoid data overlap.
