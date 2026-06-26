# ADR-0001: Standardize Kubernetes Deployments with Helm

## Status

Accepted

## Context

Development teams currently maintain their own Kubernetes manifests, leading to inconsistent deployments, duplicated configuration, and operational risk.

## Decision

The Platform Team will provide a reusable Helm chart that serves as the standard deployment mechanism for Kubernetes applications.

Developers will configure applications using `values.yaml` instead of maintaining raw Kubernetes manifests.

## Consequences

### Positive

- Consistent deployments
- Reduced duplication
- Easier upgrades
- Standardized security
- Faster onboarding

### Negative

- Initial learning curve for Helm
- Platform Team responsible for maintaining the chart

## Owner

Platform Engineering Team