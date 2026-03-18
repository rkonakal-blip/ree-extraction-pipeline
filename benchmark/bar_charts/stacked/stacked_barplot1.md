# Ground Truth: stacked_barplot1

## Plot Configuration

- **Plot type**: Stacked bar chart
- **Orientation**: Vertical
- **Number of groups**: 5
- **Number of segments**: 3
- **Y-axis metric**: Proportion (%)
- **numpy seed**: 201

## Data

```json
{
  "title": "Phase Distribution Across pH Levels",
  "x_label": "pH",
  "y_label": "Proportion (%)",
  "y_axis_range": [
    0,
    100
  ],
  "segments": [
    "Organic phase",
    "Aqueous phase",
    "Interfacial"
  ],
  "bars": [
    {
      "label": "1.5",
      "segments": [
        {
          "name": "Organic phase",
          "value": 10.2,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Aqueous phase",
          "value": 49.1,
          "cumulative_bottom": 10.2
        },
        {
          "name": "Interfacial",
          "value": 40.7,
          "cumulative_bottom": 59.3
        }
      ]
    },
    {
      "label": "2.0",
      "segments": [
        {
          "name": "Organic phase",
          "value": 47.4,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Aqueous phase",
          "value": 42.0,
          "cumulative_bottom": 47.4
        },
        {
          "name": "Interfacial",
          "value": 10.6,
          "cumulative_bottom": 89.4
        }
      ]
    },
    {
      "label": "2.5",
      "segments": [
        {
          "name": "Organic phase",
          "value": 40.0,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Aqueous phase",
          "value": 25.0,
          "cumulative_bottom": 40.0
        },
        {
          "name": "Interfacial",
          "value": 35.0,
          "cumulative_bottom": 65.0
        }
      ]
    },
    {
      "label": "3.0",
      "segments": [
        {
          "name": "Organic phase",
          "value": 23.4,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Aqueous phase",
          "value": 60.3,
          "cumulative_bottom": 23.4
        },
        {
          "name": "Interfacial",
          "value": 16.3,
          "cumulative_bottom": 83.7
        }
      ]
    },
    {
      "label": "3.5",
      "segments": [
        {
          "name": "Organic phase",
          "value": 35.6,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Aqueous phase",
          "value": 53.8,
          "cumulative_bottom": 35.6
        },
        {
          "name": "Interfacial",
          "value": 10.6,
          "cumulative_bottom": 89.4
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: tab10 with 3 colors. Horizontal gridlines only. Legend displayed upper right with light gray border frame. All bars sum to 100%.
