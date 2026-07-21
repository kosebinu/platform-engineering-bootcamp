# Backstage Entity Model

## Purpose

This document defines the standard Backstage entity model used within the organization's Internal Developer Platform (IDP).

The Software Catalog represents engineering assets as entities. These entities describe software components, infrastructure resources, APIs, teams, and users, along with the relationships between them.

Maintaining accurate entity metadata enables service discovery, ownership tracking, dependency visualization, automation, governance, and operational excellence.

---

# What is an Entity?

An entity is a structured representation of an engineering asset stored within the Backstage Software Catalog.

Examples include:

- Applications
- APIs
- Databases
- Message queues
- Teams
- Engineers
- Business systems

Each entity contains metadata describing ownership, lifecycle, relationships, and operational information.

---

# Component

## Purpose

A Component represents a deployable software asset.

Examples include:

- payment-api
- billing-service
- inventory-worker
- authentication-service
- frontend-web
- mobile-backend

Components are the most common entity type within the Software Catalog.

---

## Typical Metadata

- Service name
- Description
- Owner
- Repository
- Lifecycle
- System
- Runtime
- Language
- Kubernetes namespace
- Documentation
- Deployment information

---

## Example

```yaml
kind: Component

metadata:
  name: payment-api

spec:
  type: service
  owner: payments-team
  system: payments
  lifecycle: production
```

---

# API

## Purpose

An API entity represents an interface exposed by a service.

Examples:

- Payment REST API
- Customer GraphQL API
- Order Events API
- Authentication API

An API entity documents how other services interact with the application.

---

## Typical Metadata

- API name
- Owner
- Protocol
- Version
- Documentation
- Definition
- Consumers

---

## Example

```yaml
kind: API

metadata:
  name: payment-rest-api

spec:
  type: openapi
  owner: payments-team
```

---

# System

## Purpose

A System represents a collection of related software components that together provide a business capability.

A System groups multiple services into a logical business domain.

Examples:

- Payments
- Inventory
- Customer Management
- Identity
- Analytics

---

## Typical Metadata

- System name
- Description
- Owner
- Business capability
- Documentation

---

## Example

```
Payments System

├── payment-api
├── billing-api
├── invoice-worker
└── payment-events-api
```

Grouping services into Systems makes large environments easier to understand.

---

# Resource

## Purpose

A Resource represents infrastructure consumed by applications.

Resources are generally not deployed by application teams but are depended upon by Components.

Examples:

- PostgreSQL database
- Redis cache
- Azure Storage Account
- Azure Key Vault
- Kafka cluster
- RabbitMQ
- Kubernetes Cluster
- Cosmos DB

---

## Typical Metadata

- Resource name
- Resource type
- Owner
- Environment
- Provider
- Region

---

## Example

```
PostgreSQL

↓

Used by

↓

payment-api
```

---

# Group

## Purpose

A Group represents an engineering team or organizational unit.

Examples:

- Platform Team
- Payments Team
- SRE Team
- Security Team
- AI Platform Team

Groups own engineering assets and operational responsibilities.

---

## Typical Metadata

- Team name
- Team lead
- Members
- Slack channel
- Email
- Escalation contact

---

## Example

```
Payments Team

Owns

↓

payment-api

billing-api

invoice-worker
```

---

# User

## Purpose

A User represents an individual engineer within the organization.

Users belong to one or more Groups.

Examples:

- Alice Smith
- Bob Johnson
- Jane Doe

User entities support ownership, approvals, and collaboration.

---

## Typical Metadata

- Name
- Email
- Team
- Role
- GitHub account
- PagerDuty account

---

# Relationships Between Entities

The Software Catalog becomes powerful because entities are connected.

Example:

```
                Payments System
                      │
       ┌──────────────┴──────────────┐
       ▼                             ▼
 payment-api                  billing-api
       │                             │
       ▼                             ▼
 Payment REST API          Billing REST API
       │                             │
       ▼                             ▼
 PostgreSQL Database       PostgreSQL Database
       │
       ▼
 Payments Team
       │
       ▼
 Jane Doe
```

These relationships provide complete visibility into the engineering ecosystem.

---

# Common Relationship Types

## Component belongs to System

```
payment-api

↓

Part Of

↓

Payments System
```

---

## Component exposes API

```
payment-api

↓

Exposes

↓

Payment REST API
```

---

## Component consumes Resource

```
payment-api

↓

Uses

↓

PostgreSQL
```

---

## Group owns Component

```
Payments Team

↓

Owns

↓

payment-api
```

---

## User belongs to Group

```
Jane Doe

↓

Member Of

↓

Payments Team
```

---

## API consumed by Component

```
inventory-api

↓

Consumed By

↓

order-service
```

---

# Ownership Model

Clear ownership is a core principle of Platform Engineering.

Every production entity must have an identified owner.

Ownership enables:

- Incident response
- Operational support
- Change management
- Security reviews
- Production readiness
- Platform governance

Ownership must never be ambiguous.

---

## Component Ownership

Each Component must define:

- Engineering owner
- Responsible team
- Repository
- Lifecycle
- On-call rotation

---

## API Ownership

Each API must define:

- Owning service
- Responsible team
- Documentation owner
- Version strategy

---

## Resource Ownership

Infrastructure resources should identify:

- Platform owner
- Responsible engineering team
- Environment
- Operational contacts

---

## System Ownership

Business Systems should define:

- Business owner
- Technical owner
- Supporting teams
- Architecture documentation

---

## Group Ownership

Groups should maintain:

- Team members
- Team lead
- Communication channels
- Escalation contacts

---

# Entity Lifecycle

Entities move through a defined lifecycle.

Typical stages include:

```
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

Lifecycle metadata helps engineers understand the maturity and support status of each entity.

---

# Metadata Standards

All catalog entities should include standardized metadata wherever applicable.

Required fields include:

- Name
- Description
- Owner
- Lifecycle
- Tags
- Repository
- Documentation
- System association

Optional metadata may include:

- Language
- Runtime
- Kubernetes namespace
- Cloud provider
- Environment
- Business capability
- Cost center

---

# Platform Engineering Responsibilities

The Platform Engineering Team is responsible for:

- Defining entity standards
- Maintaining metadata quality
- Reviewing ownership information
- Managing Software Catalog governance
- Building automation around catalog metadata
- Supporting engineering teams during registration
- Improving discoverability across engineering assets

---

# Platform Engineering Principles

Our entity model follows these principles:

- Every engineering asset should be discoverable.
- Every production asset must have a clear owner.
- Metadata should be accurate and continuously maintained.
- Relationships between entities should reflect the actual system architecture.
- Catalog metadata should enable automation and governance.
- Documentation and ownership should evolve with the service lifecycle.

---

# Key Takeaways

- The Backstage Software Catalog models engineering assets as entities.
- Components represent deployable applications and services.
- APIs define the interfaces exposed by components.
- Systems group related components into business capabilities.
- Resources represent infrastructure consumed by applications.
- Groups model engineering teams, while Users represent individual engineers.
- Relationships between entities provide visibility into ownership, dependencies, and architecture.
- A consistent ownership model enables effective operations, governance, and automation across the Internal Developer Platform.