# REE Extraction Pipeline

## Project Overview
An LLM-based pipeline that extracts structured quantitative data from scientific 
figures (charts, tables) in rare earth element (REE) solvent extraction literature. 
Outputs JSON, HTML, and Markdown for downstream analysis and potential compilation 
into a reference database.

## Repository
https://github.com/rkonakai-blip/ree-extraction-pipeline

## Project Structure
- `prompts/` — all skill files (slash commands)
- `results/` — extraction outputs
- `benchmark/` — test figures and ground truth JSONs
- `schemas.py` — output JSON schemas
- `install_skills.py` — installs skill files into Claude Code

## Environment
- Python 3.10+
- Key dependencies: PyMuPDF, apted

## Pipeline Stages (for plots)
1. Detect → `detect.md`
2. Classify → `classify.md`
3. Extract → `extract.md`
4. Validate → `validate_charts.md`
5. Summarise → `summarise.md`
6. Master orchestrator → `orchestrate.md`

## Tables
- Detection: `detect_tables.md`
- Extraction + Validation + Report: `table.md`

## Rules
- Never modify or use files in `benchmark/` unless explicitly asked — confirm once before proceeding
- Output must always be valid JSON matching schemas in `schemas.py`
- This pipeline is for research and publication — no shortcuts, no manipulation of data
- Never approximate values unless explicitly asked to — extract only what is present in the figure
- If any value is approximated, explicitly flag it in the output

## Usage
Always launch Claude Code from the project root by running: cd ree-extraction-pipeline then claude
Do not access, modify, or create files outside the project directory unless explicitly asked by the user