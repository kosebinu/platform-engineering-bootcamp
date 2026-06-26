# Application Template Design

## Purpose

The Application Template is the standard deployment mechanism for all Kubernetes applications within the platform.

Its purpose is to provide developers with a simple, secure, and consistent way to deploy applications without requiring Kubernetes expertise.

---

# Design Principles

1. Simplicity over flexibility
2. Secure by default
3. Sensible defaults
4. Platform-owned infrastructure
5. Developer-owned application configuration

---

# Developer Responsibilities

Developers should only configure:

- Application name
- Team
- Environment
- Container image
- Image tag
- Replica count

---

# Platform Responsibilities

The platform automatically manages:

- Deployment
- Service
- Labels
- Annotations
- Liveness probes
- Readiness probes
- Resource defaults
- Security context
- Network policies
- Service accounts
- ConfigMaps
- Secrets integration
- Monitoring labels

---

# Platform Goal

A developer should be able to deploy a production-ready application by editing only one file:

values.yaml