# BX-009 — KPI, Evidence & Pilot Measurement Map

- **Status:** ACTIVE EXPLORATION BASELINE
- **Stage:** Business — Exploration
- **Date:** 2026-10-07
- **Source basis:** BC-010 + BC-011 + BC-012 + BC-020 + DC-008 + BR-004 + BX-008
- **Purpose:** تعریف نقشه مفهومی KPI، Evidence و Pilot Measurement بدون تعیین Target/Threshold عددی یا Scale Gate Authority.

## Core rules

- Measurement ≠ Decision
- Coverage ≠ Scale Readiness
- Satisfaction ≠ Outcome
- Service Completion ≠ Outcome
- Reporting / AI Analysis ≠ Approved Decision
- Single KPI ≠ Pilot Success
- Missing Evidence ≠ Positive Evidence

## Evaluation levels

چهار سطح ارزیابی منبع:
1. Operational
2. Managerial
3. Economic
4. Social

## KPI families

چهار خانواده اصلی:
- کیفیت خدمات
- رضایت سالمندان و خانواده‌ها
- توسعه سرمایه انسانی
- پایداری اقتصادی و توسعه بازار

Metricهای دقیق و Targetها هنوز OPEN هستند.

## Operational evidence

Candidate dimensions:
- access to service
- referral flow
- service completion
- follow-up
- response timeliness
- unresolved work
- continuity
- documentation completeness
- routing quality

## Service quality evidence

Possible sources:
- Service Delivery Evidence
- Provider Result
- Follow-up
- Satisfaction
- Complaint
- Incident
- Quality Review

Service Quality Evidence با Outcome Evidence یکی نیست.

## Workforce evidence

Source-supported dimensions include:
- elders covered
- follow-up quality
- satisfaction
- registration accuracy
- response speed
- training participation

هیچ Weight، Score، Ranking یا Compensation Formula تعریف نمی‌شود.

## Provider evidence

Candidate dimensions:
- referral response
- completion evidence
- timeliness
- complaint/incident
- satisfaction
- quality review
- rework
- data completeness

Provider KPI Evidence نباید خودکار به Suspension منجر شود.

## Outcome evidence

Outcome باید از Service Delivery جدا سنجیده شود.

Possible sources:
- Baseline
- Reassessment
- Accepted State
- Outcome
- unresolved Need burden
- continuity
- access improvement

Observed Change به‌تنهایی Causal Effect را اثبات نمی‌کند.

## Economic evidence

Candidate evidence:
- funding flow
- operating cost categories
- service/network cost
- provider cost where applicable
- cash-flow evidence
- economic-unit candidates

OPEN:
- Unit Economics definition
- pricing
- margin
- break-even
- settlement formula

## AI evidence

چون AI از روز اول عملیاتی است، Pilot Evidence باید بتواند این موارد را پوشش دهد:
- Use-case activation evidence
- Model Version
- AI Policy Version
- Human Review results
- AI incident evidence
- evaluation evidence
- fail-safe evidence
- provenance completeness

هیچ AI quality threshold تعریف نمی‌شود.

## Dataset / learning evidence

Pilot باید بتواند نشان دهد:
- Training Eligibility Policy Version
- eligible/excluded data evidence
- Dataset Version creation
- lineage completeness
- preparation/curation version
- Dataset incident evidence
- Training/Evaluation lineage where applicable

Dataset Automation ≠ Governance Automation.

## Risk / continuity evidence

Evidence package should include:
- Risk Register status
- Incident evidence
- unresolved remediation
- provider/data/AI/dataset issues
- outage/recovery evidence
- continuity gaps

No Recorded Incident ≠ Proven Safety.
Backup Exists ≠ Recovery Proven.

## Metric Definition Versioning

هر KPI رسمی باید Versionable باشد و در آینده بتواند حداقل این موارد را نگه دارد:
- metric ID/name
- purpose
- numerator/denominator where relevant
- inclusion/exclusion
- time window
- source data
- scope
- owner
- definition version
- effective period
- target/threshold if later approved

Metric Definition Change نباید History را بی‌صدا بازنویسی کند.

## Pilot Evidence Package

Pilot Evidence Package باید بتواند این حوزه‌ها را پوشش دهد:
- scope/population
- service operations
- referral/provider
- quality
- satisfaction
- outcome/reassessment
- workforce
- economics
- risk/incidents
- continuity
- data governance
- AI
- Dataset/Learning
- integrations where applicable
- unresolved decisions/deferrals

## Pilot success boundary

Pilot Success نباید بدون Decision صریح به یک Score واحد تبدیل شود.

Candidate judgment dimensions:
- operational viability
- service quality
- elder experience
- safety/risk
- workforce readiness
- provider readiness
- data/AI readiness
- economic evidence
- governance maturity
- continuity

## Scale Gate inputs

Scale Gate آینده باید بتواند KPI، Outcome، Satisfaction، Risk/Incident، Provider، Workforce، Economic، AI/Dataset و Continuity Evidence را دریافت کند.

Evidence Package ≠ Automatic GO Decision.

GO / CONDITIONAL GO / NO-GO فقط Vocabulary مفهومی است و Rule/Authority آن هنوز OPEN است.

## Reporting boundary

Dashboard یا Report فقط نمایش Evidence است و خود Business Decision نیست.

AI می‌تواند Summary/Flag/Draft ارائه کند، اما KPI Definition، Target، Risk Acceptance یا Scale Gate Decision را خودکار تعیین نمی‌کند.

## Decision triggers

- Pilot KPI catalog: before measurement contract freeze
- Metric definitions: before production measurement
- KPI owner: before official reporting
- Satisfaction method: before satisfaction workflow
- Provider/workforce KPI: before governance use
- AI evaluation metrics: before AI evaluation gate
- Pilot Success Criteria: before Pilot launch
- Scale Gate evidence package: before Pilot exit
- Scale Gate rule/owner: before formal Scale Gate
- Numeric targets: only when real decision/automation requires them

## Explicit non-decisions

BX-009 does not define:
- numeric targets
- thresholds
- weights
- overall score
- provider/caregiver ranking
- incentive formula
- AI evaluation threshold
- Pilot pass score
- Scale Gate authority
- dashboard technology

## Next artifact

**BX-010 — Economics, Funding & Unit-Evidence Map**

## Current stage

- Stage: Business
- KPI/Pilot measurement exploration: ACTIVE
- Business → Technical: NOT READY
- Code: NOT STARTED
- Codex handoff: NOT YET TRIGGERED
