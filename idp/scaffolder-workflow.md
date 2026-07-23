# Backstage Scaffolder Workflow

## Purpose

This document defines the architecture, execution workflow, integrations, and operational standards for the Backstage Scaffolder used within the organization's Internal Developer Platform (IDP).

The Backstage Scaffolder enables developers to create production-ready applications and engineering resources through standardized, self-service software templates. It automates project scaffolding while enforcing organizational engineering standards.

The Scaffolder is a core platform capability that improves developer experience, accelerates delivery, and promotes consistency across engineering teams.

---

# Backstage Scaffolder Architecture

The Backstage Scaffolder is responsible for transforming reusable software templates into fully initialized engineering projects.

High-level architecture:

```text
                     Developer
                          │
                          ▼
                 Backstage Developer Portal
                          │
                          ▼
                  Software Template Catalog
                          │
                          ▼
                 Backstage Scaffolder Engine
                          │
         ┌────────────────┼─────────────────┐
         ▼                ▼                 ▼
    GitHub API      CI/CD Platform     GitOps Repository
         │                │                 │
         └────────────────┼─────────────────┘
                          ▼
                  Service Catalog
                          │
                          ▼
                Production-Ready Project
```

The Scaffolder orchestrates interactions with multiple platform services to automate project creation.

---

# Template Execution Workflow

Template execution follows a consistent lifecycle.

```text
Developer

↓

Open Backstage

↓

Select Software Template

↓

Provide Required Parameters

↓

Validate Inputs

↓

Execute Template Actions

↓

Generate Project Assets

↓

Create Repository

↓

Configure CI/CD

↓

Register Service

↓

Configure GitOps

↓

Return Project Summary
```

Each stage is automated wherever possible to minimize manual effort and reduce configuration errors.

---

# Execution Stages

## 1. Template Selection

The developer selects an approved Software Template from the Internal Developer Portal.

Examples include:

- REST API
- Worker Service
- Event Consumer
- Scheduled Job
- Frontend Application
- Infrastructure Component

Only Platform Team–approved templates are available.

---

## 2. Parameter Collection

The Scaffolder collects project-specific information.

Typical parameters include:

- Service name
- Description
- Engineering team
- Business system
- Programming language
- Deployment environment
- Repository visibility

Validation occurs before template execution begins.

---

## 3. Template Rendering

The Scaffolder processes template files and substitutes user-provided values into project artifacts.

Examples:

- README
- Helm chart
- Kubernetes manifests
- GitHub Actions workflow
- Configuration files
- `catalog-info.yaml`

Rendering ensures every generated project adheres to organizational standards.

---

# Repository Creation

After template rendering, the Scaffolder creates a source code repository.

Repository provisioning typically includes:

- Repository creation
- Default branch initialization
- Standard directory structure
- Initial commit
- README generation
- CODEOWNERS configuration
- Branch protection (where supported)
- Repository topics and metadata

Example structure:

```text
payment-api/

├── src/
├── tests/
├── docs/
├── helm/
├── .github/
├── catalog-info.yaml
├── Dockerfile
├── README.md
└── values.yaml
```

Repository creation should be fully automated.

---

# Catalog Registration

Once the repository is created, the service is registered in the Backstage Software Catalog.

Registration includes:

- Component metadata
- Ownership
- System association
- Tags
- Documentation links
- Repository reference
- Lifecycle status

Typical entity:

```yaml
kind: Component

metadata:
  name: payment-api

spec:
  owner: payments-team
  system: payments
  lifecycle: development
```

Automatic registration ensures discoverability from day one.

---

# GitHub Integration

The Scaffolder integrates with GitHub to automate repository management.

Typical actions include:

- Create repository
- Apply repository settings
- Create initial commit
- Configure branch protection
- Add repository topics
- Configure CODEOWNERS
- Create default labels
- Assign repository permissions

Authentication should use GitHub Apps or secure service credentials rather than personal access tokens.

---

# GitOps Integration

The Scaffolder integrates with the organization's GitOps workflow.

Typical actions include:

- Generate Argo CD Application manifest
- Update GitOps repository
- Create environment configuration
- Register deployment manifests
- Trigger GitOps synchronization

