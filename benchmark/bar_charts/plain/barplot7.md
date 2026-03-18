# Ground Truth: barplot7

## Plot Configuration

- **Plot type**: Plain bar chart
- **Orientation**: Vertical
- **Number of bars**: 8
- **Y-axis metric**: Extraction Efficiency (%)
- **Error bars present**: No
- **numpy seed**: 107

## Data

```json
{
  "title": "Effect of Diluent on Nd Extraction Efficiency",
  "x_label": "Diluent",
  "y_label": "Extraction Efficiency (%)",
  "y_axis_range": [
    20,
    90
  ],
  "bars": [
    {
      "label": "kerosene",
      "value": 32.7,
      "error": null
    },
    {
      "label": "hexane",
      "value": 78.9,
      "error": null
    },
    {
      "label": "toluene",
      "value": 63.9,
      "error": null
    },
    {
      "label": "heptane",
      "value": 37.6,
      "error": null
    },
    {
      "label": "octanol",
      "value": 46.6,
      "error": null
    },
    {
      "label": "cyclohexane",
      "value": 31.9,
      "error": null
    },
    {
      "label": "xylene",
      "value": 46.9,
      "error": null
    },
    {
      "label": "dodecane",
      "value": 23.3,
      "error": null
    }
  ]
}
```

## Notes

X-tick labels rotated 45 degrees, right-aligned. Legend displayed upper right with light gray border frame. Varied colors per bar using matplotlib tab10 colormap. Horizontal gridlines only.
