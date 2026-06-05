# Release Page

## Current Release

No production release has been published yet.

## Versioning

This project uses semantic versioning:

```text
MAJOR.MINOR.PATCH
```

- `MAJOR`: Incompatible changes to public interfaces, incident behavior, or alert contracts.
- `MINOR`: New features or detection capabilities that remain backward compatible.
- `PATCH`: Bug fixes, test updates, and small reliability improvements.

## Release Checklist

Before publishing a release:

- Confirm all pull request checks pass.
- Run the full test suite locally or in CI.
- Review requirements affected by the release.
- Confirm alert behavior is covered by tests.
- Update this release page.
- Tag the release from `main`.
- Publish GitHub Release notes.

## Release Notes Template

```text
Version:
Release date:
Branch:
Commit:

Summary:

Functional changes:

Non-functional changes:

Test evidence:

Known limitations:

Rollback notes:
```

## Release History

### v0.1.0 - Planned

Initial development release target.

Planned scope:

- Core sensor abstraction.
- Vehicle state model.
- Occupancy inference model.
- Risk evaluation logic.
- Alert orchestration.
- Incident lifecycle.
- Unit test suite using TDD.
- Pull request validation through GitHub Actions.
