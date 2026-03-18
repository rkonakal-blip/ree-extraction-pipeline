# Ground Truth: piechart4

## Plot Configuration

- **Plot type**: Pie chart
- **Number of slices**: 7
- **Label style**: Legend only
- **Percentage position**: Inside slice
- **Start angle**: 90
- **numpy seed**: 704

## Data

```json
{
  "title": "Mineral Composition of REE Ore Sample",
  "start_angle": 90,
  "slices": [
    {
      "label": "La",
      "value": 16.0,
      "percentage": 16.0
    },
    {
      "label": "Ce",
      "value": 22.3,
      "percentage": 22.3
    },
    {
      "label": "Nd",
      "value": 13.5,
      "percentage": 13.5
    },
    {
      "label": "Pr",
      "value": 4.6,
      "percentage": 4.6
    },
    {
      "label": "Sm",
      "value": 9.1,
      "percentage": 9.1
    },
    {
      "label": "Eu",
      "value": 21.4,
      "percentage": 21.4
    },
    {
      "label": "Others",
      "value": 13.1,
      "percentage": 13.1
    }
  ],
  "total": 100.0
}
```

## Notes

Color scheme: tab10. Labels skipped for small slices (< 5%): Pr. Legend placed to the right of the pie chart. Wedge edges: white, linewidth 1.5.
