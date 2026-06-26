# Platform Architecture

## Vision

Build an AI-ready Internal Developer Platform that enables secure, self-service application deployment using GitOps.

---

## Architecture Overview

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
Pull Request
    │
    ▼
GitHub Actions (CI)
    │
    ▼
Azure Container Registry
    │
    ▼
ArgoCD (CD)
    │
    ▼
Azure Kubernetes Service
    │
    ├───────────────┐
    │               │
    ▼               ▼
Prometheus      Azure Key Vault
    │
    ▼
Grafana
```

---

## Component Responsibilities

| Component | Responsibility |
|----------|----------------|
| GitHub | Source code, version control |
| GitHub Actions | Build, test, package applications |
| Azure Container Registry | Store container images |
| ArgoCD | Continuous deployment using GitOps |
| AKS | Run containerized workloads |
| Prometheus | Collect metrics |
| Grafana | Visualize metrics |
| Azure Key Vault | Manage secrets |

---

## Deployment Flow

1. Developer pushes code.
2. Pull request is reviewed.
3. GitHub Actions builds the application.
4. Docker image is pushed to ACR.
5. Kubernetes manifests are updated.
6. ArgoCD detects changes.
7. Application is deployed to AKS.
8. Prometheus collects metrics.
9. Grafana visualizes system health.

---

## Platform Principles

- Git is the single source of truth.
- Everything is automated.
- Infrastructure is reusable.
- Developers use self-service workflows.
- Observability is built in.
- Security is enforced by default.