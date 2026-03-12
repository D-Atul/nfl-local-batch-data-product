# Local Batch Data Pipeline for Historical NFL Game Analytics

![CI](https://github.com/D-Atul/local-batch-data-product/actions/workflows/ci.yml/badge.svg)

A contract-first local batch data pipeline that ingests historical NFL game events, validates them with schema contracts, transforms them into curated analytics tables, and produces reproducible outputs with run logging and evidence.

---

## Business / Engineering Problem

Historical sports datasets are often distributed as raw CSV files with inconsistent guarantees around structure, completeness, and reliability.  
Without validation and controlled transformations, downstream analysis can easily become unreliable or irreproducible.

This project demonstrates how a **data engineer converts raw historical data into trustworthy, analysis-ready datasets** using a structured batch pipeline with explicit validation, deterministic execution, and observable run artifacts.

The objective is to demonstrate **production-minded data engineering practices**, not exploratory analysis.

---

## Architecture Overview

![Architecture](docs/architecture.png)

Pipeline flow:

Raw CSV input  
→ Raw schema guardrails validate required columns and structure  
→ Transformation stage standardizes event records  
→ Curated contract validation ensures post-transform correctness  
→ Metric tables are generated from curated events  
→ Output contracts validate published datasets  
→ Outputs are written atomically  
→ Run metadata and validation outcomes are logged  
→ Evidence notebook inspects run artifacts and outputs

This mirrors a simplified **local batch data product architecture** used in production environments.

---

## Tech Stack

- Python  
- Pandas  
- Pandera (data contracts)  
- Parquet  
- Pytest  
- GitHub Actions (CI testing)

Only technologies directly used in the pipeline are included.

---

## Project Structure

```
local-batch-data-product/

README.md
requirements.txt
.gitignore
LICENSE

data/
 └── raw/
     nfl_events.csv
     nfl_teams.csv

src/
 ├── contracts/
 │   raw_events_contract.py
 │   metrics_contracts.py
 │
 ├── pipelines/
 │   transform_events.py
 │   build_metrics.py
 │
 └── runner/
     run_local_batch.py

tests/
 ├── test_contracts.py
 ├── test_metrics.py
 ├── test_runner.py
 └── test_transformations.py

docs/
 ├── architecture.png
 └── pipeline_flow.png

logs/
 └── run_<example>.json

evidence/
 └── evidence_notebook.ipynb

framework/
 └── batch_framework.md
```

### Folder Overview

- **src/contracts** — schema contracts and validation logic  
- **src/pipelines** — transformation and metric generation logic  
- **src/runner** — pipeline orchestration and run logging  
- **tests** — contract validation and pipeline tests  
- **docs** — architecture and pipeline diagrams  
- **logs** — example run metadata from pipeline execution  
- **evidence** — read-only notebook inspecting pipeline outputs  
- **framework** — architectural framework defined before implementation

---

## Key Engineering Features

- Contract-first validation before and after transformation  
- Deterministic batch execution  
- Explicit run logging and validation outcomes  
- Separation between raw ingestion and curated outputs  
- Reproducible pipeline runs from a minimal local dataset  
- Automated tests validating contracts and transformations  
- CI pipeline executing tests on repository changes

These features reflect **production-oriented engineering discipline** rather than exploratory analysis.

---

## How to Run

Clone the repository:

```
git clone https://github.com/D-Atul/local-batch-data-product
cd local-batch-data-product
```

Create a virtual environment:

```
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the pipeline:

```
python src/runner/run_local_batch.py
```

Outputs generated:

- Curated metric tables written to `outputs/`
- Run metadata written to `logs/`
- Validation outcomes captured in the run log

---

## Sample Outputs

Example artifacts produced by the pipeline include:

- Metric summary tables (Parquet format)
- Run metadata logs
- Validation status reports
- Evidence notebook inspection

Example log artifact:

```
logs/run_<run_id>.json
```

This file contains:

- execution timestamp  
- input sources  
- row counts  
- validation outcomes  
- output locations  

These artifacts demonstrate **observable pipeline execution**.

---

## Evidence Notebook

The repository includes a read-only notebook:

```
evidence/evidence_notebook.ipynb
```

The notebook inspects:

- generated output datasets  
- run metadata logs  
- validation outcomes  

It provides **execution transparency and verification** without modifying pipeline outputs.

---

## What This Project Demonstrates

This project demonstrates the ability to:

- design a batch data pipeline with clear architectural boundaries  
- implement contract-first data validation  
- produce deterministic and reproducible outputs  
- implement logging and observability in data pipelines  
- structure data engineering repositories professionally  
- create artifacts that resemble real engineering deliverables  

The project is intended to show **data pipeline design, validation discipline, and production-oriented engineering thinking**.

---

## Portfolio Context

This repository represents the **Local Batch** component of a four-stage data engineering portfolio:

1. Local Batch  
2. Local Streaming  
3. Azure Batch  
4. Azure Streaming  

Each project demonstrates progressively more complex pipeline architectures while maintaining consistent engineering discipline.