# Ground Truth: stacked_barplot9

## Plot Configuration

- **Plot type**: Stacked bar chart
- **Orientation**: Vertical
- **Number of groups**: 5
- **Number of segments**: 4
- **Y-axis metric**: Recovery (%)
- **numpy seed**: 209

## Data

```json
{
  "title": "Recovery Distribution Across A:O Ratios",
  "x_label": "A:O Ratio",
  "y_label": "Recovery (%)",
  "y_axis_range": [
    0,
    100
  ],
  "segments": [
    "Extracted",
    "Co-extracted",
    "Scrubbed",
    "Stripped"
  ],
  "bars": [
    {
      "label": "1:3",
      "segments": [
        {
          "name": "Extracted",
          "value": 31.6,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Co-extracted",
          "value": 13.8,
          "cumulative_bottom": 31.6
        },
        {
          "name": "Scrubbed",
          "value": 30.7,
          "cumulative_bottom": 45.4
        },
        {
          "name": "Stripped",
          "value": 23.9,
          "cumulative_bottom": 76.1
        }
      ]
    },
    {
      "label": "1:2",
      "segments": [
        {
          "name": "Extracted",
          "value": 24.3,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Co-extracted",
          "value": 46.1,
          "cumulative_bottom": 24.3
        },
        {
          "name": "Scrubbed",
          "value": 20.9,
          "cumulative_bottom": 70.4
        },
        {
          "name": "Stripped",
          "value": 8.7,
          "cumulative_bottom": 91.3
        }
      ]
    },
    {
      "label": "1:1",
      "segments": [
        {
          "name": "Extracted",
          "value": 32.4,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Co-extracted",
          "value": 14.9,
          "cumulative_bottom": 32.4
        },
        {
          "name": "Scrubbed",
          "value": 17.3,
          "cumulative_bottom": 47.3
        },
        {
          "name": "Stripped",
          "value": 35.4,
          "cumulative_bottom": 64.6
        }
      ]
    },
    {
      "label": "2:1",
      "segments": [
        {
          "name": "Extracted",
          "value": 14.2,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Co-extracted",
          "value": 3.8,
          "cumulative_bottom": 14.2
        },
        {
          "name": "Scrubbed",
          "value": 46.2,
          "cumulative_bottom": 18.0
        },
        {
          "name": "Stripped",
          "value": 35.8,
          "cumulative_bottom": 64.2
        }
      ]
    },
    {
      "label": "3:1",
      "segments": [
        {
          "name": "Extracted",
          "value": 7.1,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Co-extracted",
          "value": 33.7,
          "cumulative_bottom": 7.1
        },
        {
          "name": "Scrubbed",
          "value": 20.3,
          "cumulative_bottom": 40.8
        },
        {
          "name": "Stripped",
          "value": 38.9,
          "cumulative_bottom": 61.1
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: Set2 with 4 colors. Horizontal gridlines only. Legend displayed upper right with light gray border frame. All bars sum to 100%.
