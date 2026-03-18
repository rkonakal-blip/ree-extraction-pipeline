# Ground Truth: barplot10

## Plot Configuration

- **Plot type**: Plain bar chart
- **Orientation**: Vertical
- **Number of bars**: 6
- **Y-axis metric**: Extraction Efficiency (%)
- **Error bars present**: Yes
- **numpy seed**: 110

## Data

```json
{
  "title": "Effect of Initial Metal Concentration on La Extraction",
  "x_label": "Initial Concentration (mg/L)",
  "y_label": "Extraction Efficiency (%)",
  "y_axis_range": [
    60,
    100
  ],
  "bars": [
    {
      "label": "50",
      "value": 61.0,
      "error": 4.82
    },
    {
      "label": "100",
      "value": 71.4,
      "error": 3.55
    },
    {
      "label": "200",
      "value": 61.0,
      "error": 3.05
    },
    {
      "label": "300",
      "value": 67.8,
      "error": 1.34
    },
    {
      "label": "500",
      "value": 73.0,
      "error": 2.55
    },
    {
      "label": "1000",
      "value": 73.2,
      "error": 2.16
    }
  ]
}
```

## Notes

Legend displayed upper right with light gray border frame. Varied colors per bar using matplotlib tab10 colormap. Horizontal gridlines only.
