# Day 1: Platform Engineering Mindset

## What is Platform Engineering?

Platform Engineering is the practice of building reusable tools, workflows, and systems that allow developers to build, deploy, monitor, and operate applications safely and efficiently.

## Difference Between DevOps and Platform Engineering

DevOps focuses on automation, CI/CD, infrastructure, monitoring, and collaboration.

Platform Engineering builds an internal platform that gives developers self-service access to those capabilities.

## My Platform Engineering Goal

My goal is to build an AI-ready Internal Developer Platform using:

- Azure
- AKS
- Terraform
- GitHub Actions
- ArgoCD
- Prometheus
- Grafana
- Azure Key Vault

## What My Platform Should Help Developers Do

Developers should be able to:

1. Push application code.
2. Automatically build and test the app.
3. Build a Docker image.
4. Deploy to Kubernetes through GitOps.
5. Access logs, metrics, and dashboards.
6. Use secrets securely.
7. Roll back deployments safely.

## Golden Path

The Golden Path for this platform is:

Developer pushes code → GitHub Actions builds image → Terraform provisions infrastructure → ArgoCD deploys app to AKS → Prometheus and Grafana monitor the app.