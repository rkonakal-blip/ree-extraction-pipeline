# Ground Truth: grouped_barplot1

## Plot Configuration

- **Plot type**: Grouped bar chart
- **Orientation**: Vertical
- **Number of groups**: 4
- **Number of series**: 3
- **Y-axis metric**: Extraction Efficiency (%)
- **Error bars present**: No
- **numpy seed**: 301

## Data

```json
{
  "title": "Extraction Efficiency of REEs with Different Extractants vs pH",
  "x_label": "pH",
  "y_label": "Extraction Efficiency (%)",
  "y_axis_range": [
    0,
    100
  ],
  "series": [
    "D2EHPA",
    "Cyanex 272",
    "PC88A"
  ],
  "groups": [
    {
      "label": "1.5",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 46.3,
          "error": null
        },
        {
          "series": "Cyanex 272",
          "value": 76.0,
          "error": null
        },
        {
          "series": "PC88A",
          "value": 78.6,
          "error": null
        }
      ]
    },
    {
      "label": "2.0",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 66.3,
          "error": null
        },
        {
          "series": "Cyanex 272",
          "value": 55.2,
          "error": null
        },
        {
          "series": "PC88A",
          "value": 75.8,
          "error": null
        }
      ]
    },
    {
      "label": "2.5",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 72.6,
          "error": null
        },
        {
          "series": "Cyanex 272",
          "value": 89.8,
          "error": null
        },
        {
          "series": "PC88A",
          "value": 49.3,
          "error": null
        }
      ]
    },
    {
      "label": "3.0",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 61.4,
          "error": null
        },
        {
          "series": "Cyanex 272",
          "value": 92.6,
          "error": null
        },
        {
          "series": "PC88A",
          "value": 75.4,
          "error": null
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: tab10 with 3 colors. Bar width per series: 0.2667. Horizontal gridlines only. Legend displayed upper right with light gray border frame.
