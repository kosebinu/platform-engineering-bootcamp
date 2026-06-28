# Platform Engineering Bootcamp

This repository documents my journey from DevOps Engineer to Platform Engineer by designing and building an AI-ready Internal Developer Platform.

The goal is to build a production-style platform that enables developers to deploy, monitor, and operate applications on Azure Kubernetes Service using secure, repeatable, and self-service workflows.

---

## Platform Vision

Build an Internal Developer Platform that provides developers with a Golden Path for deploying applications to Kubernetes.

The platform will support:

- Infrastructure as Code with Terraform
- Azure Kubernetes Service
- GitOps with ArgoCD
- CI/CD with GitHub Actions
- Observability with Prometheus and Grafana
- Secrets management with Azure Key Vault
- Secure multi-environment deployments
- Future AI infrastructure capabilities

---

## Architecture Overview

```text
Developer
    |
    v
GitHub Repository
    |
    v
Pull Request
    |
    v
GitHub Actions
    |
    v
Azure Container Registry
    |
    v
ArgoCD
    |
    v
Azure Kubernetes Service
    |
    +--> Prometheus
    |
    +--> Grafana
    |
    +--> Azure Key Vault