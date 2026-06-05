# Bidirectional Traceability Matrix

## 1. Purpose

This document keeps requirements, development work, tests, and implementation linked in both directions.

Use it during TDD:

- Before coding, add the requirement ID to the planned test.
- After coding, update the implementation reference.
- During review, confirm each changed requirement has tests and source links.

Status values:

- `Planned`: Not implemented yet.
- `Tested`: Test exists but implementation may still be evolving.
- `Implemented`: Source and tests both exist.
- `Deferred`: Intentionally postponed.

## 2. Forward Traceability: Requirements to Work Products

| Requirement ID | Requirement Summary | Milestone | Planned Tests | Implementation | Status |
| --- | --- | --- | --- | --- | --- |
| FR-001 | Vehicle state detection | M1 | `tests/domain/test_vehicle_state.py` | `src/vehicle_occupancy_alert/domain/vehicle_state.py` | Planned |
| FR-002 | Occupancy signal collection | M1 | `tests/domain/test_sensor_reading.py` | `src/vehicle_occupancy_alert/domain/sensors.py` | Planned |
| FR-003 | Child or pet presence inference | M2 | `tests/inference/test_occupancy.py` | `src/vehicle_occupancy_alert/inference/occupancy.py` | Planned |
| FR-004 | Risk evaluation | M3 | `tests/risk/test_risk_evaluator.py` | `src/vehicle_occupancy_alert/risk/evaluator.py` | Planned |
| FR-005 | Alert triggering | M4 | `tests/alerting/test_alert_trigger.py` | `src/vehicle_occupancy_alert/alerting/service.py` | Planned |
| FR-006 | Alert escalation | M4 | `tests/alerting/test_escalation.py` | `src/vehicle_occupancy_alert/alerting/escalation.py` | Planned |
| FR-007 | Alert acknowledgement | M4 | `tests/incidents/test_acknowledgement.py` | `src/vehicle_occupancy_alert/incidents/lifecycle.py` | Planned |
| FR-008 | False alarm suppression | M2 | `tests/inference/test_debounce.py` | `src/vehicle_occupancy_alert/inference/debounce.py` | Planned |
| FR-009 | Sensor failure handling | M1 | `tests/domain/test_sensor_health.py` | `src/vehicle_occupancy_alert/domain/sensor_health.py` | Planned |
| FR-010 | Event logging | M5 | `tests/observability/test_events.py` | `src/vehicle_occupancy_alert/observability/events.py` | Planned |
| FR-011 | Configuration management | M3 | `tests/config/test_settings.py` | `src/vehicle_occupancy_alert/config/settings.py` | Planned |
| FR-012 | Simulation support | M1 | `tests/simulation/test_scenarios.py` | `src/vehicle_occupancy_alert/simulation/scenarios.py` | Planned |
| FR-013 | Incident lifecycle management | M4 | `tests/incidents/test_lifecycle.py` | `src/vehicle_occupancy_alert/incidents/lifecycle.py` | Planned |
| FR-014 | Manual test mode | M4 | `tests/alerting/test_manual_mode.py` | `src/vehicle_occupancy_alert/alerting/manual_test.py` | Planned |
| FR-015 | Privacy-aware data handling | M5 | `tests/privacy/test_data_minimization.py` | `src/vehicle_occupancy_alert/privacy/policy.py` | Planned |
| NFR-001 | Reliability under sensor loss | M1-M2 | `tests/domain/test_sensor_health.py` | Domain and inference modules | Planned |
| NFR-002 | Risk evaluation timeliness | M3 | `tests/risk/test_performance.py` | `src/vehicle_occupancy_alert/risk/evaluator.py` | Planned |
| NFR-003 | Testability | M0-M5 | `tests/` | Core modules under `src/` | Implemented |
| NFR-004 | Maintainability | M0-M5 | PR review checklist | Package structure and module boundaries | Implemented |
| NFR-005 | Observability | M5 | `tests/observability/test_events.py` | `src/vehicle_occupancy_alert/observability/events.py` | Planned |
| NFR-006 | Security | M5 | `tests/config/test_secret_handling.py` | `src/vehicle_occupancy_alert/config/settings.py` | Planned |
| NFR-007 | Privacy | M5 | `tests/privacy/test_data_minimization.py` | `src/vehicle_occupancy_alert/privacy/policy.py` | Planned |
| NFR-008 | Configurability | M3 | `tests/config/test_settings.py` | `src/vehicle_occupancy_alert/config/settings.py` | Planned |
| NFR-009 | Portability | M5 | CI matrix | `pyproject.toml` and package structure | Implemented |
| NFR-010 | Performance | M2-M3 | `tests/risk/test_performance.py` | Inference and risk modules | Planned |
| NFR-011 | Auditability | M3-M5 | `tests/observability/test_events.py` | Risk and observability modules | Planned |
| NFR-012 | CI compliance | M0-M5 | GitHub Actions run | `.github/workflows/pr-validation.yml` | Implemented |

## 3. Reverse Traceability: Work Products to Requirements

| Work Product | Requirement IDs |
| --- | --- |
| `.github/workflows/pr-validation.yml` | NFR-003, NFR-009, NFR-012 |
| `pyproject.toml` | NFR-003, NFR-004, NFR-009 |
| `src/vehicle_occupancy_alert/__init__.py` | NFR-003, NFR-004 |
| `tests/test_package.py` | NFR-003, NFR-012 |
| `docs/development-plan.md` | NFR-004, NFR-012 |
| `docs/requirements.md` | All requirement definitions |
| `docs/release.md` | NFR-011, NFR-012 |
| `docs/traceability.md` | NFR-003, NFR-004, NFR-011, NFR-012 |

## 4. Test Naming Rule

New tests should include the requirement ID in either the test name, test docstring, or a nearby comment.

Example:

```python
def test_fr_005_alert_is_triggered_when_risk_exceeds_threshold():
    ...
```

## 5. Review Checklist

- Every changed requirement has at least one test reference.
- Every new test maps back to one or more requirement IDs.
- Every implementation file maps back to requirements in the reverse traceability table.
- Deferred requirements have a reason in `memory.md` or the relevant issue.
