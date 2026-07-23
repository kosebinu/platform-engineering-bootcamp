# Backstage Scaffolder Template Development

## Purpose

This document defines the architecture, structure, development standards, and lifecycle of Backstage Software Templates used within the organization's Internal Developer Platform (IDP).

Software Templates provide reusable, automated workflows that provision production-ready engineering projects while enforcing organizational standards for security, reliability, observability, and governance.

This document serves as the implementation guide for Platform Engineers responsible for designing, maintaining, and evolving Backstage templates.

---

# Scaffolder Architecture

The Backstage Scaffolder consists of several logical components that work together to automate project creation.

```text
                 Developer
                      │
                      ▼
             Backstage Frontend
                      │
                      ▼
              Software Template
                      │
                      ▼
             Scaffolder Backend
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 Template Engine   Action Engine   Task Runner
      │               │                │
      └───────────────┼────────────────┘
                      ▼
 GitHub • GitOps • CI/CD • Service Catalog
```

### Frontend

Presents templates and collects user input through dynamically generated forms.

### Template Engine

Processes template files, substitutes variables, and prepares project artifacts.

### Action Engine

Executes workflow actions such as creating repositories, registering catalog entities, or invoking external APIs.

### Task Runner

Coordinates execution, tracks progress, records logs, and reports success or failure.

---

# Template Anatomy

Every Software Template contains four major sections.

```yaml
apiVersion:
kind:
metadata:
spec:
```

Example:

```yaml
apiVersion: scaffolder.backstage.io/v1beta3

kind: Template

metadata:
  name: springboot-service

spec:
  owner: platform-team
```

Each section has a specific responsibility.

---

# Template YAML Structure

## apiVersion

Defines the Scaffolder API version used by the template.

Example:

```yaml
apiVersion: scaffolder.backstage.io/v1beta3
```

---

## kind

Identifies the resource type.

Example:

```yaml
kind: Template
```

---

## metadata

Describes the template itself.

Example:

```yaml
metadata:
  name: payment-api-template
  title: Payment API
  description: Creates a production-ready payment service.
  tags:
    - java
    - kubernetes
    - rest-api
```

Metadata is displayed in the Backstage catalog and helps developers discover templates.

---

## spec

Defines the behavior of the template.

Typical elements include:

- owner
- type
- parameters
- steps
- output

Example:

```yaml
spec:
  owner: platform-team
  type: service
```

---

# Metadata

Metadata provides descriptive information about the template.

Typical fields include:

- Name
- Title
- Description
- Tags
- Version
- Documentation links
- Owner
- Template type

Metadata should be clear, searchable, and consistently maintained.

---

# Spec

The `spec` section defines how the template executes.

Typical structure:

```yaml
spec:
  owner:
  type:
  parameters:
  steps:
  output:
```

The Platform Team should keep the specification concise and focused on reusable workflows.

---

# Parameters

Parameters collect information from the developer during template execution.

Typical inputs include:

```yaml
parameters:
  - title: Service Information

    properties:

      serviceName:
        type: string

      description:
        type: string

      owner:
        type: string
```

Common parameter categories:

## Service Information

- Service name
- Description
- Business system

---

## Ownership

- Team
- Technical owner
- Product owner

---

## Technology

- Language
- Framework
- Runtime

---

## Deployment

- Namespace
- Environment
- Cloud provider

Only collect parameters that cannot be derived automatically.

---

# Variables

Template variables substitute parameter values into generated files.

Example:

```text
${{ parameters.serviceName }}
```

During execution:

```text
payment-api
```

Variables may be used in:

- README files
- Helm charts
- Kubernetes manifests
- GitHub Actions
- Dockerfiles
- Documentation
- Catalog metadata

Consistent variable naming improves template readability and maintainability.

---

# Steps

The `steps` section defines the ordered workflow executed by the Scaffolder.

Typical execution flow:

```text
Fetch Template

↓

Render Files

↓

Create Repository

↓

Push Initial Commit

↓

Configure CI/CD

↓

Register Service

↓

Return Outputs
```

