# Ground Truth: grouped_barplot6

## Plot Configuration

- **Plot type**: Grouped bar chart
- **Orientation**: Vertical
- **Number of groups**: 4
- **Number of series**: 4
- **Y-axis metric**: Separation Factor (α)
- **Error bars present**: No
- **numpy seed**: 306

## Data

```json
{
  "title": "Separation Factor for Adjacent REE Pairs at Different Extractant Concentrations",
  "x_label": "REE Pair",
  "y_label": "Separation Factor (\u03b1)",
  "y_axis_range": [
    0,
    5
  ],
  "series": [
    "0.1M D2EHPA",
    "0.5M D2EHPA",
    "1.0M D2EHPA",
    "2.0M D2EHPA"
  ],
  "groups": [
    {
      "label": "La/Ce",
      "bars": [
        {
          "series": "0.1M D2EHPA",
          "value": 1.87,
          "error": null
        },
        {
          "series": "0.5M D2EHPA",
          "value": 4.0,
          "error": null
        },
        {
          "series": "1.0M D2EHPA",
          "value": 4.0,
          "error": null
        },
        {
          "series": "2.0M D2EHPA",
          "value": 3.04,
          "error": null
        }
      ]
    },
    {
      "label": "Ce/Pr",
      "bars": [
        {
          "series": "0.1M D2EHPA",
          "value": 4.0,
          "error": null
        },
        {
          "series": "0.5M D2EHPA",
          "value": 3.77,
          "error": null
        },
        {
          "series": "1.0M D2EHPA",
          "value": 3.41,
          "error": null
        },
        {
          "series": "2.0M D2EHPA",
          "value": 2.74,
          "error": null
        }
      ]
    },
    {
      "label": "Pr/Nd",
      "bars": [
        {
          "series": "0.1M D2EHPA",
          "value": 2.0,
          "error": null
        },
        {
          "series": "0.5M D2EHPA",
          "value": 4.0,
          "error": null
        },
        {
          "series": "1.0M D2EHPA",
          "value": 4.0,
          "error": null
        },
        {
          "series": "2.0M D2EHPA",
          "value": 4.0,
          "error": null
        }
      ]
    },
    {
      "label": "Nd/Sm",
      "bars": [
        {
          "series": "0.1M D2EHPA",
          "value": 2.61,
          "error": null
        },
        {
          "series": "0.5M D2EHPA",
          "value": 2.08,
          "error": null
        },
        {
          "series": "1.0M D2EHPA",
          "value": 1.92,
          "error": null
        },
        {
          "series": "2.0M D2EHPA",
          "value": 1.07,
          "error": null
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: tab10 with 4 colors. Bar width per series: 0.2. Horizontal gridlines only. Legend displayed upper right with light gray border frame.
