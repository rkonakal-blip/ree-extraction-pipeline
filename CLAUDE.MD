# REE Extraction Pipeline

## Project Overview
An LLM-based modular pipeline that extracts structured quantitative 
data from scientific figures and tables in rare earth element (REE) 
solvent extraction literature. Outputs structured JSON, HTML reports, 
and Markdown for downstream analysis and compilation into a reference 
database.

The pipeline runs five sequential stages — Detect, Classify, Extract, 
Validate, and Summarise — each executed as a dedicated slash command. 
For figures and plots, all five stages run independently. For tables, 
Extract and Validate are condensed into a single unified skill.

## Repository
https://github.com/rkonakal-blip/ree-extraction-pipeline

## Project Structure
├── .claude/           ← Claude Code config (auto-generated, do not edit)
│   └── commands/      ← installed skill files (do not edit directly)
├── .obsidian/         ← Obsidian config (auto-generated, ignore)
├── benchmark/         ← synthetic benchmark figures and ground truth JSONs
├── prompts/           ← source skill files (edit these)
├── results/           ← all extraction outputs (JSON, HTML, Markdown)
├── CLAUDE.md          ← this file
├── install_skills.py  ← run this to install skill files into Claude Code
└── schemas.py         ← Pydantic schemas for output validation

## Environment
- Python 3.10+
- Key dependencies: PyMuPDF, apted

## Pipeline Stages

### Figures and Plots
1. Detect → `detect.md`
2. Classify → `classify.md`
3. Extract → `extract.md`
4. Validate → `validate_charts.md`
5. Summarise → `summarise.md`
6. Master orchestrator → `orchestrate.md`

### Tables
1. Detect → `detect_tables.md`
2. Extract + Validate + Report → `table.md`

## Rules

### General
- Stay strictly within this project directory at all times
- Never read or write files outside this project directory
- Follow all instructions in every skill file strictly — no steps 
  skipped, no steps reordered
- Ask before installing any new package
- Ask before deleting any file
- Never edit files in .claude/commands/ directly — always edit in 
  prompts/ and run install_skills.py

### Pipeline Execution
- Always follow the sequential order: 
  Detect → Classify → Extract → Validate → Summarise
- Never combine, skip, or reorder pipeline stages unless explicitly 
  instructed by the user
- Take a modular approach (running individual stages) only when 
  explicitly asked by the user

### Figure vs Table Branching
- Detect identifies both figures and tables from the input PDF
- After detection, branch automatically:
  - Figures and plots → Classify → Extract → Validate → Summarise
  - Tables → Table skill (extract + validate combined) → Summarise
- Both branches feed into Summarise for a single combined output
- Never run Classify, Extract, or validate_charts.md on tables
- Never run table.md on figures or plots

### Benchmark
- Never modify, overwrite, or delete any file in benchmark/
- Never use benchmark/ files as outputs or temporary storage
- Read benchmark/ files only when explicitly asked for evaluation 
  or testing

### Outputs
- Save all outputs to results/ only, never anywhere else
- Never overwrite an existing file in results/ without asking first
- All output JSON must be valid and match the schemas in schemas.py
- Never skip schema validation before saving output
- Output filenames must follow this pattern:
  [input_filename]_[stage]_output.[ext]
  e.g. syn_001_classified.json, syn_001_extracted.json

### Data Integrity
- This pipeline is for research and publication — no shortcuts, 
  no manipulation of extracted data
- Never approximate values unless explicitly asked — extract only 
  what is present in the figure or table
- If any value is approximated, explicitly flag it in the output 
  JSON under an "approximated" field set to true
- Never hallucinate or infer data points that are not visible in 
  the input image

## Usage
Always launch Claude Code from the project root:
cd ree-extraction-pipeline
claude

Do not access, modify, or create files outside the project directory 
unless explicitly instructed by the user.