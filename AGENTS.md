# AGENTS.md

## Project Overview

This repository contains a Python-based software project for detecting and alerting when a child or pet may be left inside a vehicle.

The system is intended to combine sensor inputs, decision logic, and alert delivery so that hazardous in-vehicle occupancy situations can be detected early and reported reliably.

## Development Principles

- Use Python as the primary implementation language.
- Follow Test-Driven Development (TDD):
  - Write a failing test first.
  - Implement the smallest change that makes the test pass.
  - Refactor while keeping all tests green.
- Keep business logic testable and separated from hardware, network, and notification adapters.
- Prefer simple, explicit modules over premature abstractions.
- Document safety-related assumptions in code or tests when they affect behavior.

## Expected Project Structure

```text
.
├── src/
│   └── vehicle_occupancy_alert/
├── tests/
├── docs/
│   ├── requirements.md
│   └── release.md
├── .github/
│   └── workflows/
│       └── pr-validation.yml
├── AGENTS.md
└── README.md
```

## TDD Workflow

1. Create or update a test that describes the required behavior.
2. Run the test and confirm it fails for the expected reason.
3. Implement the production code.
4. Run the full test suite.
5. Update `docs/traceability.md` when requirement coverage changes.
6. Update `memory.md` when a project decision or assumption changes.
7. Refactor only after tests pass.

Recommended commands:

```bash
python -m pytest
python -m pytest --cov=src --cov-report=term-missing
```

## Branch Policy

Use protected long-lived branches:

- `main`: Production-ready code only. Releases are created from this branch.
- `develop`: Integration branch for completed features before release.

Use short-lived working branches:

- `feature/<topic>`: New feature work.
- `fix/<topic>`: Bug fixes.
- `test/<topic>`: Test-only improvements.
- `docs/<topic>`: Documentation changes.
- `release/<version>`: Release preparation.

Branch rules:

- Do not commit directly to `main`.
- Pull requests are required for merges into `develop` and `main`.
- PRs into `main` should come from `develop` or `release/<version>`.
- All GitHub Actions checks must pass before merge.
- Prefer squash merge for feature branches.
- Require at least one review before merging into `main`.

## Pull Request Requirements

Every PR should include:

- Purpose of the change.
- Requirement IDs covered by the change.
- Tests added or changed.
- Safety assumptions affected by the change.
- Any known limitations.

For behavior changes, include or update tests before implementation code.

## Traceability

Bidirectional traceability is maintained in:

```text
docs/traceability.md
```

Each requirement should map forward to planned or actual tests and implementation files. Each test or implementation file should map backward to the requirement IDs it supports.

## Project Memory

Project memory is active in:

```text
memory.md
```

Use it to record durable decisions, assumptions, current status, and next steps that future agents should preserve.

## CI Validation

Pull requests are validated by GitHub Actions using:

- Python setup.
- Dependency installation.
- Unit test execution with `pytest`.
- Coverage reporting.
- Static checks when project configuration is available.

The workflow file is located at:

```text
.github/workflows/pr-validation.yml
```

## Release Policy

Releases are documented in `docs/release.md`.

Each release should include:

- Version.
- Release date.
- Summary.
- Functional changes.
- Test evidence.
- Known risks or limitations.

Use semantic versioning:

```text
MAJOR.MINOR.PATCH
```

## Safety Notes

This project supports safety-related alerts, but software detection must be treated as one layer of protection. Requirements, tests, and implementation should avoid implying perfect detection. Any real deployment must validate sensors, alert delivery paths, environmental limits, and failure modes.
