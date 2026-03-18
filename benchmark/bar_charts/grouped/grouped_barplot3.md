# Ground Truth: grouped_barplot3

## Plot Configuration

- **Plot type**: Grouped bar chart
- **Orientation**: Vertical
- **Number of groups**: 3
- **Number of series**: 4
- **Y-axis metric**: Distribution Ratio (D)
- **Error bars present**: No
- **numpy seed**: 303

## Data

```json
{
  "title": "Distribution Ratio of REEs at Different Extractant Concentrations",
  "x_label": "REE Element",
  "y_label": "Distribution Ratio (D)",
  "y_axis_range": [
    0,
    15
  ],
  "series": [
    "0.1M extractant",
    "0.5M extractant",
    "1.0M extractant",
    "2.0M extractant"
  ],
  "groups": [
    {
      "label": "La",
      "bars": [
        {
          "series": "0.1M extractant",
          "value": 10.63,
          "error": null
        },
        {
          "series": "0.5M extractant",
          "value": 11.45,
          "error": null
        },
        {
          "series": "1.0M extractant",
          "value": 3.02,
          "error": null
        },
        {
          "series": "2.0M extractant",
          "value": 8.43,
          "error": null
        }
      ]
    },
    {
      "label": "Ce",
      "bars": [
        {
          "series": "0.1M extractant",
          "value": 4.29,
          "error": null
        },
        {
          "series": "0.5M extractant",
          "value": 8.89,
          "error": null
        },
        {
          "series": "1.0M extractant",
          "value": 5.36,
          "error": null
        },
        {
          "series": "2.0M extractant",
          "value": 9.35,
          "error": null
        }
      ]
    },
    {
      "label": "Nd",
      "bars": [
        {
          "series": "0.1M extractant",
          "value": 7.94,
          "error": null
        },
        {
          "series": "0.5M extractant",
          "value": 6.38,
          "error": null
        },
        {
          "series": "1.0M extractant",
          "value": 4.39,
          "error": null
        },
        {
          "series": "2.0M extractant",
          "value": 2.46,
          "error": null
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: tab10 with 4 colors. Bar width per series: 0.2. Horizontal gridlines only. Legend displayed upper right with light gray border frame.
