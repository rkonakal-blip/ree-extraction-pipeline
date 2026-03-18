# Ground Truth: piechart1

## Plot Configuration

- **Plot type**: Pie chart
- **Number of slices**: 5
- **Label style**: Slice labels only
- **Percentage position**: Inside slice
- **Start angle**: 90
- **numpy seed**: 701

## Data

```json
{
  "title": "REE Elemental Composition of Leach Solution",
  "start_angle": 90,
  "slices": [
    {
      "label": "La",
      "value": 29.7,
      "percentage": 29.7
    },
    {
      "label": "Ce",
      "value": 26.4,
      "percentage": 26.4
    },
    {
      "label": "Nd",
      "value": 29.9,
      "percentage": 29.9
    },
    {
      "label": "Pr",
      "value": 12.5,
      "percentage": 12.5
    },
    {
      "label": "Others",
      "value": 1.5,
      "percentage": 1.5
    }
  ],
  "total": 100.0
}
```

## Notes

Color scheme: tab10. Labels skipped for small slices (< 5%): Others. Wedge edges: white, linewidth 1.5.
