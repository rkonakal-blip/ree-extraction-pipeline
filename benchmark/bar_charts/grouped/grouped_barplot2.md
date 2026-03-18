# Ground Truth: grouped_barplot2

## Plot Configuration

- **Plot type**: Grouped bar chart
- **Orientation**: Vertical
- **Number of groups**: 5
- **Number of series**: 2
- **Y-axis metric**: Extraction Efficiency (%)
- **Error bars present**: Yes
- **numpy seed**: 302

## Data

```json
{
  "title": "Effect of Temperature on La and Nd Extraction",
  "x_label": "Temperature (\u00b0C)",
  "y_label": "Extraction Efficiency (%)",
  "y_axis_range": [
    0,
    100
  ],
  "series": [
    "La",
    "Nd"
  ],
  "groups": [
    {
      "label": "20",
      "bars": [
        {
          "series": "La",
          "value": 69.6,
          "error": 3.31
        },
        {
          "series": "Nd",
          "value": 62.3,
          "error": 2.19
        }
      ]
    },
    {
      "label": "30",
      "bars": [
        {
          "series": "La",
          "value": 84.4,
          "error": 2.12
        },
        {
          "series": "Nd",
          "value": 62.6,
          "error": 2.88
        }
      ]
    },
    {
      "label": "40",
      "bars": [
        {
          "series": "La",
          "value": 46.6,
          "error": 4.29
        },
        {
          "series": "Nd",
          "value": 30.3,
          "error": 3.54
        }
      ]
    },
    {
      "label": "50",
      "bars": [
        {
          "series": "La",
          "value": 77.7,
          "error": 4.49
        },
        {
          "series": "Nd",
          "value": 32.0,
          "error": 2.92
        }
      ]
    },
    {
      "label": "60",
      "bars": [
        {
          "series": "La",
          "value": 56.6,
          "error": 2.74
        },
        {
          "series": "Nd",
          "value": 40.0,
          "error": 2.38
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: Set1 with 2 colors. Bar width per series: 0.4. Horizontal gridlines only. Legend displayed upper right with light gray border frame.
