# Service Catalog

## Purpose

This document defines the standards, governance model, and operational responsibilities for the organization's Service Catalog.

The Service Catalog is the authoritative inventory of software services, APIs, infrastructure resources, engineering teams, and supporting metadata across the Internal Developer Platform (IDP).

It enables engineering teams to discover services, identify ownership, understand dependencies, access operational resources, and support production systems efficiently.

The Service Catalog is maintained as part of the Internal Developer Platform and serves as the single source of truth for engineering assets.

---

# Purpose of a Service Catalog

A Service Catalog provides centralized visibility into the organization's engineering ecosystem.

Its primary objectives are to:

- Provide a single source of truth for engineering assets
- Enable service discovery
- Clearly define ownership
- Improve incident response
- Support platform automation
- Standardize engineering metadata
- Improve developer onboarding
- Enable dependency analysis
- Strengthen operational governance

The Service Catalog should be treated as a core platform capability rather than a documentation repository.

---

# Required Metadata

Every production service registered in the catalog must include standardized metadata.

## Identity

- Service name
- Description
- Tags
- Service type
- Lifecycle status
- Version

---

## Ownership

- Engineering team
- Technical owner
- Product owner
- On-call team
- Escalation contacts

---

## Source Code

- Repository URL
- Default branch
- CI/CD pipeline
- Release pipeline

---

## Runtime Environment

- Kubernetes namespace
- Cluster
- Environment (Development, Staging, Production)
- Cloud provider
- Region

---

## Documentation

- Architecture documentation
- Deployment guide
- API documentation
- Runbooks
- ADRs
- Disaster recovery documentation

---

## Operational Information

- Grafana dashboard
- Prometheus metrics
- Loki logs
- Tempo traces
- Alertmanager alerts
- SLOs
- PagerDuty service (or equivalent)
- Incident playbooks

---

# Service Lifecycle

Every service should have a defined lifecycle state.

Typical lifecycle stages include:

```text
Experimental

↓

Development

↓

Testing

↓

Production

↓

Deprecated

↓

Retired
```

## Lifecycle Definitions

### Experimental

Early prototypes or proof-of-concept services.

---

### Development

Active engineering work with limited operational guarantees.

---

### Testing

Validated within non-production environments.

---

### Production

Supported service with defined ownership and operational commitments.

---

### Deprecated

Scheduled for replacement or removal.

---

### Retired

No longer supported or deployed.

Lifecycle status should be reviewed regularly and updated whenever the service transitions between stages.

---

# Ownership Model

Every service must have clearly defined ownership.

Ownership enables:

- Incident response
- Operational support
- Security reviews
- Change management
- Production readiness
- Lifecycle management

Each catalog entry should define:

- Engineering owner
- Product owner
- Responsible team
- On-call rotation
- Escalation contacts

Ownership must always identify a team rather than relying on a single individual.

---

# Operational Metadata

Operational metadata enables engineers to support services efficiently during normal operations and production incidents.

Each production service should include links to:

- Monitoring dashboards
- Alert definitions
- Logging platform
- Distributed tracing
- Runbooks
- Incident procedures
- Deployment history
- Production Readiness Review documentation
- Service Level Objectives (SLOs)

Operational information should be accessible directly from the Service Catalog.

---

# Dependency Mapping

The Service Catalog should document relationships between engineering assets.

Example:

```text
Payments System
│
├── payment-api
│      │
│      ├── PostgreSQL
│      ├── Redis
│      ├── Azure Key Vault
│      └── Payment REST API
│
└── billing-api
       │
       └── RabbitMQ
```

Dependency mapping supports:

- Change impact analysis
- Incident response
- Architecture reviews
- Capacity planning
- Platform modernization
- Risk assessment

Dependencies should be updated whenever new integrations or infrastructure components are introduced.

---

# Service Tiers

Services should be classified according to business criticality.

