# ADR-0002: Expose a Minimal Public Platform API

## Status

Accepted

---

## Context

The Platform Team is responsible for providing a standardized Helm chart that enables development teams to deploy applications consistently across Kubernetes environments.

One design question arose during the implementation of the platform:

**How much Kubernetes configuration should be exposed through `values.yaml`?**

A naïve approach would expose nearly every Kubernetes option, allowing developers to customize deployments extensively. While this provides flexibility, it also increases complexity, creates inconsistent deployments, and expands the long-term maintenance burden of the platform.

The Platform Team must balance flexibility with simplicity while maintaining security and operational consistency.

---

## Decision

The Platform Team will expose only a minimal set of configuration options through `values.yaml`.

Developers should configure only application-specific information such as:

* Application name
* Team ownership
* Environment
* Container image
* Image tag
* Replica count

All infrastructure-related configuration will be managed by the Platform Team.

Examples include:

* Resource requests and limits
* Liveness and readiness probes
* Security contexts
* Service accounts
* Labels and annotations
* Network policies
* Monitoring configuration
* Secrets integration
* Pod security standards

---

## Rationale

A minimal public API provides several important benefits.

### Improved Developer Experience

Developers should focus on building business applications rather than learning Kubernetes internals.

Reducing the number of required configuration options lowers cognitive load and makes the platform easier to adopt.

### Consistency

Standardized deployments ensure that all applications follow the same operational, security, and monitoring standards.

This reduces production incidents caused by inconsistent configurations.

### Maintainability

Every exposed configuration option becomes part of the platform's public API.

Supporting unnecessary configuration options increases documentation, testing, backward compatibility requirements, and long-term maintenance costs.

By exposing only essential configuration, the Platform Team retains the ability to improve platform internals without impacting application teams.

### Security

Security controls should be enforced by the platform rather than delegated to individual development teams.

Providing secure defaults reduces the likelihood of misconfiguration and improves organizational compliance.

### Platform Evolution

Keeping the public API intentionally small allows the platform to evolve over time while minimizing breaking changes for application teams.

---

## Consequences

### Positive

* Simpler developer experience
* Consistent Kubernetes deployments
* Reduced operational risk
* Easier onboarding
* Smaller long-term maintenance burden
* Stronger security posture
* Faster platform evolution

### Negative

* Developers have less direct control over Kubernetes configuration.
* Platform engineers must carefully choose sensible defaults.
* Advanced use cases may occasionally require platform enhancements rather than application-level customization.

---

## Alternatives Considered

### Expose All Kubernetes Configuration

This approach provides maximum flexibility but significantly increases platform complexity, creates inconsistent deployments, and makes long-term maintenance more difficult.

The Platform Team rejected this option because it shifts Kubernetes expertise onto application developers.

### Allow Unlimited Overrides

Allowing unrestricted overrides gives developers complete control but weakens platform standardization and increases operational risk.

This option was also rejected.

---

## Decision Summary

The Platform Team will provide an opinionated platform that exposes only the configuration developers genuinely need while managing infrastructure concerns internally.

This approach aligns with the platform engineering principles of reducing cognitive load, improving developer productivity, enforcing organizational standards, and enabling secure, repeatable deployments.