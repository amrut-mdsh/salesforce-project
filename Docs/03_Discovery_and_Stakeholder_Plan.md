# Discovery and stakeholder engagement

**Standalone-copy scope:** The original documentation refers to a shared Local_System workbench that is not included in this extracted project. Its workflows, screenshots, and historical test claims are not reproducible here. The local CSV/SQL runner and snapshot checks are available in `scripts/`; see [the audit scope](../AUDIT.md). Native dashboard refresh and business approval remain unverified.


## Workshop objective

Resolve the reporting decision, the source grain, metric ownership, and the evidence needed to justify action. This is a **proposed facilitation plan**, not a transcript of meetings that occurred.

## Proposed 60-minute discovery workshop

| Minutes | Activity | Output |
| --- | --- | --- |
| 0-10 | Sponsor describes the decision and current pain | Decision statement and scope boundary |
| 10-25 | Walk through actual fields and sample records | Confirmed grain, source ownership, key gaps |
| 25-40 | Agree KPI arithmetic and exception behavior | Proposed KPI dictionary and acceptance examples |
| 40-50 | Review process ownership and access | Role matrix and control responsibilities |
| 50-60 | Resolve priorities and assign open questions | Decision log, RAID owners, and next review |

## Domain discovery questions

| Role | Question | Current evidence / proposed response |
| --- | --- | --- |
| Sales VP | Is weighted amount booked revenue? | No; it is a probability-weighted view of open opportunities. |
| Sales Ops | Can win rate be calculated? | Closed outcomes alone do not establish a cohort or time interval. |
| CRM Admin | Which fields block a forecast? | Close date, snapshot date, owner, and stage history are missing. |
| Account Executive | Why are probabilities assigned? | Stage conventions are supplied but not empirically calibrated. |

Responses above summarize what the current extract supports. They are not quotations from real stakeholders. In a real engagement, capture the respondent, date, evidence, unresolved question, and approval separately.

## Engagement strategy

| Role | Position | Influence | Interest | Engagement |
| --- | --- | --- | --- | --- |
| Sponsor | VP Sales | High | High | Decision review at discovery and release |
| Business owner | Sales Operations Manager | High | High | Weekly working session and exception triage |
| Primary user | Revenue Operations Analyst | Medium | High | Prototype walkthrough and usability review |
| Data owner | Source System Administrator | High | Medium | Data-contract review and refresh triage |
| Engineering | Data / BI Engineer | Medium | High | Backlog refinement and technical review |
| Control reviewer | Finance / Security Reviewer | High | Medium | Control review before release |

High-influence approvers receive concise decision briefs before scope and release gates. Users receive a prototype walkthrough with denominators visible and exercises involving missing data. Engineering receives the canonical schema, exact SQL, acceptance fixtures, and error contract. Control reviewers receive provenance, access design, reconciliation, and unresolved exception evidence.

## RACI for the proposed implementation

| Activity | Sponsor | Business owner | BA | Engineer | Control reviewer |
| --- | --- | --- | --- | --- | --- |
| Scope and release decision | A | C | R | C | C |
| KPI definitions | C | A | R | C | C |
| Source contract and transforms | I | C | C | A/R | C |
| UAT execution and disposition | I | A | R | C | C |
| Access implementation | I | C | C | R | A |
| Reconciliation exception approval | C | A | R | C | C |

A is accountable, R responsible, C consulted, I informed. Confirm actual roles and authority before execution.

## Communication and escalation

- Weekly working session: review data exceptions, ambiguous requirements, and backlog changes. BA publishes proposed decisions with evidence links and records unresolved disagreements.
- Prototype review: the user completes a reporting task and explains the meaning of a weighted rate. Record task completion and interpretation problems rather than claiming adoption.
- Release review: the sponsor receives open Must requirements, source reconciliation results, access-test evidence, UAT disposition, and rollback readiness.
- Escalation: a failed control total, missing business key, or unauthorized export blocks publication until the accountable owner records an approved disposition. A label change that changes business meaning requires requirement and test updates.

## Conflict-resolution example

If operations wants the report published immediately but the control reviewer questions a rate or source total, the BA shows numerator, denominator, source hash, query result, and independent control. Capture the impact of delay and the consequence of publication. The sponsor decides scope/schedule after the control owner resolves the evidence; the BA does not remove an exception merely to meet a deadline.
