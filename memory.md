# Project Memory

This file is active for project continuity. Keep it updated when decisions, assumptions, milestones, or traceability status change.

## Current Objective

Build a Python-based, TDD-driven vehicle occupancy alert system that detects possible children or pets left in a parked vehicle and sends appropriate alerts.

## Active Working Agreements

- Use TDD for all behavior changes.
- Keep core logic independent from physical hardware integrations.
- Maintain bidirectional traceability in `docs/traceability.md`.
- Use branch policy from `AGENTS.md`.
- Validate pull requests through GitHub Actions before merge.
- Update `docs/release.md` before publishing releases.

## Key Decisions

| Date | Decision | Reason |
| --- | --- | --- |
| 2026-06-05 | Python is the primary implementation language. | User requested Python development. |
| 2026-06-05 | Core logic will be separated from sensor, alert, and persistence adapters. | Enables TDD and hardware-independent validation. |
| 2026-06-05 | Requirements use stable IDs such as `FR-001` and `NFR-001`. | Supports bidirectional traceability. |
| 2026-06-05 | GitHub Actions validates tests on `main`, `develop`, and pull requests. | Enforces merge quality gates. |

## Current Status

- Project documentation exists.
- CI workflow exists.
- Minimal Python package and smoke test exist.
- Development plan exists.
- Bidirectional traceability matrix exists.
- M1 domain model and sensor abstractions are implemented.
- M1 tests cover vehicle state derivation, sensor reading validation, sensor health, and deterministic simulation scenarios.

## Next Steps

1. Create `develop` branch and protect `main` in repository settings.
2. Implement M2 occupancy inference using TDD.
3. Update traceability status as tests and implementation are added.
4. Add release notes for `v0.1.0` when M1-M4 behavior is usable.

## Open Questions

- Which alert channels should be prioritized first: local alarm, SMS, mobile push, webhook, or another channel?
- Which sensor inputs will be available in the initial demo environment?
- Should camera or audio processing be included in the first release, or deferred for privacy and scope control?
