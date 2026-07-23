# Backstage Scaffolder Actions

## Purpose

This document defines the architecture, implementation standards, governance, and operational practices for Scaffolder Actions used within the organization's Internal Developer Platform (IDP).

Scaffolder Actions are the executable building blocks of Software Templates. They automate interactions with source control systems, cloud providers, Kubernetes clusters, CI/CD platforms, Service Catalogs, and other engineering systems.

This document serves as the engineering standard for developing, maintaining, and governing both built-in and custom Scaffolder Actions.

---

# What is a Scaffolder Action?

A Scaffolder Action is an executable unit of work performed during template execution.

Each action performs a single, well-defined task.

Examples include:

- Creating a GitHub repository
- Rendering template files
- Registering a Backstage catalog entity
- Creating a Kubernetes namespace
- Updating a GitOps repository
- Calling an external API

Actions are executed sequentially by the Scaffolder Task Runner.

---

# Scaffolder Action Architecture

```text
                  Software Template
                         │
                         ▼
                    Task Runner
                         │
        ┌────────────────┼─────────────────┐
        ▼                ▼                 ▼
 Built-in Actions   Custom Actions   External APIs
        │                │                 │
        └────────────────┼─────────────────┘
                         ▼
                Execution Results
                         │
                         ▼
                   Template Output
```

The Task Runner orchestrates action execution and records execution status, logs, and outputs.

---

# Built-in Actions

Backstage provides a library of reusable built-in actions.

Common built-in actions include:

| Action | Purpose |
|---------|----------|
| `fetch:template` | Copy and render template files |
| `publish:github` | Create and initialize a GitHub repository |
| `publish:gitlab` | Create a GitLab repository |
| `catalog:register` | Register an entity in the Software Catalog |
| `debug:log` | Write execution logs |
| `http:request` | Invoke external HTTP APIs |
| `fetch:plain` | Retrieve files from a remote location |

Built-in actions should be used whenever they satisfy platform requirements to reduce maintenance overhead.

---

# Custom Actions

Organizations frequently develop custom actions to integrate with internal systems.

Examples include:

- Create Azure Resource Group
- Provision AKS namespace
- Create Azure Key Vault
- Configure Azure DNS
- Create PagerDuty service
- Generate Grafana dashboard
- Create Jira project
- Register monitoring alerts
- Provision cloud storage
- Configure internal identity systems

Custom actions allow the Internal Developer Platform to automate organization-specific workflows.

---

# Action Execution

Actions execute in the order defined by the template.

Typical execution flow:

```text
Validate Parameters

↓

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

Register Catalog Entity

↓

Configure GitOps

↓

Return Outputs
```

Each action:

- Receives validated inputs
- Performs a single responsibility
- Produces structured outputs
- Reports success or failure
- Records execution logs

Actions should be deterministic and repeatable whenever possible.

---

# Action Inputs

Actions receive input values from:

- Template parameters
- Previous action outputs
- Configuration values
- Secure secrets
- Environment variables

Example:

```yaml
steps:

  - id: publish

    action: publish:github

    input:
      repoUrl: github.com/org/payment-api
      description: ${{ parameters.description }}
```

Inputs should be validated before execution.

---

# Action Outputs

Actions may expose outputs that are consumed by later workflow steps.

Typical outputs include:

- Repository URL
- Commit SHA
- Pull request URL
- Catalog entity reference
- Deployment URL

Example:

```yaml
output:

  links:

    - title: Repository

      url: ${{ steps.publish.output.remoteUrl }}
```

Outputs enable templates to chain actions together without duplicating configuration.

---

# Secrets

Many actions require access to sensitive credentials.

Examples include:

- GitHub App credentials
- Azure service principals
- AWS IAM credentials
- Kubernetes tokens
- API keys
- Database passwords

Secrets must never be:

- Hardcoded
- Stored in template files
- Logged
- Returned as outputs

Secrets should be retrieved from approved secret management systems such as:

- Azure Key Vault
- HashiCorp Vault
- AWS Secrets Manager
- Kubernetes Secrets

Access should follow the principle of least privilege.

---

# Error Handling

Actions should fail predictably and provide actionable diagnostics.

Common failure scenarios include:

- Invalid parameters
- Duplicate repository names
- Authentication failures
- Network connectivity issues
- API rate limits
- Permission errors
- Cloud provisioning failures
- Catalog registration failures

