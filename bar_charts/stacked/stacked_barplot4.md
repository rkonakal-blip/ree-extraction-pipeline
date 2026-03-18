# Ground Truth: stacked_barplot4

## Plot Configuration

- **Plot type**: Stacked bar chart
- **Orientation**: Vertical
- **Number of groups**: 5
- **Number of segments**: 5
- **Y-axis metric**: Composition (%)
- **numpy seed**: 204

## Data

```json
{
  "title": "Reagent Composition Effect on REE Recovery",
  "x_label": "Extractant",
  "y_label": "Composition (%)",
  "y_axis_range": [
    0,
    100
  ],
  "segments": [
    "La",
    "Ce",
    "Nd",
    "Pr",
    "Others"
  ],
  "bars": [
    {
      "label": "D2EHPA",
      "segments": [
        {
          "name": "La",
          "value": 23.8,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Ce",
          "value": 10.5,
          "cumulative_bottom": 23.8
        },
        {
          "name": "Nd",
          "value": 17.4,
          "cumulative_bottom": 34.3
        },
        {
          "name": "Pr",
          "value": 25.5,
          "cumulative_bottom": 51.7
        },
        {
          "name": "Others",
          "value": 22.8,
          "cumulative_bottom": 77.2
        }
      ]
    },
    {
      "label": "Cyanex 272",
      "segments": [
        {
          "name": "La",
          "value": 29.6,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Ce",
          "value": 15.8,
          "cumulative_bottom": 29.6
        },
        {
          "name": "Nd",
          "value": 23.8,
          "cumulative_bottom": 45.4
        },
        {
          "name": "Pr",
          "value": 11.3,
          "cumulative_bottom": 69.2
        },
        {
          "name": "Others",
          "value": 19.5,
          "cumulative_bottom": 80.5
        }
      ]
    },
    {
      "label": "PC88A",
      "segments": [
        {
          "name": "La",
          "value": 12.6,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Ce",
          "value": 11.9,
          "cumulative_bottom": 12.6
        },
        {
          "name": "Nd",
          "value": 38.9,
          "cumulative_bottom": 24.5
        },
        {
          "name": "Pr",
          "value": 28.1,
          "cumulative_bottom": 63.4
        },
        {
          "name": "Others",
          "value": 8.5,
          "cumulative_bottom": 91.5
        }
      ]
    },
    {
      "label": "TBP",
      "segments": [
        {
          "name": "La",
          "value": 8.0,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Ce",
          "value": 24.1,
          "cumulative_bottom": 8.0
        },
        {
          "name": "Nd",
          "value": 10.5,
          "cumulative_bottom": 32.1
        },
        {
          "name": "Pr",
          "value": 36.4,
          "cumulative_bottom": 42.6
        },
        {
          "name": "Others",
          "value": 21.0,
          "cumulative_bottom": 79.0
        }
      ]
    },
    {
      "label": "EHEHPA",
      "segments": [
        {
          "name": "La",
          "value": 30.1,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Ce",
          "value": 19.9,
          "cumulative_bottom": 30.1
        },
        {
          "name": "Nd",
          "value": 11.8,
          "cumulative_bottom": 50.0
        },
        {
          "name": "Pr",
          "value": 15.3,
          "cumulative_bottom": 61.8
        },
        {
          "name": "Others",
          "value": 22.9,
          "cumulative_bottom": 77.1
        }
      ]
    }
  ]
}
```

## Notes

X-tick labels rotated 45 degrees, right-aligned. Color scheme: tab10 with 5 colors. Horizontal gridlines only. Legend displayed upper right with light gray border frame. All bars sum to 100%.
