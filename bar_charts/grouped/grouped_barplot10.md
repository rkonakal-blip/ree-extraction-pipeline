# Ground Truth: grouped_barplot10

## Plot Configuration

- **Plot type**: Grouped bar chart
- **Orientation**: Vertical
- **Number of groups**: 4
- **Number of series**: 3
- **Y-axis metric**: Extraction Efficiency (%)
- **Error bars present**: Yes
- **numpy seed**: 310

## Data

```json
{
  "title": "Extraction Efficiency at Different Reagent Concentrations",
  "x_label": "Reagent Concentration (M)",
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
      "label": "0.1",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 83.8,
          "error": 3.26
        },
        {
          "series": "Cyanex 272",
          "value": 81.1,
          "error": 3.5
        },
        {
          "series": "PC88A",
          "value": 82.1,
          "error": 4.89
        }
      ]
    },
    {
      "label": "0.5",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 72.1,
          "error": 2.23
        },
        {
          "series": "Cyanex 272",
          "value": 44.4,
          "error": 3.89
        },
        {
          "series": "PC88A",
          "value": 90.8,
          "error": 2.72
        }
      ]
    },
    {
      "label": "1.0",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 96.0,
          "error": 1.46
        },
        {
          "series": "Cyanex 272",
          "value": 24.7,
          "error": 3.96
        },
        {
          "series": "PC88A",
          "value": 62.1,
          "error": 3.84
        }
      ]
    },
    {
      "label": "2.0",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 67.6,
          "error": 4.94
        },
        {
          "series": "Cyanex 272",
          "value": 71.5,
          "error": 1.47
        },
        {
          "series": "PC88A",
          "value": 23.2,
          "error": 3.4
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: tab10 with 3 colors. Bar width per series: 0.2667. Horizontal gridlines only. Legend displayed upper right with light gray border frame.
