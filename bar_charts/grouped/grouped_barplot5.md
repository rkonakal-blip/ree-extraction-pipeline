# Ground Truth: grouped_barplot5

## Plot Configuration

- **Plot type**: Grouped bar chart
- **Orientation**: Vertical
- **Number of groups**: 5
- **Number of series**: 2
- **Y-axis metric**: Extraction Efficiency (%)
- **Error bars present**: Yes
- **numpy seed**: 305

## Data

```json
{
  "title": "Extraction Kinetics of D2EHPA vs PC88A",
  "x_label": "Contact Time (min)",
  "y_label": "Extraction Efficiency (%)",
  "y_axis_range": [
    40,
    100
  ],
  "series": [
    "D2EHPA",
    "PC88A"
  ],
  "groups": [
    {
      "label": "10",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 41.0,
          "error": 2.81
        },
        {
          "series": "PC88A",
          "value": 67.2,
          "error": 2.68
        }
      ]
    },
    {
      "label": "20",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 86.2,
          "error": 2.77
        },
        {
          "series": "PC88A",
          "value": 96.5,
          "error": 2.77
        }
      ]
    },
    {
      "label": "30",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 60.5,
          "error": 1.14
        },
        {
          "series": "PC88A",
          "value": 54.7,
          "error": 1.25
        }
      ]
    },
    {
      "label": "45",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 52.8,
          "error": 3.04
        },
        {
          "series": "PC88A",
          "value": 85.6,
          "error": 3.87
        }
      ]
    },
    {
      "label": "60",
      "bars": [
        {
          "series": "D2EHPA",
          "value": 57.5,
          "error": 1.18
        },
        {
          "series": "PC88A",
          "value": 48.6,
          "error": 1.1
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: Paired with 2 colors. Bar width per series: 0.4. Horizontal gridlines only. Legend displayed upper right with light gray border frame.