| Tier | Description | Examples |
|------|-------------|----------|
| Tier 0 | Mission-critical services with organization-wide impact | Identity, Authentication |
| Tier 1 | Customer-facing business-critical services | Payments, Checkout |
| Tier 2 | Important internal business services | Inventory, Reporting |
| Tier 3 | Supporting or non-critical services | Internal tools, Development utilities |

Service tier influences:

- Availability targets
- SLOs
- Incident severity
- Disaster recovery requirements
- On-call expectations
- Monitoring standards

---

# Benefits

## For Developers

- Faster service discovery
- Easier onboarding
- Better documentation
- Clear ownership
- Improved collaboration

---

## For Platform Engineering

- Standardized metadata
- Better governance
- Reduced operational overhead
- Improved automation
- Centralized platform visibility

---

## For Operations

- Faster incident response
- Easier dependency analysis
- Improved operational readiness
- Better production support
- Consistent service management

---

## For the Organization

- Improved engineering productivity
- Higher operational maturity
- Reduced knowledge silos
- Better governance
- More reliable software delivery

---

# Platform Team Responsibilities

The Platform Engineering Team owns the Service Catalog platform and defines catalog standards.

Responsibilities include:

## Platform Development

- Maintain the Software Catalog platform
- Integrate engineering systems
- Develop catalog automation
- Support engineering teams

---

## Standards

- Define metadata requirements
- Establish ownership standards
- Maintain lifecycle definitions
- Publish governance documentation

---

## Quality

- Review catalog completeness
- Validate metadata accuracy
- Monitor adoption
- Improve discoverability

---

## Automation

Automate synchronization with:

- GitHub
- Kubernetes
- CI/CD systems
- Monitoring platforms
- Incident management systems
- Documentation repositories

Manual catalog maintenance should be minimized whenever possible.

---

# Catalog Governance

The Service Catalog is governed by Platform Engineering standards.

## Metadata Governance

- Required fields must be populated.
- Metadata should follow standardized naming conventions.
- Ownership information must remain current.

---

## Registration Policy

Every production service must:

- Be registered before production deployment.
- Include required operational metadata.
- Identify responsible ownership.
- Link required documentation.

---

## Review Process

Catalog entries should be reviewed:

- During Production Readiness Reviews
- Following major architectural changes
- After ownership changes
- During periodic platform audits

---

## Continuous Improvement

The Platform Team should continuously evaluate:

- Metadata quality
- Platform adoption
- Search effectiveness
- Developer feedback
- Automation opportunities

The Service Catalog should evolve alongside the engineering organization.

---

# High-Level Service Catalog Architecture

```text
                        Developers
                             │
                             ▼
                    Backstage Portal
                             │
                     Software Catalog
                             │
      ┌──────────────┬──────────────┬──────────────┐
      ▼              ▼              ▼              ▼
   GitHub      Kubernetes     Observability   Documentation
      │              │              │              │
      ▼              ▼              ▼              ▼
Repositories   Deployments   Dashboards      TechDocs
```

The Service Catalog acts as the central knowledge layer of the Internal Developer Platform by connecting engineering metadata with operational tooling.

---

# Platform Engineering Principles

Our Service Catalog follows these principles:

- Every engineering asset should be discoverable.
- Every production service must have a clearly defined owner.
- Metadata should be accurate, complete, and continuously maintained.
- Operational information should be easily accessible.
- Relationships between services should be explicitly modeled.
- Automation should keep metadata synchronized wherever possible.
- The catalog should support governance without creating unnecessary administrative overhead.

---

# Key Takeaways

- The Service Catalog is the authoritative inventory of engineering assets within the organization.
- Standardized metadata enables discoverability, ownership, governance, and automation.
- Every production service should define its lifecycle, ownership, operational metadata, and dependencies.
- Service tiers help determine operational expectations and business criticality.
- Platform Engineering owns the catalog, while engineering teams own the accuracy of their service metadata.
- A well-maintained Service Catalog improves developer experience, operational efficiency, and organizational reliability.