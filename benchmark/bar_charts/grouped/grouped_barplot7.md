# Ground Truth: grouped_barplot7

## Plot Configuration

- **Plot type**: Grouped bar chart
- **Orientation**: Vertical
- **Number of groups**: 6
- **Number of series**: 3
- **Y-axis metric**: Extraction Efficiency (%)
- **Error bars present**: Yes
- **numpy seed**: 307

## Data

```json
{
  "title": "Effect of Initial Concentration on REE Extraction",
  "x_label": "Initial Concentration (mg/L)",
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
      "label": "50",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 45.0,
          "error": 5.72
        },
        {
          "series": "Cyanex 272",
          "value": 58.1,
          "error": 3.96
        },
        {
          "series": "PC88A",
          "value": 78.4,
          "error": 5.93
        }
      ]
    },
    {
      "label": "100",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 52.7,
          "error": 4.14
        },
        {
          "series": "Cyanex 272",
          "value": 53.2,
          "error": 3.63
        },
        {
          "series": "PC88A",
          "value": 47.6,
          "error": 3.71
        }
      ]
    },
    {
      "label": "200",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 51.5,
          "error": 4.55
        },
        {
          "series": "Cyanex 272",
          "value": 90.7,
          "error": 2.4
        },
        {
          "series": "PC88A",
          "value": 25.6,
          "error": 4.69
        }
      ]
    },
    {
      "label": "300",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 88.8,
          "error": 5.42
        },
        {
          "series": "Cyanex 272",
          "value": 71.1,
          "error": 4.8
        },
        {
          "series": "PC88A",
          "value": 95.2,
          "error": 4.88
        }
      ]
    },
    {
      "label": "500",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 81.8,
          "error": 3.51
        },
        {
          "series": "Cyanex 272",
          "value": 39.6,
          "error": 3.8
        },
        {
          "series": "PC88A",
          "value": 65.7,
          "error": 3.42
        }
      ]
    },
    {
      "label": "1000",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 21.8,
          "error": 4.26
        },
        {
          "series": "Cyanex 272",
          "value": 97.8,
          "error": 4.79
        },
        {
          "series": "PC88A",
          "value": 44.4,
          "error": 5.61
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: Set1 with 3 colors. Bar width per series: 0.2667. Horizontal gridlines only. Legend displayed upper right with light gray border frame.
