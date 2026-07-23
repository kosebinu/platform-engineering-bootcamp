# Golden Paths

## Purpose

This document defines the organization's Golden Path strategy for software development and delivery within the Internal Developer Platform (IDP).

Golden Paths provide engineering teams with standardized, opinionated, and fully supported workflows for building, deploying, and operating software.

The objective is to reduce complexity, improve developer productivity, and ensure that every new service adheres to the organization's engineering standards.

---

# What is a Golden Path?

A Golden Path is the recommended and fully supported approach for creating, deploying, and operating software on the Internal Developer Platform.

Rather than requiring every team to design its own workflows, Golden Paths provide reusable patterns that incorporate platform best practices.

Golden Paths are:

- Opinionated
- Automated
- Self-service
- Secure by default
- Observable by default
- Continuously maintained

Engineering teams remain free to choose alternative approaches when necessary, but Golden Paths receive the highest level of Platform Team support.

---

# Why Golden Paths Exist

As engineering organizations scale, inconsistency becomes a significant operational risk.

Without standardized workflows:

- Teams create different project structures.
- Deployment processes vary between applications.
- Security controls are implemented inconsistently.
- Monitoring is often incomplete.
- Documentation quality varies.
- Operational support becomes difficult.

Golden Paths solve these challenges by providing consistent, repeatable workflows.

Primary objectives include:

- Reduce cognitive load
- Accelerate developer onboarding
- Improve deployment consistency
- Enforce engineering standards
- Reduce production incidents
- Improve operational support
- Increase platform adoption

---

# Standard Developer Workflow

The Golden Path defines the recommended lifecycle for building and deploying a new service.

```text
Developer

↓

Open Internal Developer Portal

↓

Select Software Template

↓

Generate Repository

↓

Create Initial Service

↓

Configure CI/CD

↓

Deploy to Development

↓

Create Pull Request

↓

Automated Testing

↓

Security Validation

↓

GitOps Deployment

↓

Production Readiness Review

↓

Production Deployment

↓

Service Registered in Catalog

↓

Operational Monitoring
```

Every step is automated wherever possible.

---

# Golden Path Principles

Our Golden Paths follow these principles:

- Self-service over manual requests
- Automation over repetitive tasks
- Standardization over customization
- Secure defaults
- Observable by default
- Infrastructure as Code
- Git as the source of truth
- Continuous improvement

---

# Required Platform Standards

Every Golden Path implementation must satisfy the organization's platform standards.

## Application Standards

- Cloud-native architecture
- Twelve-Factor App principles
- Externalized configuration
- Stateless design where appropriate
- Health endpoints implemented

---

## Kubernetes Standards

- Helm chart provided
- Resource requests defined
- Resource limits defined
- Readiness probe configured
- Liveness probe configured
- Startup probe (if required)
- Rolling updates enabled

---

## Security Standards

- Secrets stored securely
- Containers run as non-root
- RBAC configured
- Vulnerability scanning enabled
- Least privilege enforced
- TLS enabled where required

---

## Observability Standards

Every production service must include:

- Prometheus metrics
- Structured logging
- OpenTelemetry tracing
- Grafana dashboard
- Alerting rules
- Health endpoints
- Defined Service Level Objectives (SLOs)

---

## Documentation Standards

Each service must include:

- Architecture documentation
- Deployment guide
- Configuration guide
- Runbooks
- API documentation (if applicable)
- Production Readiness documentation

---

# CI/CD Integration

Golden Paths include standardized Continuous Integration and Continuous Delivery pipelines.

The CI/CD pipeline should automate:

- Source code checkout
- Dependency installation
- Build
- Unit testing
- Integration testing
- Static code analysis
- Security scanning
- Container image build
- Container image scanning
- Artifact publication

Example workflow:

```text
Git Commit

↓

GitHub Actions

↓

Build

↓

Test

↓

Security Scan

↓

Container Image

↓

Artifact Registry
```

