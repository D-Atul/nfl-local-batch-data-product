# NFL Local Batch Data Product

Version: v1.1 (Hardening In Progress)

---

## Overview

This project implements a deterministic local batch data product over historical NFL game data.

The pipeline validates raw inputs against an explicit contract, applies controlled transformations, computes season-level metrics, and publishes curated outputs along with an auditable run log.

The goal is reliability and reproducibility — not analytics exploration.

---

## Product Guarantees

The system guarantees:

- **Contract-first validation** of raw inputs using explicit schema rules
- **Fail-fast behaviour** on validation or transformation violations
- **Row-count preservation** during transformation
- **Deterministic metric computation**
- **Atomic publish of outputs**
- **Structured run logging for auditability**
- **Overwrite-based rerun behaviour (idempotent at run level)**

If validation fails, no partial outputs are considered valid.

---

## Non-Goals

This project does not:

- Perform forecasting or prediction
- Generate rankings or recommendations
- Provide betting logic
- Modify or silently repair corrupted data
- Perform cross-era franchise normalization

It is a data product, not an analytics notebook.

---

## Architecture

Pipeline stages:

1. Raw CSV ingestion
2. Raw contract validation
3. Controlled transformation
4. Reconciliation check (row preservation)
5. Metric computation
6. Metric contract validation
7. Atomic publish to output directory
8. Structured JSON run log emission

Data flow:

```
Raw → Validate → Transform → Reconcile → Metrics → Validate → Publish → Log
```

---

## How to Run

From project root:

```bash
python -m src.runner.run_local_batch
```

> Next version will introduce CLI argument support.

---

## Outputs

Outputs are written to the `outputs/` directory:

### 1. `team_outcomes.parquet`

Grain: `(team, season)`

Includes:
- `games_played`
- `wins`
- `losses`
- `ties`
- `points_for`
- `points_against`

### 2. `season_summaries.parquet`

Grain: `(season)`

Includes:
- `total_games`
- `playoff_games`
- `regular_games`

### 3. `venue_neutral_counts.parquet`

Grain: `(season)`

Includes:
- `neutral_site_games`

### 4. Run Log

Each run produces a structured JSON log containing:

- `run_id`
- `input row count`
- `output row counts`
- `status` (`SUCCESS` / `FAILED`)
- `error message` (if applicable)

This provides minimal but sufficient audit traceability.

---

## Determinism & Rerun Behaviour

- Outputs are recomputed from raw input each run
- Previous outputs are overwritten
- No hidden state is maintained
- Identical input produces identical output

The system is deterministic by logic, not infrastructure tricks.

---

## Failure Modes

The pipeline fails when:

- Raw contract validation fails
- Transformation drops or duplicates rows
- Metric contract validation fails
- Unexpected runtime exception occurs

On failure:

- Status is marked `FAILED` in run log
- No partially validated dataset is considered valid

---

## Repository Structure

```
src/
  contracts/
  metrics/
  runner/
framework/
raw_data/
logs/
outputs/
notebook.ipynb
requirements.txt
```

---

## Version History

| Version | Description |
|---------|-------------|
| v1.0.0 | Baseline deterministic batch pipeline |
| v1.1.0 | Hardening phase (tests, dependency pinning, CLI, CI) |

---

This repository is part of a broader portfolio demonstrating contract-first, audit-aware data engineering practices suitable for production-style batch systems.