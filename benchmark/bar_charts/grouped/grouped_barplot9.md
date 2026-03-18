# Ground Truth: grouped_barplot9

## Plot Configuration

- **Plot type**: Grouped bar chart
- **Orientation**: Horizontal
- **Number of groups**: 5
- **Number of series**: 2
- **Y-axis metric**: Distribution Ratio (D)
- **Error bars present**: No
- **numpy seed**: 309

## Data

```json
{
  "title": "Distribution Ratio of La and Nd at Different A:O Ratios",
  "x_label": "A:O Ratio",
  "y_label": "Distribution Ratio (D)",
  "y_axis_range": [
    0,
    20
  ],
  "series": [
    "La",
    "Nd"
  ],
  "groups": [
    {
      "label": "1:3",
      "bars": [
        {
          "series": "La",
          "value": 14.29,
          "error": null
        },
        {
          "series": "Nd",
          "value": 12.14,
          "error": null
        }
      ]
    },
    {
      "label": "1:2",
      "bars": [
        {
          "series": "La",
          "value": 14.7,
          "error": null
        },
        {
          "series": "Nd",
          "value": 5.22,
          "error": null
        }
      ]
    },
    {
      "label": "1:1",
      "bars": [
        {
          "series": "La",
          "value": 14.63,
          "error": null
        },
        {
          "series": "Nd",
          "value": 3.66,
          "error": null
        }
      ]
    },
    {
      "label": "2:1",
      "bars": [
        {
          "series": "La",
          "value": 9.04,
          "error": null
        },
        {
          "series": "Nd",
          "value": 4.83,
          "error": null
        }
      ]
    },
    {
      "label": "3:1",
      "bars": [
        {
          "series": "La",
          "value": 5.8,
          "error": null
        },
        {
          "series": "Nd",
          "value": 1.0,
          "error": null
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: Set2 with 2 colors. Bar width per series: 0.4. Vertical gridlines only. Legend displayed upper right with light gray border frame.
