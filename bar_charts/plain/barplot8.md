# Ground Truth: barplot8

## Plot Configuration

- **Plot type**: Plain bar chart
- **Orientation**: Horizontal
- **Number of bars**: 5
- **Y-axis metric**: Stripping Efficiency (%)
- **Error bars present**: Yes
- **numpy seed**: 108

## Data

```json
{
  "title": "Stripping Efficiency with Different Stripping Agents",
  "x_label": "Stripping Agent",
  "y_label": "Stripping Efficiency (%)",
  "y_axis_range": [
    0,
    100
  ],
  "bars": [
    {
      "label": "HCl 1M",
      "value": 45.7,
      "error": 4.73
    },
    {
      "label": "HCl 2M",
      "value": 32.3,
      "error": 5.49
    },
    {
      "label": "H2SO4 1M",
      "value": 68.9,
      "error": 2.51
    },
    {
      "label": "HNO3 1M",
      "value": 38.7,
      "error": 4.36
    },
    {
      "label": "EDTA 0.5M",
      "value": 76.0,
      "error": 2.21
    }
  ]
}
```

## Notes

Single bar color: #E26B0A. Vertical gridlines only.
