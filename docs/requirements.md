# Requirements

## 1. Purpose

This project develops a Python-based system that detects whether a child or pet may remain inside a parked vehicle and sends alerts to reduce the risk of heatstroke, hypothermia, or delayed rescue.

## 2. Scope

The first version focuses on software decision logic, testable sensor abstraction, and alert orchestration. Physical sensor integration may be implemented through adapters after the core behavior is verified by tests.

## 3. Assumptions

- The vehicle can provide or simulate ignition state, door state, cabin temperature, motion, seat occupancy, sound, or image-derived signals.
- The system can determine whether the vehicle is parked or recently stopped.
- At least one alert channel is available, such as mobile notification, SMS, audible alarm, or cloud webhook.
- Sensor readings may be noisy, delayed, unavailable, or contradictory.
- The system must favor timely warning while reducing repeated false alarms.

## 4. Functional Requirements

### FR-001 Vehicle State Detection

The system shall determine whether the vehicle is moving, parked, recently stopped, or powered off based on available input signals.

### FR-002 Occupancy Signal Collection

The system shall receive occupancy-related signals through abstract sensor interfaces, including support for seat occupancy, cabin motion, sound, temperature, and optional camera-derived detection.

### FR-003 Child or Pet Presence Inference

The system shall infer a possible child or pet presence using one or more configured signals.

### FR-004 Risk Evaluation

The system shall calculate risk based on occupancy inference, vehicle state, elapsed time since parking, cabin temperature, and sensor confidence.

### FR-005 Alert Triggering

The system shall trigger an alert when risk exceeds a configured threshold.

### FR-006 Alert Escalation

The system shall support alert escalation if the first alert is not acknowledged within a configured time window.

### FR-007 Alert Acknowledgement

The system shall record acknowledgement of an alert and stop repeated alerts for the same incident unless risk increases again.

### FR-008 False Alarm Suppression

The system shall apply configurable debounce and confirmation rules to reduce alerts caused by transient sensor noise.

### FR-009 Sensor Failure Handling

The system shall detect missing, stale, or invalid sensor data and adjust confidence or trigger a diagnostic warning.

### FR-010 Event Logging

The system shall log important events, including sensor updates, risk transitions, alert attempts, acknowledgements, and escalation decisions.

### FR-011 Configuration Management

The system shall support configuration for thresholds, sensor weights, alert channels, escalation timing, and debounce windows.

### FR-012 Simulation Support

The system shall provide a way to run deterministic simulations for tests and demos without physical vehicle hardware.

### FR-013 Incident Lifecycle Management

The system shall group related detections and alerts into a single incident from initial detection through resolution.

### FR-014 Manual Test Mode

The system shall support a test mode that verifies alert channels without creating a real emergency incident.

### FR-015 Privacy-Aware Data Handling

If image, audio, or personally sensitive signals are used, the system shall process only the minimum data needed for detection and avoid storing raw sensitive data by default.

## 5. Non-Functional Requirements

### NFR-001 Reliability

The system should continue operating when one non-critical sensor is unavailable, while clearly recording reduced confidence.

### NFR-002 Timeliness

The system should evaluate risk within 5 seconds of receiving new relevant sensor data under normal operating conditions.

### NFR-003 Testability

Core detection, risk scoring, alert escalation, and incident lifecycle logic shall be covered by automated tests and designed without direct dependency on physical hardware.

### NFR-004 Maintainability

The codebase shall use clear module boundaries for sensors, inference, risk evaluation, alerting, configuration, and persistence.

### NFR-005 Observability

The system shall expose logs or structured events sufficient to diagnose alert decisions during development and validation.

### NFR-006 Security

Credentials, API keys, phone numbers, and webhook endpoints shall not be hard-coded. Secrets must be supplied through secure configuration.

### NFR-007 Privacy

The system shall minimize collection and retention of personal data, especially image, audio, location, and contact information.

### NFR-008 Configurability

Safety thresholds and escalation rules shall be configurable without changing production code.

### NFR-009 Portability

The core Python package should run on common development environments and be portable to embedded Linux or vehicle gateway environments where feasible.

### NFR-010 Performance

The core decision logic should be lightweight enough to run on low-power edge hardware.

### NFR-011 Auditability

Safety-relevant decisions should be reproducible from logged inputs, configuration, and version information.

### NFR-012 CI Compliance

All pull requests shall pass automated validation before merge.

## 6. Initial Acceptance Criteria

- Unit tests exist for normal detection, no-occupancy, sensor failure, alert escalation, acknowledgement, and debounce scenarios.
- A simulated incident can move through detection, alert, acknowledgement, and resolution states.
- Pull requests run GitHub Actions validation automatically.
- Release notes are maintained for each published version.

## 7. Out of Scope for Initial Version

- Production-certified automotive safety compliance.
- Guaranteed detection in all environmental conditions.
- Direct integration with every vehicle manufacturer API.
- Emergency service dispatch without explicit product and legal review.