Each step performs a single, well-defined task.

Example actions include:

- `fetch:template`
- `publish:github`
- `catalog:register`
- `debug:log`
- `http:request`

Complex workflows should be decomposed into smaller, reusable steps.

---

# Outputs

Outputs provide useful information after template execution completes.

Typical outputs include:

- Repository URL
- Service Catalog link
- Documentation URL
- CI/CD pipeline URL
- Deployment dashboard
- Pull request link

Example:

```yaml
output:
  links:
    - title: Repository
      url: ${{ steps.publish.output.remoteUrl }}
```

Outputs improve developer experience by providing immediate access to generated resources.

---

# Validation

Validation prevents invalid input and reduces failed executions.

Validation should occur before expensive actions are performed.

Typical validation includes:

- Required fields
- Naming conventions
- Repository uniqueness
- Allowed environments
- Team ownership
- Supported runtimes
- Maximum length constraints

Validation errors should:

- Clearly identify the invalid field
- Explain why validation failed
- Suggest corrective actions

Fail fast whenever possible.

---

# Template Lifecycle

Software Templates should be managed as versioned platform products.

Typical lifecycle:

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

### Design

Requirements are gathered and reviewed.

### Development

Template implementation and initial testing.

### Testing

Validation in development and staging environments.

### Published

Available for general engineering use.

### Supported

Actively maintained by the Platform Team.

### Deprecated

Scheduled for replacement.

### Retired

Removed from active use after migration.

Template versions should be tracked using source control and release management practices.

---

# Best Practices

Platform Engineers should follow these principles when developing templates.

## Keep Templates Opinionated

Provide sensible defaults while allowing necessary customization.

---

## Minimize Required Input

Only request information that cannot be generated automatically.

---

## Automate Repetitive Tasks

Templates should automate:

- Repository creation
- CI/CD configuration
- GitOps registration
- Service Catalog registration
- Documentation scaffolding

---

## Build Secure Defaults

Every generated project should include:

- Non-root containers
- Security scanning
- Least privilege
- Secret management
- Approved base images

---

## Include Observability

Generated services should include:

- Metrics
- Structured logging
- Distributed tracing
- Health endpoints
- Alert configuration

---

## Design for Reuse

Avoid hardcoding team-specific logic.

Templates should support multiple engineering teams with minimal modification.

---

## Version Templates

Changes should be versioned and backward compatibility considered where practical.

---

## Document Every Template

Each template should include:

- Purpose
- Intended use
- Inputs
- Outputs
- Dependencies
- Supported languages
- Known limitations

---

## Test Before Publishing

Templates should be validated through automated and manual testing before being released to developers.

---

# Platform Team Responsibilities

The Platform Engineering Team is responsible for:

## Template Design

- Develop reusable templates
- Standardize project structure
- Improve developer workflows

---

## Governance

- Approve template changes
- Maintain engineering standards
- Review adoption metrics

---

## Maintenance

- Fix defects
- Update dependencies
- Retire obsolete templates
- Improve execution performance

---

## Developer Experience

- Gather feedback
- Reduce onboarding friction
- Improve self-service capabilities
- Continuously evolve templates

---

# Platform Engineering Principles

Our template development strategy follows these principles:

- Treat templates as production software.
- Prefer automation over manual configuration.
- Provide secure, observable defaults.
- Keep templates reusable and maintainable.
- Validate early and fail clearly.
- Use Git for version control and change management.
- Continuously improve templates based on developer feedback.

---

# Key Takeaways

- Backstage Software Templates automate the creation of standardized engineering projects.
- Templates are composed of metadata, specifications, parameters, workflow steps, and outputs.
- The Scaffolder renders templates, executes actions, integrates with platform services, and provisions production-ready resources.
- Strong validation, reusable design, and secure defaults improve reliability and developer experience.
- Software Templates should be managed as versioned platform products with clear ownership, governance, and lifecycle management.