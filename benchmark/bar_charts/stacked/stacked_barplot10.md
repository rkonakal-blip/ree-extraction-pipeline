# Ground Truth: stacked_barplot10

## Plot Configuration

- **Plot type**: Stacked bar chart
- **Orientation**: Horizontal
- **Number of groups**: 6
- **Number of segments**: 3
- **Y-axis metric**: Concentration (mg/L)
- **numpy seed**: 210

## Data

```json
{
  "title": "REE Concentration Distribution After Processing",
  "x_label": "REE Element",
  "y_label": "Concentration (mg/L)",
  "y_axis_range": [
    0,
    300
  ],
  "segments": [
    "Extracted fraction",
    "Aqueous residual",
    "Precipitated"
  ],
  "bars": [
    {
      "label": "La",
      "segments": [
        {
          "name": "Extracted fraction",
          "value": 27.7,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Aqueous residual",
          "value": 65.0,
          "cumulative_bottom": 27.7
        },
        {
          "name": "Precipitated",
          "value": 43.3,
          "cumulative_bottom": 92.7
        }
      ]
    },
    {
      "label": "Ce",
      "segments": [
        {
          "name": "Extracted fraction",
          "value": 10.8,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Aqueous residual",
          "value": 63.7,
          "cumulative_bottom": 10.8
        },
        {
          "name": "Precipitated",
          "value": 63.5,
          "cumulative_bottom": 74.5
        }
      ]
    },
    {
      "label": "Pr",
      "segments": [
        {
          "name": "Extracted fraction",
          "value": 72.7,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Aqueous residual",
          "value": 20.7,
          "cumulative_bottom": 72.7
        },
        {
          "name": "Precipitated",
          "value": 90.4,
          "cumulative_bottom": 93.4
        }
      ]
    },
    {
      "label": "Nd",
      "segments": [
        {
          "name": "Extracted fraction",
          "value": 47.8,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Aqueous residual",
          "value": 32.1,
          "cumulative_bottom": 47.8
        },
        {
          "name": "Precipitated",
          "value": 48.6,
          "cumulative_bottom": 79.9
        }
      ]
    },
    {
      "label": "Sm",
      "segments": [
        {
          "name": "Extracted fraction",
          "value": 67.0,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Aqueous residual",
          "value": 107.1,
          "cumulative_bottom": 67.0
        },
        {
          "name": "Precipitated",
          "value": 88.4,
          "cumulative_bottom": 174.1
        }
      ]
    },
    {
      "label": "Eu",
      "segments": [
        {
          "name": "Extracted fraction",
          "value": 12.9,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Aqueous residual",
          "value": 113.4,
          "cumulative_bottom": 12.9
        },
        {
          "name": "Precipitated",
          "value": 121.4,
          "cumulative_bottom": 126.3
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: tab10 with 3 colors. Vertical gridlines only. Legend displayed upper right with light gray border frame.
