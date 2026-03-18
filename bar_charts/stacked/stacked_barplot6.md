# Ground Truth: stacked_barplot6

## Plot Configuration

- **Plot type**: Stacked bar chart
- **Orientation**: Vertical
- **Number of groups**: 6
- **Number of segments**: 4
- **Y-axis metric**: Extraction Efficiency (%)
- **numpy seed**: 206

## Data

```json
{
  "title": "Extraction Kinetics by Contact Time",
  "x_label": "Contact Time (min)",
  "y_label": "Extraction Efficiency (%)",
  "y_axis_range": [
    0,
    100
  ],
  "segments": [
    "Fast extraction",
    "Slow extraction",
    "Equilibrium",
    "Residual"
  ],
  "bars": [
    {
      "label": "5",
      "segments": [
        {
          "name": "Fast extraction",
          "value": 27.4,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Slow extraction",
          "value": 30.7,
          "cumulative_bottom": 27.4
        },
        {
          "name": "Equilibrium",
          "value": 5.6,
          "cumulative_bottom": 58.1
        },
        {
          "name": "Residual",
          "value": 36.3,
          "cumulative_bottom": 63.7
        }
      ]
    },
    {
      "label": "10",
      "segments": [
        {
          "name": "Fast extraction",
          "value": 36.6,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Slow extraction",
          "value": 26.4,
          "cumulative_bottom": 36.6
        },
        {
          "name": "Equilibrium",
          "value": 8.8,
          "cumulative_bottom": 63.0
        },
        {
          "name": "Residual",
          "value": 28.2,
          "cumulative_bottom": 71.8
        }
      ]
    },
    {
      "label": "20",
      "segments": [
        {
          "name": "Fast extraction",
          "value": 21.8,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Slow extraction",
          "value": 13.3,
          "cumulative_bottom": 21.8
        },
        {
          "name": "Equilibrium",
          "value": 42.6,
          "cumulative_bottom": 35.1
        },
        {
          "name": "Residual",
          "value": 22.3,
          "cumulative_bottom": 77.7
        }
      ]
    },
    {
      "label": "30",
      "segments": [
        {
          "name": "Fast extraction",
          "value": 38.8,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Slow extraction",
          "value": 28.9,
          "cumulative_bottom": 38.8
        },
        {
          "name": "Equilibrium",
          "value": 7.0,
          "cumulative_bottom": 67.7
        },
        {
          "name": "Residual",
          "value": 25.3,
          "cumulative_bottom": 74.7
        }
      ]
    },
    {
      "label": "45",
      "segments": [
        {
          "name": "Fast extraction",
          "value": 32.0,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Slow extraction",
          "value": 14.0,
          "cumulative_bottom": 32.0
        },
        {
          "name": "Equilibrium",
          "value": 29.5,
          "cumulative_bottom": 46.0
        },
        {
          "name": "Residual",
          "value": 24.5,
          "cumulative_bottom": 75.5
        }
      ]
    },
    {
      "label": "60",
      "segments": [
        {
          "name": "Fast extraction",
          "value": 15.1,
          "cumulative_bottom": 0.0
        },
        {
          "name": "Slow extraction",
          "value": 25.6,
          "cumulative_bottom": 15.1
        },
        {
          "name": "Equilibrium",
          "value": 35.2,
          "cumulative_bottom": 40.7
        },
        {
          "name": "Residual",
          "value": 24.1,
          "cumulative_bottom": 75.9
        }
      ]
    }
  ]
}
```

## Notes

Color scheme: tab20 with 4 colors. Horizontal gridlines only. Legend displayed upper right with light gray border frame. All bars sum to 100%.
