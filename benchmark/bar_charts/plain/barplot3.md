# Ground Truth: barplot3

## Plot Configuration

- **Plot type**: Plain bar chart
- **Orientation**: Horizontal
- **Number of bars**: 4
- **Y-axis metric**: Distribution Ratio (D)
- **Error bars present**: No
- **numpy seed**: 103

## Data

```json
{
  "title": "Distribution Ratio of REEs in D2EHPA System",
  "x_label": "REE Element",
  "y_label": "Distribution Ratio (D)",
  "y_axis_range": [
    0,
    10
  ],
  "bars": [
    {
      "label": "La",
      "value": 8.06,
      "error": null
    },
    {
      "label": "Ce",
      "value": 3.55,
      "error": null
    },
    {
      "label": "Nd",
      "value": 3.49,
      "error": null
    },
    {
      "label": "Pr",
      "value": 9.0,
      "error": null
    }
  ]
}
```

## Notes

Legend displayed upper right with light gray border frame. Varied colors per bar using matplotlib tab10 colormap. No gridlines.
