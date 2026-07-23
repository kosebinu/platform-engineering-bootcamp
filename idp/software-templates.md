# Software Templates

## Purpose

This document defines the standards, governance, and lifecycle for Software Templates used within the organization's Internal Developer Platform (IDP).

Software Templates provide a standardized, automated, and self-service mechanism for creating new applications, services, infrastructure components, and supporting engineering assets.

By encapsulating organizational best practices into reusable templates, Software Templates enable engineering teams to rapidly deliver production-ready services while maintaining consistency, security, and operational excellence.

---

# What is a Software Template?

A Software Template is a reusable blueprint that automatically generates a new engineering project according to organizational standards.

Rather than manually creating repositories, configuring CI/CD pipelines, writing Kubernetes manifests, or registering services, developers complete a small set of inputs and the platform generates the required assets automatically.

Software Templates are designed to:

- Standardize project creation
- Reduce repetitive work
- Improve developer productivity
- Enforce platform standards
- Accelerate onboarding
- Improve operational consistency

Software Templates are executed through the organization's Internal Developer Portal (Backstage).

---

# Why Software Templates Exist

As engineering organizations grow, manually creating new projects becomes inefficient and error-prone.

Without standardized templates, teams often:

- Copy existing repositories
- Forget required configuration
- Implement inconsistent CI/CD pipelines
- Miss security requirements
- Omit observability configuration
- Produce inconsistent documentation

Software Templates solve these problems by providing a consistent starting point for every new project.

Primary objectives include:

- Improve consistency
- Reduce setup time
- Eliminate repetitive manual work
- Encourage platform adoption
- Embed engineering best practices
- Improve software quality
- Reduce operational risk

---

# Template Inputs

Templates should collect only the information necessary to customize the generated project.

Typical inputs include:

## Service Information

- Service name
- Description
- Business domain
- System name
- Service type

---

## Ownership

- Engineering team
- Technical owner
- Product owner

---

## Technology Stack

- Programming language
- Runtime
- Framework
- Container base image

---

## Deployment

- Target Kubernetes cluster
- Environment
- Namespace
- Cloud provider
- Region

---

## Repository

- Repository visibility
- Repository name
- Default branch

The Platform Team should minimize required inputs while providing sensible defaults wherever possible.

---

# Generated Assets

Software Templates should generate all resources required to begin development.

Typical generated assets include:

## Source Code

- Project structure
- Sample application
- Configuration files
- Dependency management

---

## Repository

- Git repository
- Standard README
- License file
- CODEOWNERS file
- Contribution guidelines

---

## CI/CD

- Build pipeline
- Test pipeline
- Container image build
- Security scanning
- Artifact publishing

---

## Kubernetes

- Helm chart
- Values files
- Deployment manifests
- Service manifests
- Ingress configuration
- Health probes
- Resource requests and limits

---

## GitOps

- Argo CD Application manifest
- GitOps repository registration
- Environment configuration

---

## Observability

- Prometheus metrics configuration
- Grafana dashboard template
- Logging configuration
- OpenTelemetry instrumentation
- Alert definitions

---

## Documentation

- Architecture overview
- Deployment guide
- Runbook
- API documentation
- ADR template
- Production Readiness Checklist

---

## Backstage

- `catalog-info.yaml`
- Ownership metadata
- System association
- Tags
- Documentation links

---

# Platform Standards

Every Software Template must comply with the organization's engineering standards.

## Security Standards

- Approved base images
- Non-root containers
- Secrets managed securely
- RBAC configured
- Vulnerability scanning enabled
- Least privilege principles

---

## Kubernetes Standards

- Helm-based deployment
- Resource requests defined
- Resource limits defined
- Readiness probes
- Liveness probes
- Rolling updates enabled

---

## CI/CD Standards

- Automated builds
- Unit tests
- Static code analysis
- Dependency scanning
- Container image scanning
- Artifact versioning

---

## Observability Standards

Every generated service must include:

- Metrics
- Structured logging
- Distributed tracing
- Health endpoints
- Monitoring dashboards
- Alerting configuration