Deployment flow:

```text
Application Repository

↓

Container Image

↓

GitOps Repository

↓

Argo CD

↓

Kubernetes Cluster
```

Git remains the source of truth for deployment configuration.

---

# CI/CD Integration

The Scaffolder provisions standardized CI/CD pipelines for every generated project.

Generated pipeline capabilities include:

- Dependency installation
- Build
- Unit testing
- Integration testing
- Static code analysis
- Vulnerability scanning
- Container image build
- Container image scanning
- Artifact publication

Example pipeline:

```text
Git Push

↓

GitHub Actions

↓

Build

↓

Test

↓

Security Scan

↓

Container Registry
```

Pipeline templates are maintained by the Platform Engineering Team.

---

# Error Handling

The Scaffolder should detect and report failures throughout the execution process.

Common validation failures include:

- Duplicate repository name
- Invalid service name
- Missing required parameters
- Unauthorized template access
- Repository creation failure
- GitHub API errors
- Catalog registration failure
- GitOps synchronization errors

Error messages should:

- Clearly identify the failed step
- Explain the cause
- Suggest corrective actions
- Include relevant execution identifiers for troubleshooting

Partial resource creation should be minimized, and rollback procedures should be implemented where feasible.

---

# Audit Logging

Every Scaffolder execution should produce an audit trail.

Audit records should include:

- Execution ID
- Timestamp
- User identity
- Selected template
- Input parameters (excluding secrets)
- Generated repository
- Created resources
- Execution duration
- Success or failure status
- Error details (if applicable)

Audit logs support:

- Compliance
- Security investigations
- Platform analytics
- Operational troubleshooting
- Usage reporting

Sensitive information such as credentials or secrets must never be written to audit logs.

---

# Security Considerations

The Scaffolder should operate using secure platform credentials.

Security controls include:

- Role-based access control (RBAC)
- Approved template catalog
- Input validation
- Secret management through external vaults
- Least privilege permissions
- Template code reviews
- Signed template releases where applicable

Template execution should never expose sensitive credentials to end users.

---

# Platform Team Responsibilities

The Platform Engineering Team owns the Scaffolder platform.

Responsibilities include:

## Platform Development

- Build and maintain Software Templates
- Extend Scaffolder capabilities
- Develop reusable template actions
- Improve automation workflows

---

## Integrations

- GitHub
- CI/CD platforms
- GitOps repositories
- Backstage Software Catalog
- Identity providers
- Secret management systems

---

## Governance

- Approve templates
- Review template quality
- Maintain execution standards
- Enforce security controls

---

## Operations

- Monitor execution success rates
- Investigate failed template runs
- Improve execution performance
- Maintain platform reliability

---

# High-Level End-to-End Workflow

```text
Developer
    │
    ▼
Backstage Portal
    │
    ▼
Software Template
    │
    ▼
Backstage Scaffolder
    │
    ├──────────────► GitHub Repository
    │
    ├──────────────► CI/CD Pipeline
    │
    ├──────────────► GitOps Repository
    │
    ├──────────────► Service Catalog
    │
    └──────────────► Documentation
                         │
                         ▼
              Production-Ready Service
```

The Scaffolder acts as the orchestration engine that connects platform services into a seamless self-service developer experience.

---

# Platform Engineering Principles

Our Scaffolder implementation follows these principles:

- Self-service over manual provisioning.
- Automation over repetitive configuration.
- Secure defaults for every generated project.
- Standardization through reusable templates.
- Git as the source of truth.
- Observable, production-ready services from day one.
- Continuous improvement driven by developer feedback and platform metrics.

---

# Key Takeaways

- The Backstage Scaffolder automates the creation of standardized engineering projects through reusable Software Templates.
- It orchestrates repository creation, CI/CD pipeline provisioning, GitOps configuration, and Software Catalog registration.
- Automated integrations ensure new services are production-ready with minimal manual effort.
- Robust error handling, audit logging, and security controls improve platform reliability and governance.
- The Platform Engineering Team owns the Scaffolder ecosystem and continuously evolves templates, integrations, and workflows to enhance developer experience.