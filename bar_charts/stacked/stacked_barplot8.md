# Ground Truth: stacked_barplot8

## Plot Configuration

- **Plot type**: Stacked bar chart
- **Orientation**: Vertical
- **Number of groups**: 4
- **Number of segments**: 6
- **Y-axis metric**: Elemental Composition (%)
- **numpy seed**: 208

## Data

```json
{
  "title": "Elemental Composition of Ore Samples",
  "x_label": "Ore Sample",
  "y_label": "Elemental Composition (%)",
  "y_axis_range": [
    0,
    100
  ],
  "segments": [
    "La",
    "Ce",
    "Nd",
    "Pr",
    "Sm",
    "Others"
  ],
  "bars": [
    {
      "label": "S1",
      "segments": [
        {
          "name": "La",
          "value": 4.5,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Ce",
          "value": 23.9,
          "cumulative_bottom": 4.5
        },
        {
          "name": "Nd",
          "value": 3.4,
          "cumulative_bottom": 28.4
        },
        {
          "name": "Pr",
          "value": 28.1,
          "cumulative_bottom": 31.8
        },
        {
          "name": "Sm",
          "value": 28.6,
          "cumulative_bottom": 59.9
        },
        {
          "name": "Others",
          "value": 11.5,
          "cumulative_bottom": 88.5
        }
      ]
    },
    {
      "label": "S2",
      "segments": [
        {
          "name": "La",
          "value": 9.5,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Ce",
          "value": 7.4,
          "cumulative_bottom": 9.5
        },
        {
          "name": "Nd",
          "value": 10.6,
          "cumulative_bottom": 16.9
        },
        {
          "name": "Pr",
          "value": 24.7,
          "cumulative_bottom": 27.5
        },
        {
          "name": "Sm",
          "value": 32.7,
          "cumulative_bottom": 52.2
        },
        {
          "name": "Others",
          "value": 15.1,
          "cumulative_bottom": 84.9
        }
      ]
    },
    {
      "label": "S3",
      "segments": [
        {
          "name": "La",
          "value": 16.4,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Ce",
          "value": 7.5,
          "cumulative_bottom": 16.4
        },
        {
          "name": "Nd",
          "value": 5.9,
          "cumulative_bottom": 23.9
        },
        {
          "name": "Pr",
          "value": 17.9,
          "cumulative_bottom": 29.8
        },
        {
          "name": "Sm",
          "value": 27.1,
          "cumulative_bottom": 47.7
        },
        {
          "name": "Others",
          "value": 25.2,
          "cumulative_bottom": 74.8
        }
      ]
    },
    {
      "label": "S4",
      "segments": [
        {
          "name": "La",
          "value": 11.8,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Ce",
          "value": 13.6,
          "cumulative_bottom": 11.8
        },
        {
          "name": "Nd",
          "value": 13.7,
          "cumulative_bottom": 25.4
        },
        {
          "name": "Pr",
          "value": 28.5,
          "cumulative_bottom": 39.1
        },
        {
          "name": "Sm",
          "value": 8.4,
          "cumulative_bottom": 67.6
        },
        {
          "name": "Others",
          "value": 24.0,
          "cumulative_bottom": 76.0
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: tab10 with 6 colors. Horizontal gridlines only. Legend displayed upper right with light gray border frame. All bars sum to 100%.
