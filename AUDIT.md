# Local audit — Salesforce_Project

## Changes

Repaired standalone ingestion and SQL execution; all five query snapshots match. Corrected claims about absent Salesforce deployment assets and the unavailable shared application. Removed three unrelated planning screenshots and an empty README; privacy-masked browser details while preserving opportunity-owner data.

## Validation performed

- **PASS** — Salesforce_Project/scripts/run_analysis.py: Python syntax
- **PASS** — Salesforce_Project/scripts/validate.py: Python syntax
- **PASS** — SQL snapshots: PASS Q01: all 1 result rows match the supplied snapshot; PASS Q02: all 1 result rows match the supplied snapshot; PASS Q03: all 6 result rows match the supplied snapshot; PASS Q04: all 8 result rows match the supplied snapshot; PASS Q05: all 0 result rows match the supplied snapshot; PASS: snapshot reconciliation; not business sign-off or native dashboard validation.
- **PASS** — portable execution: Q01: 1 rows; Q02: 1 rows; Q03: 6 rows; Q04: 8 rows; Q05: 0 rows
- **PASS** — full SQL packs: All SQL files executed successfully with the canonical schema.
- **PASS** — blank ingestion: Invalid input rejected before query execution.
- **PASS** — nonfinite ingestion: Invalid input rejected before query execution.
- **PASS** — fractional ingestion: Invalid input rejected before query execution.
- Archive members and XML were parsed where present; images decoded and screenshots reviewed. Notebook/JSON syntax and local paths were checked.
- No plaintext secret candidates, personal contact emails, promotional GitHub/LinkedIn profile links or machine-home paths were detected in the final scanned text/package content. This is a bounded local pattern scan, not proof that opaque native models contain no sensitive data.

## Remaining limitations

No Salesforce org, API credentials, configuration export or deployable Salesforce implementation was supplied. Historical screenshot figures differ from the CSV and are explicitly labeled. Original owner names inside report rows are preserved as analytical record content. Source licensing and redistribution rights remain unconfirmed.

## Provenance and execution scope

Original source datasets and SQL are retained. No Git history was present in the five extracted folders. Original Downloads folders match their pre-copy SHA-256 hashes. No GitHub command, authentication, repository creation, commit, push or upload was performed.

Original authorship and legally required notices remain in [ATTRIBUTION.md](ATTRIBUTION.md). Personal UI redactions do not replace author attribution.
