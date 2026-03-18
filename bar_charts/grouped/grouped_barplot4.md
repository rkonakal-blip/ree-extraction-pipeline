# Ground Truth: grouped_barplot4

## Plot Configuration

- **Plot type**: Grouped bar chart
- **Orientation**: Horizontal
- **Number of groups**: 4
- **Number of series**: 3
- **Y-axis metric**: Stripping Efficiency (%)
- **Error bars present**: No
- **numpy seed**: 304

## Data

```json
{
  "title": "Stripping Efficiency of REEs with Different Stripping Agents",
  "x_label": "Stripping Agent",
  "y_label": "Stripping Efficiency (%)",
  "y_axis_range": [
    0,
    100
  ],
  "series": [
    "La",
    "Ce",
    "Nd"
  ],
  "groups": [
    {
      "label": "HCl 1M",
      "bars": [
        {
          "series": "La",
          "value": 57.9,
          "error": null
        },
        {
          "series": "Ce",
          "value": 53.3,
          "error": null
        },
        {
          "series": "Nd",
          "value": 88.7,
          "error": null
        }
      ]
    },
    {
      "label": "HCl 2M",
      "bars": [
        {
          "series": "La",
          "value": 85.6,
          "error": null
        },
        {
          "series": "Ce",
          "value": 57.4,
          "error": null
        },
        {
          "series": "Nd",
          "value": 42.2,
          "error": null
        }
      ]
    },
    {
      "label": "H2SO4",
      "bars": [
        {
          "series": "La",
          "value": 92.9,
          "error": null
        },
        {
          "series": "Ce",
          "value": 70.4,
          "error": null
        },
        {
          "series": "Nd",
          "value": 42.6,
          "error": null
        }
      ]
    },
    {
      "label": "HNO3",
      "bars": [
        {
          "series": "La",
          "value": 57.4,
          "error": null
        },
        {
          "series": "Ce",
          "value": 89.7,
          "error": null
        },
        {
          "series": "Nd",
          "value": 33.4,
          "error": null
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: Set2 with 3 colors. Bar width per series: 0.2667. Vertical gridlines only. Legend displayed upper right with light gray border frame.
