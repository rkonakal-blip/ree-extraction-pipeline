# Ground Truth: stacked_barplot2

## Plot Configuration

- **Plot type**: Stacked bar chart
- **Orientation**: Vertical
- **Number of groups**: 4
- **Number of segments**: 4
- **Y-axis metric**: Mass Distribution (%)
- **numpy seed**: 202

## Data

```json
{
  "title": "REE Mass Distribution After Solvent Extraction",
  "x_label": "REE Element",
  "y_label": "Mass Distribution (%)",
  "y_axis_range": [
    0,
    100
  ],
  "segments": [
    "Extracted",
    "Raffinate",
    "Scrubbed",
    "Stripped"
  ],
  "bars": [
    {
      "label": "La",
      "segments": [
        {
          "name": "Extracted",
          "value": 10.4,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Raffinate",
          "value": 11.9,
          "cumulative_bottom": 10.4
        },
        {
          "name": "Scrubbed",
          "value": 38.6,
          "cumulative_bottom": 22.3
        },
        {
          "name": "Stripped",
          "value": 39.1,
          "cumulative_bottom": 60.9
        }
      ]
    },
    {
      "label": "Ce",
      "segments": [
        {
          "name": "Extracted",
          "value": 42.1,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Raffinate",
          "value": 25.1,
          "cumulative_bottom": 42.1
        },
        {
          "name": "Scrubbed",
          "value": 26.2,
          "cumulative_bottom": 67.2
        },
        {
          "name": "Stripped",
          "value": 6.6,
          "cumulative_bottom": 93.4
        }
      ]
    },
    {
      "label": "Nd",
      "segments": [
        {
          "name": "Extracted",
          "value": 30.9,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Raffinate",
          "value": 10.2,
          "cumulative_bottom": 30.9
        },
        {
          "name": "Scrubbed",
          "value": 37.3,
          "cumulative_bottom": 41.1
        },
        {
          "name": "Stripped",
          "value": 21.6,
          "cumulative_bottom": 78.4
        }
      ]
    },
    {
      "label": "Pr",
      "segments": [
        {
          "name": "Extracted",
          "value": 24.0,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Raffinate",
          "value": 6.8,
          "cumulative_bottom": 24.0
        },
        {
          "name": "Scrubbed",
          "value": 24.0,
          "cumulative_bottom": 30.8
        },
        {
          "name": "Stripped",
          "value": 45.2,
          "cumulative_bottom": 54.8
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: tab10 with 4 colors. Horizontal gridlines only. Legend displayed upper right with light gray border frame. All bars sum to 100%.
