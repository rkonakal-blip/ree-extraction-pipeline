# Ground Truth: barplot2

## Plot Configuration

- **Plot type**: Plain bar chart
- **Orientation**: Vertical
- **Number of bars**: 6
- **Y-axis metric**: Extraction Efficiency (%)
- **Error bars present**: Yes
- **numpy seed**: 102

## Data

```json
{
  "title": "Extraction Efficiency of La with Different Extractants",
  "x_label": "Extractant",
  "y_label": "Extraction Efficiency (%)",
  "y_axis_range": [
    0,
    100
  ],
  "bars": [
    {
      "label": "D2EHPA",
      "value": 66.6,
      "error": 2.5
    },
    {
      "label": "Cyanex 272",
      "value": 72.7,
      "error": 2.94
    },
    {
      "label": "PC88A",
      "value": 43.3,
      "error": 3.07
    },
    {
      "label": "TBP",
      "value": 77.0,
      "error": 3.48
    },
    {
      "label": "EHEHPA",
      "value": 65.1,
      "error": 3.47
    },
    {
      "label": "Aliquat 336",
      "value": 83.1,
      "error": 4.68
    }
  ]
}
```

## Notes

X-tick labels rotated 45 degrees, right-aligned. Single bar color: #C0504D. Horizontal gridlines only.
