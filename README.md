# REE Extraction Data Pipeline

A Claude-based pipeline for extracting quantitative data from scientific 
figures and tables in rare earth element (REE) extraction literature. 
The goal is to build a production-ready, modular extraction system 
evaluated against a rigorous benchmark dataset.

---

## Project Overview

Scientific publications in REE extraction research present critical data — 
recovery rates, extraction efficiencies, leaching kinetics — locked inside 
plot images and complex tables. This project develops and benchmarks a 
Claude-based pipeline to automatically extract that data into structured, 
machine-readable JSON.

The system is evaluated using a synthetic benchmark dataset where ground 
truth values are known exactly, enabling precise error computation 
using MAE, RMSE, MAPE, and R².

---

## Repository Structure
```
ree-extraction-pipeline/
│
├── reports/                  # Weekly progress reports
│
├── week1/                    # Initial exploration and setup
├── week2/                    # Two-phase extract–validate framework
├── week3/                    # Schema design and skill architecture
├── week4/                    # Synthetic benchmark dataset construction
│
└── README.md
```

---

## How It Works

**1. Extraction**
The Claude-based pipeline receives a plot image or table and extracts 
data into a structured JSON output.

**2. Validation**
Extracted output is validated against a fixed Pydantic schema with 
confidence flags and uncertainty indicators.

**3. Evaluation**
Extracted JSON is compared against ground truth point by point. 
Error metrics (MAE, RMSE, MAPE, R²) are computed per figure and 
aggregated by type.

---

## Tools and Models

- **Extraction:** Claude (Anthropic)
- **Validation:** Pydantic
- **Baseline comparison:** WebPlotDigitizer, ChartOCR benchmarks
- **Comparative models:** GPT-4o, Gemini 1.5 Pro, LangExtract

---

## Progress

| Week | Focus |
|------|-------|
| Week 1 | Initial setup and proof of concept |
| Week 2 | Two-phase extract–validate framework and evaluation metrics |
| Week 3 | Schema design, skill architecture, and benchmarking strategy |
| Week 4 | Synthetic benchmark dataset construction and scatter plot verification |

---

## Status

Actively under development as part of an ongoing research project. 
Weekly progress reports are available in the `/reports` folder.
