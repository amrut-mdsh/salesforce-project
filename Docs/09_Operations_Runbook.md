# Local analysis runbook

## Requirements

Python 3.10+ with SQLite 3.25+ (window functions). No network access or credentials are needed. Run from this project directory; scripts resolve inputs relative to their own location.

```sh
python3 scripts/run_analysis.py
python3 scripts/validate.py
```

The first command loads only this project's CSV sources into an in-memory SQLite database and executes Q01–Q05. Generated CSVs go to ignored `artifacts/`. The second command compares query headers, row counts and all values with the preserved `Analysis/` snapshots. Numeric tolerance is 1e-6 absolute / 1e-9 relative. Neither command overwrites input data or historical results.

## Scope and failures

Missing columns, blank required values, non-finite numbers and fractional integer fields stop ingestion. A snapshot mismatch is a failure requiring investigation; do not change reference results solely to pass a test. Inspect the CSV, field mapping in `scripts/sources.json`, and relevant SQL together.

The original shared Local_System server, persistent UAT application and external Quality test suite were not supplied. This copy does not implement those workflows. Historical Delivery and UAT records are portfolio examples, not independently verified approvals. Native Power BI refresh, Excel recalculation and CRM configuration require their respective applications and separate validation.

Retain source provenance, confirm rights to data and assets, reconcile business definitions, and obtain real stakeholder approval before any production use. See [audit scope](../AUDIT.md).
