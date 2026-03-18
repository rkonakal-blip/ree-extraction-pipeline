# Ground Truth: stacked_barplot5

## Plot Configuration

- **Plot type**: Stacked bar chart
- **Orientation**: Horizontal
- **Number of groups**: 4
- **Number of segments**: 3
- **Y-axis metric**: Mass (mg)
- **numpy seed**: 205

## Data

```json
{
  "title": "Mass Balance Across Leaching Stages",
  "x_label": "Leaching Stage",
  "y_label": "Mass (mg)",
  "y_axis_range": [
    0,
    500
  ],
  "segments": [
    "REE fraction",
    "Iron impurity",
    "Silica impurity"
  ],
  "bars": [
    {
      "label": "Stage 1",
      "segments": [
        {
          "name": "REE fraction",
          "value": 113.7,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Iron impurity",
          "value": 193.3,
          "cumulative_bottom": 113.7
        },
        {
          "name": "Silica impurity",
          "value": 161.8,
          "cumulative_bottom": 307.0
        }
      ]
    },
    {
      "label": "Stage 2",
      "segments": [
        {
          "name": "REE fraction",
          "value": 148.4,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Iron impurity",
          "value": 99.8,
          "cumulative_bottom": 148.4
        },
        {
          "name": "Silica impurity",
          "value": 213.0,
          "cumulative_bottom": 248.2
        }
      ]
    },
    {
      "label": "Stage 3",
      "segments": [
        {
          "name": "REE fraction",
          "value": 104.8,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Iron impurity",
          "value": 130.9,
          "cumulative_bottom": 104.8
        },
        {
          "name": "Silica impurity",
          "value": 209.4,
          "cumulative_bottom": 235.7
        }
      ]
    },
    {
      "label": "Stage 4",
      "segments": [
        {
          "name": "REE fraction",
          "value": 126.3,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Iron impurity",
          "value": 57.1,
          "cumulative_bottom": 126.3
        },
        {
          "name": "Silica impurity",
          "value": 29.9,
          "cumulative_bottom": 183.4
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: Set1 with 3 colors. Vertical gridlines only. Legend displayed upper right with light gray border frame.