---

## Documentation Standards

Each project must include:

- README
- Architecture documentation
- Deployment guide
- Runbooks
- API documentation (where applicable)
- Production Readiness documentation

---

# Guardrails

Software Templates establish engineering guardrails to reduce operational and security risks.

Examples include:

- Standard repository structure
- Approved dependency versions
- Required documentation
- Secure container configuration
- Standard CI/CD pipelines
- Naming conventions
- Kubernetes best practices
- Mandatory metadata
- Service registration

Guardrails should guide developers without unnecessarily limiting innovation.

---

# Template Lifecycle

Software Templates should be managed as versioned engineering products.

Typical lifecycle stages include:

```text
Design

↓

Development

↓

Testing

↓

Published

↓

Supported

↓

Deprecated

↓

Retired
```

Template updates should be reviewed, tested, and communicated before release.

Older template versions should remain available until migration guidance is provided.

---

# Benefits

## For Developers

- Faster project creation
- Reduced manual setup
- Consistent project structure
- Easier onboarding
- Built-in platform capabilities

---

## For Platform Engineering

- Standardized engineering practices
- Reduced support effort
- Easier governance
- Improved platform adoption
- Simplified maintenance

---

## For Operations

- Consistent deployments
- Better observability
- Improved incident response
- Predictable infrastructure
- Easier troubleshooting

---

## For the Organization

- Improved developer productivity
- Faster delivery
- Higher software quality
- Stronger governance
- Reduced operational risk
- Better compliance

---

# Platform Team Responsibilities

The Platform Engineering Team owns the Software Template ecosystem.

Responsibilities include:

## Template Development

- Design reusable templates
- Maintain template quality
- Improve developer workflows
- Introduce new platform capabilities

---

## Standards

- Define engineering standards
- Maintain platform defaults
- Publish template documentation
- Ensure alignment with organizational policies

---

## Automation

- Integrate templates with Backstage
- Automate repository creation
- Automate CI/CD configuration
- Automate GitOps registration
- Automate Service Catalog registration

---

## Governance

- Review template adoption
- Monitor template quality
- Approve template changes
- Deprecate outdated templates

---

## Developer Experience

- Collect developer feedback
- Reduce onboarding friction
- Improve self-service capabilities
- Continuously refine templates

---

# High-Level Software Template Architecture

```text
                     Developer
                          │
                          ▼
                 Internal Developer Portal
                          │
                          ▼
                 Select Software Template
                          │
                          ▼
                  Provide Project Inputs
                          │
                          ▼
                 Backstage Scaffolder
                          │
        ┌─────────────────┼──────────────────┐
        ▼                 ▼                  ▼
  GitHub Repository   CI/CD Pipeline    Helm Chart
        │                 │                  │
        └─────────────────┼──────────────────┘
                          ▼
                  GitOps Registration
                          ▼
                 Service Catalog Entry
                          ▼
             Production-Ready Foundation
```

Software Templates provide a repeatable and standardized process for creating new engineering assets while embedding organizational standards into every project.

---

# Platform Engineering Principles

Our Software Template strategy follows these principles:

- Developers should never start from an empty repository.
- Standardization improves reliability without eliminating flexibility.
- Automation should replace repetitive manual tasks.
- Secure, observable, and production-ready defaults should be provided automatically.
- Templates should evolve alongside the platform.
- Self-service experiences should minimize friction for engineering teams.
- Platform standards should be enforced through reusable automation rather than manual reviews.

---

# Key Takeaways

- Software Templates provide reusable blueprints for creating new engineering projects.
- Templates automate repository creation, CI/CD configuration, Kubernetes deployment, GitOps registration, observability, and documentation.
- Standardized templates reduce cognitive load, improve consistency, and accelerate software delivery.
- Platform standards and guardrails ensure new services are secure, observable, and operationally ready by default.
- The Platform Engineering Team owns the lifecycle, governance, and continuous improvement of Software Templates.
- Well-designed templates are a foundational capability of a modern Internal Developer Platform and significantly improve developer experience while supporting organizational governance.