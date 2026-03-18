# Ground Truth: stacked_barplot3

## Plot Configuration

- **Plot type**: Stacked bar chart
- **Orientation**: Vertical
- **Number of groups**: 6
- **Number of segments**: 3
- **Y-axis metric**: Extraction Efficiency (%)
- **numpy seed**: 203

## Data

```json
{
  "title": "Extraction Fraction by Temperature",
  "x_label": "Temperature (\u00b0C)",
  "y_label": "Extraction Efficiency (%)",
  "y_axis_range": [
    0,
    100
  ],
  "segments": [
    "D2EHPA fraction",
    "PC88A fraction",
    "Residual"
  ],
  "bars": [
    {
      "label": "20",
      "segments": [
        {
          "name": "D2EHPA fraction",
          "value": 54.7,
          "cumulative_bottom": 0.0
        },
        {
          "name": "PC88A fraction",
          "value": 14.7,
          "cumulative_bottom": 54.7
        },
        {
          "name": "Residual",
          "value": 30.6,
          "cumulative_bottom": 69.4
        }
      ]
    },
    {
      "label": "30",
      "segments": [
        {
          "name": "D2EHPA fraction",
          "value": 34.6,
          "cumulative_bottom": 0.0
        },
        {
          "name": "PC88A fraction",
          "value": 52.1,
          "cumulative_bottom": 34.6
        },
        {
          "name": "Residual",
          "value": 13.3,
          "cumulative_bottom": 86.7
        }
      ]
    },
    {
      "label": "40",
      "segments": [
        {
          "name": "D2EHPA fraction",
          "value": 33.9,
          "cumulative_bottom": 0.0
        },
        {
          "name": "PC88A fraction",
          "value": 50.5,
          "cumulative_bottom": 33.9
        },
        {
          "name": "Residual",
          "value": 15.6,
          "cumulative_bottom": 84.4
        }
      ]
    },
    {
      "label": "50",
      "segments": [
        {
          "name": "D2EHPA fraction",
          "value": 35.1,
          "cumulative_bottom": 0.0
        },
        {
          "name": "PC88A fraction",
          "value": 29.2,
          "cumulative_bottom": 35.1
        },
        {
          "name": "Residual",
          "value": 35.7,
          "cumulative_bottom": 64.3
        }
      ]
    },
    {
      "label": "60",
      "segments": [
        {
          "name": "D2EHPA fraction",
          "value": 46.7,
          "cumulative_bottom": 0.0
        },
        {
          "name": "PC88A fraction",
          "value": 20.9,
          "cumulative_bottom": 46.7
        },
        {
          "name": "Residual",
          "value": 32.4,
          "cumulative_bottom": 67.6
        }
      ]
    },
    {
      "label": "70",
      "segments": [
        {
          "name": "D2EHPA fraction",
          "value": 28.7,
          "cumulative_bottom": 0.0
        },
        {
          "name": "PC88A fraction",
          "value": 34.9,
          "cumulative_bottom": 28.7
        },
        {
          "name": "Residual",
          "value": 36.4,
          "cumulative_bottom": 63.6
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: Set2 with 3 colors. Horizontal gridlines only. Legend displayed upper right with light gray border frame. All bars sum to 100%.
