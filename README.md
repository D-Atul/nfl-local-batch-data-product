# NFL Local Batch Data Product

This repository contains a local, deterministic batch data product built over historical NFL game events.

The purpose of this project is to demonstrate how a data engineer designs, validates, executes, and proves a batch system under explicit constraints — without overengineering or analytical cosplay.

The system is contract-first, fail-fast, and evidence-driven.

---

## What this project is

- A local batch pipeline over historical NFL game events
- Events-only metric computation (no enrichment joins)
- Deterministic reruns with explicit guarantees
- Evidence-driven execution using a single source of truth

This is a **data engineering portfolio project**, not an exploratory analysis notebook.

---

## What this project is not

- No prediction, forecasting, or optimisation
- No betting, strategy, or ranking recommendations
- No deduplication or silent data fixing
- No incremental processing or backfills
- No cloud, orchestration, or distributed claims

---

## Data scope

- Primary entity: NFL game events (one row per match)
- Reference entity: Teams (present but unused in computation)
- Source: Static historical dataset

Metric computation operates exclusively on the Events entity.
Reference datasets are not joined and are not enforced via contracts.

---

## Guarantees

- Contract-first execution  
  Raw inputs and all published outputs are validated via explicit contracts.
  Contract violations fail execution immediately.

- Deterministic reruns  
  Identical inputs produce identical outputs.
  No time-dependent logic or hidden state.

- Reconciliation invariant  
  Transformations preserve event cardinality (one row per match).

- No partial publish  
  Outputs are written via a staged publish (temporary write followed by rename).
  Either the previous outputs remain, or the new outputs fully replace them.

- Single source of truth for evidence  
  One run log (`logs/run_<id>.json`) captures inputs, row counts, validations,
  outputs, execution status, and errors.

---

## Repository structure

framework/
  NFL_Local_Batch_Framework_v1.ipynb

src/
  contracts/
  pipelines/
  runner/
    run_local_batch.py

raw_data/
  spreadspoke_scores.csv
  nfl_teams.csv

outputs/
  metrics/

logs/
  run_c547f0fcc34940d7b64c71c01c0ff19c.json

evidence_notebook.ipynb

---

## How to run

From the project root:

python -m src.runner.run_local_batch

---

## Outputs

Published to outputs/metrics:

- team_outcomes.parquet
- season_summaries.parquet
- venue_neutral_counts.parquet

Each execution also produces a run log in logs/ as the authoritative evidence artifact.

---

## Evidence notebook

notebook.ipynb is a read-only evidence notebook.

It loads the latest run log, summarises execution and validation outcomes,
and reads published outputs using paths recorded in the run log.
It performs no mutation or recomputation.

---

## Design philosophy

This project intentionally avoids premature abstraction and overengineering.

The focus is first-job readiness with a senior mindset:
clear scope, explicit guarantees, and proof over claims.
