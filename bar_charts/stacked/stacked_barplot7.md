# Ground Truth: stacked_barplot7

## Plot Configuration

- **Plot type**: Stacked bar chart
- **Orientation**: Vertical
- **Number of groups**: 5
- **Number of segments**: 3
- **Y-axis metric**: Species Distribution (%)
- **numpy seed**: 207

## Data

```json
{
  "title": "Species Distribution vs Aqueous pH",
  "x_label": "Aqueous pH",
  "y_label": "Species Distribution (%)",
  "y_axis_range": [
    0,
    100
  ],
  "segments": [
    "Free ion",
    "Mono-complex",
    "Di-complex"
  ],
  "bars": [
    {
      "label": "1",
      "segments": [
        {
          "name": "Free ion",
          "value": 37.7,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Mono-complex",
          "value": 28.4,
          "cumulative_bottom": 37.7
        },
        {
          "name": "Di-complex",
          "value": 33.9,
          "cumulative_bottom": 66.1
        }
      ]
    },
    {
      "label": "2",
      "segments": [
        {
          "name": "Free ion",
          "value": 24.5,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Mono-complex",
          "value": 40.6,
          "cumulative_bottom": 24.5
        },
        {
          "name": "Di-complex",
          "value": 34.9,
          "cumulative_bottom": 65.1
        }
      ]
    },
    {
      "label": "3",
      "segments": [
        {
          "name": "Free ion",
          "value": 37.7,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Mono-complex",
          "value": 6.5,
          "cumulative_bottom": 37.7
        },
        {
          "name": "Di-complex",
          "value": 55.8,
          "cumulative_bottom": 44.2
        }
      ]
    },
    {
      "label": "4",
      "segments": [
        {
          "name": "Free ion",
          "value": 7.0,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Mono-complex",
          "value": 13.4,
          "cumulative_bottom": 7.0
        },
        {
          "name": "Di-complex",
          "value": 79.6,
          "cumulative_bottom": 20.4
        }
      ]
    },
    {
      "label": "5",
      "segments": [
        {
          "name": "Free ion",
          "value": 35.9,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Mono-complex",
          "value": 38.0,
          "cumulative_bottom": 35.9
        },
        {
          "name": "Di-complex",
          "value": 26.1,
          "cumulative_bottom": 73.9
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: Paired with 3 colors. Horizontal gridlines only. Legend displayed upper right with light gray border frame. All bars sum to 100%.