Pipeline templates are maintained by the Platform Engineering Team to ensure consistency across services.

---

# GitOps Integration

All production deployments should follow the organization's GitOps model.

Deployment workflow:

```text
Application Repository

↓

Container Image Published

↓

GitOps Repository Updated

↓

Argo CD Detects Change

↓

Cluster Synchronization

↓

Deployment Verification
```

GitOps principles include:

- Declarative infrastructure
- Git as the source of truth
- Automated reconciliation
- Version-controlled deployments
- Auditable change history
- Rollback through Git

The Platform Team owns the GitOps deployment framework.

---

# Production Readiness Integration

Every service following the Golden Path must complete a Production Readiness Review (PRR) before production deployment.

The review verifies:

- Architecture
- Reliability
- Security
- Observability
- Scalability
- Disaster recovery
- Operational readiness
- Documentation
- Ownership

The Production Readiness Checklist must be completed and approved before deployment proceeds.

---

# Platform Automation

The Golden Path should automate repetitive engineering tasks wherever possible.

Examples include:

- Repository creation
- Software Catalog registration
- Helm chart generation
- CI/CD pipeline creation
- Kubernetes namespace creation
- Monitoring configuration
- Dashboard provisioning
- Alert creation
- Documentation scaffolding

Automation reduces manual effort while improving consistency.

---

# Platform Team Responsibilities

The Platform Engineering Team owns and maintains the Golden Paths.

Responsibilities include:

## Platform Design

- Define standard workflows
- Maintain software templates
- Establish engineering standards

---

## Automation

- Build self-service capabilities
- Maintain CI/CD templates
- Maintain GitOps workflows
- Automate infrastructure provisioning

---

## Governance

- Review platform standards
- Maintain Production Readiness requirements
- Ensure compliance with organizational policies

---

## Developer Experience

- Reduce friction
- Improve onboarding
- Gather developer feedback
- Continuously improve workflows

---

# Measuring Success

The effectiveness of Golden Paths should be measured using platform metrics such as:

- Developer onboarding time
- Time to first deployment
- Platform adoption rate
- Deployment frequency
- Lead time for changes
- Production incident rate
- Developer satisfaction
- Support request volume

These metrics help identify opportunities for continuous improvement.

---

# High-Level Golden Path Architecture

```text
                     Developer
                          │
                          ▼
             Internal Developer Portal
                          │
                          ▼
                Software Template Selected
                          │
                          ▼
                Repository Automatically Created
                          │
                          ▼
                 CI/CD Pipeline Generated
                          │
                          ▼
                 Application Built & Tested
                          │
                          ▼
                  GitOps Repository Updated
                          │
                          ▼
                  Argo CD Deploys Service
                          │
                          ▼
             Service Registered in Catalog
                          │
                          ▼
           Monitoring, Alerts & Documentation
```

The Golden Path provides an end-to-end, standardized workflow from service creation to production operations.

---

# Platform Engineering Principles

Our Golden Path strategy follows these principles:

- Developers should focus on business value rather than infrastructure complexity.
- Every service should begin with secure and reliable defaults.
- Automation should replace repetitive manual tasks.
- Platform standards should be enforced through reusable templates.
- Git is the source of truth for deployments.
- Observability and operational readiness are built in from the start.
- Continuous feedback drives platform improvement.

---

# Key Takeaways

- A Golden Path is the organization's recommended and fully supported workflow for building and operating software.
- Golden Paths reduce cognitive load by providing standardized, automated development experiences.
- Platform standards for architecture, security, observability, Kubernetes, and documentation are incorporated by default.
- CI/CD and GitOps are integrated into the Golden Path to enable consistent, automated software delivery.
- Production Readiness Reviews ensure services meet operational requirements before deployment.
- The Platform Engineering Team owns the Golden Paths and continuously evolves them to improve developer experience, governance, and operational excellence.