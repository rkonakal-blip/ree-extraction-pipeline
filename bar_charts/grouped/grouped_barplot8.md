# Ground Truth: grouped_barplot8

## Plot Configuration

- **Plot type**: Grouped bar chart
- **Orientation**: Vertical
- **Number of groups**: 3
- **Number of series**: 5
- **Y-axis metric**: Recovery (%)
- **Error bars present**: No
- **numpy seed**: 308

## Data

```json
{
  "title": "Recovery of REEs with Different Diluents",
  "x_label": "Diluent",
  "y_label": "Recovery (%)",
  "y_axis_range": [
    50,
    100
  ],
  "series": [
    "La",
    "Ce",
    "Nd",
    "Pr",
    "Sm"
  ],
  "groups": [
    {
      "label": "Kerosene",
      "bars": [
        {
          "series": "La",
          "value": 87.7,
          "error": null
        },
        {
          "series": "Ce",
          "value": 78.2,
          "error": null
        },
        {
          "series": "Nd",
          "value": 76.6,
          "error": null
        },
        {
          "series": "Pr",
          "value": 74.2,
          "error": null
        },
        {
          "series": "Sm",
          "value": 56.2,
          "error": null
        }
      ]
    },
    {
      "label": "Hexane",
      "bars": [
        {
          "series": "La",
          "value": 83.1,
          "error": null
        },
        {
          "series": "Ce",
          "value": 55.5,
          "error": null
        },
        {
          "series": "Nd",
          "value": 61.1,
          "error": null
        },
        {
          "series": "Pr",
          "value": 66.1,
          "error": null
        },
        {
          "series": "Sm",
          "value": 91.2,
          "error": null
        }
      ]
    },
    {
      "label": "Toluene",
      "bars": [
        {
          "series": "La",
          "value": 51.0,
          "error": null
        },
        {
          "series": "Ce",
          "value": 53.8,
          "error": null
        },
        {
          "series": "Nd",
          "value": 81.2,
          "error": null
        },
        {
          "series": "Pr",
          "value": 73.8,
          "error": null
        },
        {
          "series": "Sm",
          "value": 66.3,
          "error": null
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: tab20 with 5 colors. Bar width per series: 0.16. Horizontal gridlines only. Legend displayed upper right with light gray border frame.