Error messages should:

- Clearly identify the failed action
- Explain the reason for failure
- Suggest corrective actions
- Include execution identifiers where appropriate

Templates should stop execution when a critical action fails unless recovery is explicitly supported.

---

# Retry Behavior

Some failures are temporary and may succeed if retried.

Typical retry candidates include:

- Network timeouts
- Temporary API outages
- Cloud service throttling
- Repository synchronization delays

Retries should use:

- Exponential backoff
- Maximum retry limits
- Configurable timeout values

Example:

```text
Attempt 1

↓

Temporary Failure

↓

Wait 2 seconds

↓

Attempt 2

↓

Wait 4 seconds

↓

Attempt 3

↓

Success
```

Non-recoverable failures such as invalid input or authorization errors should not be retried.

---

# Action Development

Custom actions should follow consistent engineering standards.

## Design Principles

- Perform one responsibility
- Keep interfaces simple
- Return structured outputs
- Avoid hidden side effects
- Support idempotent execution where practical

---

## Implementation Standards

Custom actions should include:

- Input validation
- Output schema
- Logging
- Error handling
- Documentation
- Unit tests
- Integration tests

---

## Versioning

Actions should be version controlled and released using standard engineering practices.

Breaking changes should be documented and communicated before adoption.

---

## Documentation

Each action should include:

- Purpose
- Required inputs
- Outputs
- Dependencies
- Example usage
- Failure conditions
- Security requirements

---

# Security Considerations

Security is a foundational requirement for all Scaffolder Actions.

## Authentication

Actions should authenticate using:

- GitHub Apps
- Managed identities
- Service principals
- Federated identity
- Short-lived credentials

Avoid long-lived personal access tokens.

---

## Authorization

Actions should operate with the minimum permissions necessary.

Examples:

- Repository creation only
- Namespace provisioning only
- Read-only catalog access where appropriate

---

## Input Validation

All external input should be validated before execution.

Examples:

- Repository names
- Team names
- Environment names
- URLs
- Resource identifiers

Validation reduces operational risk and prevents injection attacks.

---

## Secret Protection

Sensitive values must:

- Never appear in logs
- Never be returned as outputs
- Never be stored in repositories
- Be masked in execution history

---

## Audit Logging

Every action execution should generate audit records including:

- Action identifier
- Timestamp
- User identity
- Template identifier
- Success or failure
- Duration
- Resource identifiers
- Correlation ID

Audit logs support:

- Compliance
- Security investigations
- Operational troubleshooting
- Platform analytics

---

# Platform Team Responsibilities

The Platform Engineering Team owns the Scaffolder Action ecosystem.

Responsibilities include:

## Platform Development

- Develop reusable actions
- Maintain built-in integrations
- Build organization-specific automation

---

## Governance

- Review action quality
- Approve new actions
- Maintain coding standards
- Ensure security compliance

---

## Operations

- Monitor action execution
- Investigate failures
- Improve execution performance
- Track platform adoption

---

## Developer Experience

- Simplify action interfaces
- Improve documentation
- Reduce manual configuration
- Gather developer feedback

---

# High-Level Action Execution Flow

```text
Developer

↓

Software Template

↓

Task Runner

↓

Action Validation

↓

Execute Built-in / Custom Action

↓

External Platform

↓

Receive Results

↓

Record Audit Log

↓

Return Outputs

↓

Next Action
```

Each action contributes a discrete capability to the overall template workflow while remaining reusable across multiple templates.

---

# Platform Engineering Principles

Our Scaffolder Actions follow these principles:

- Actions should perform one well-defined responsibility.
- Prefer built-in actions before creating custom implementations.
- Validate inputs early and fail with clear diagnostics.
- Use secure authentication and least-privilege authorization.
- Protect secrets throughout execution.
- Design actions to be reusable, testable, and maintainable.
- Monitor action execution and continuously improve reliability.

---

# Key Takeaways

- Scaffolder Actions are the execution units that power Backstage Software Templates.
- Built-in actions provide common capabilities such as repository creation, template rendering, and catalog registration.
- Custom actions extend the platform by integrating with organization-specific systems and workflows.
- Strong input validation, structured outputs, retry logic, and error handling improve execution reliability.
- Security, audit logging, and least-privilege access are essential for safe automation.
- The Platform Engineering Team owns the development, governance, and continuous improvement of the organization's Scaffolder Action ecosystem.