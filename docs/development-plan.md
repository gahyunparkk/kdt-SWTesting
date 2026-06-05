# Development Plan

## 1. Development Strategy

This project will be developed with TDD. Each feature starts with acceptance tests mapped to requirement IDs, then production code is added in small increments.

Primary delivery goals:

- Keep core safety logic independent from hardware adapters.
- Make every major decision reproducible through tests and logs.
- Maintain bidirectional traceability from requirements to tests and implementation.
- Keep CI green on every pull request before merge.

## 2. Milestones

### M0 Project Foundation

Target outcome:

- Python package structure exists.
- CI validates tests on pull requests and protected branches.
- Requirements, release policy, development plan, and traceability documents exist.

Requirement coverage:

- NFR-003 Testability
- NFR-004 Maintainability
- NFR-012 CI Compliance

Deliverables:

- `pyproject.toml`
- `src/vehicle_occupancy_alert/`
- `tests/`
- `.github/workflows/pr-validation.yml`
- `docs/requirements.md`
- `docs/development-plan.md`
- `docs/traceability.md`
- `docs/release.md`

### M1 Domain Model and Sensor Abstractions

Target outcome:

- Define vehicle state, sensor reading, confidence, and timestamp models.
- Support deterministic test fixtures for sensor inputs.
- Detect stale, missing, and invalid sensor values.

Requirement coverage:

- FR-001 Vehicle State Detection
- FR-002 Occupancy Signal Collection
- FR-009 Sensor Failure Handling
- FR-012 Simulation Support
- NFR-001 Reliability
- NFR-003 Testability

Expected tests:

- Vehicle state is derived from ignition, movement, and door signals.
- Missing sensor data reduces confidence.
- Stale sensor data is rejected or marked diagnostic.
- Simulation inputs are deterministic.

### M2 Occupancy Inference

Target outcome:

- Infer possible child or pet presence from one or more sensor signals.
- Combine signal confidence without depending on a physical device.
- Suppress transient noise before escalating to risk evaluation.

Requirement coverage:

- FR-003 Child or Pet Presence Inference
- FR-008 False Alarm Suppression
- NFR-001 Reliability
- NFR-010 Performance

Expected tests:

- High-confidence occupancy signal creates a possible presence result.
- Contradictory signals produce reduced confidence.
- Short transient motion does not create a stable presence result.

### M3 Risk Evaluation

Target outcome:

- Calculate risk from occupancy inference, vehicle state, elapsed parked time, cabin temperature, and confidence.
- Support configurable thresholds and sensor weights.

Requirement coverage:

- FR-004 Risk Evaluation
- FR-011 Configuration Management
- NFR-002 Timeliness
- NFR-008 Configurability
- NFR-011 Auditability

Expected tests:

- Risk increases when occupied vehicle is parked and cabin temperature rises.
- Risk remains low when no occupancy is inferred.
- Threshold changes affect alert eligibility without code changes.
- Risk decision records the inputs and versioned configuration.

### M4 Alerting and Incident Lifecycle

Target outcome:

- Trigger alerts when risk exceeds configured thresholds.
- Track incident state from detection through acknowledgement and resolution.
- Escalate when an alert is not acknowledged.

Requirement coverage:

- FR-005 Alert Triggering
- FR-006 Alert Escalation
- FR-007 Alert Acknowledgement
- FR-013 Incident Lifecycle Management
- FR-014 Manual Test Mode

Expected tests:

- Alert is sent once when risk crosses the threshold.
- Unacknowledged alert escalates after the configured interval.
- Acknowledgement suppresses repeat alerts for the same incident.
- Manual test mode verifies channels without creating an emergency incident.

### M5 Observability, Privacy, and Release Readiness

Target outcome:

- Produce structured logs for sensor updates, risk transitions, alerts, acknowledgements, and escalation.
- Ensure secrets are configuration-driven.
- Avoid raw sensitive media storage by default.
- Prepare the first planned release.

Requirement coverage:

- FR-010 Event Logging
- FR-015 Privacy-Aware Data Handling
- NFR-005 Observability
- NFR-006 Security
- NFR-007 Privacy
- NFR-009 Portability

Expected tests:

- Important decision events are emitted with traceable IDs.
- Sensitive values are not logged by default.
- Secret values are loaded from configuration rather than source code.

## 3. Branch and PR Flow

Development should follow the branch policy in `AGENTS.md`.

Recommended flow:

1. Create `feature/<topic>` from `develop`.
2. Add or update tests that reference requirement IDs.
3. Implement the smallest change that passes the tests.
4. Update `docs/traceability.md` when coverage changes.
5. Open a pull request into `develop`.
6. Merge only after CI passes.
7. Promote `develop` to `main` through a release PR.

## 4. Definition of Done

A work item is done when:

- Related requirement IDs are identified.
- Tests exist and pass.
- Implementation is linked from the traceability matrix.
- CI passes in GitHub Actions.
- Safety, privacy, and configuration impacts are documented when relevant.
- Release notes are updated if user-visible behavior changes.

## 5. Near-Term Backlog

| Priority | Item | Requirement IDs | Target Milestone |
| --- | --- | --- | --- |
| P0 | Define vehicle state model | FR-001 | M1 |
| P0 | Define sensor reading model | FR-002, FR-009 | M1 |
| P0 | Add deterministic simulation fixtures | FR-012, NFR-003 | M1 |
| P1 | Implement occupancy inference | FR-003, FR-008 | M2 |
| P1 | Implement risk scoring | FR-004, FR-011 | M3 |
| P1 | Implement alert trigger interface | FR-005 | M4 |
| P2 | Implement acknowledgement and escalation | FR-006, FR-007, FR-013 | M4 |
| P2 | Add structured event logging | FR-010, NFR-005, NFR-011 | M5 |
| P2 | Add privacy and secret handling checks | FR-015, NFR-006, NFR-007 | M5 |
