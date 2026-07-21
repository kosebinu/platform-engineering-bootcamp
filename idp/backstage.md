# Backstage

## Purpose

This document provides an overview of Backstage and its role within the organization's Internal Developer Platform (IDP).

Backstage serves as the central developer portal that unifies engineering tools, documentation, service metadata, deployment workflows, and operational information into a single platform. It enables engineering teams to discover, create, deploy, and operate software using standardized, self-service workflows.

The Platform Engineering Team owns and maintains Backstage as a core component of the Internal Developer Platform.

---

# What is Backstage?

Backstage is an open-source framework for building Internal Developer Platforms (IDPs).

Originally developed by Spotify and now part of the Cloud Native Computing Foundation (CNCF), Backstage provides a centralized portal where engineers can interact with the organization's software ecosystem.

Rather than requiring developers to navigate multiple independent systems, Backstage provides a unified interface for:

- Service discovery
- Software templates
- Technical documentation
- CI/CD visibility
- Kubernetes workloads
- Infrastructure resources
- Engineering ownership
- Operational dashboards

Backstage does not replace infrastructure platforms such as Kubernetes or cloud providers. Instead, it integrates them into a consistent developer experience.

---

# Why Organizations Use Backstage

As organizations grow, engineering systems become increasingly complex.

Developers often need to interact with many different tools, including:

- Source code repositories
- CI/CD platforms
- Kubernetes clusters
- Monitoring systems
- Documentation portals
- Incident management tools
- Cloud platforms

Without a centralized platform, engineers spend significant time locating information and understanding ownership.

Backstage addresses this challenge by providing:

- A single developer portal
- Consistent engineering workflows
- Centralized service ownership
- Improved discoverability
- Self-service capabilities
- Standardized development practices

This improves developer productivity while reducing operational overhead.

---

# Core Features

Backstage provides several foundational capabilities for modern Platform Engineering.

## Developer Portal

A centralized web interface that serves as the entry point for engineering teams.

Developers can:

- Browse services
- View documentation
- Create new applications
- Access dashboards
- Explore APIs
- Review deployments
- Discover ownership information

---

## Software Catalog

The Software Catalog provides a searchable inventory of engineering assets.

Each catalog entry contains operational metadata such as:

- Service owner
- Engineering team
- Repository
- Documentation
- APIs
- Kubernetes resources
- Dependencies
- Lifecycle status

The catalog becomes the authoritative source of engineering metadata across the organization.

---

## Software Templates

Software Templates enable engineers to create new services using standardized project templates.

Templates typically automate:

- Repository creation
- Project scaffolding
- CI/CD configuration
- Kubernetes manifests
- Helm charts
- Documentation
- Catalog registration

Templates ensure new projects follow organizational best practices from the beginning.

---

## TechDocs

TechDocs provides documentation-as-code capabilities.

Documentation is stored alongside application source code and automatically published within Backstage.

Advantages include:

- Version-controlled documentation
- Consistent formatting
- Searchable content
- Documentation maintained with the application lifecycle

This encourages engineers to treat documentation as part of the software product.

---

## Plugin Architecture

Backstage is designed around a modular plugin architecture.

Plugins integrate external engineering systems into the developer portal.

Common integrations include:

- GitHub
- GitLab
- Azure DevOps
- Jenkins
- Argo CD
- Kubernetes
- Grafana
- Prometheus
- PagerDuty
- SonarQube

Organizations can also develop custom plugins to integrate internal tools and workflows.

The plugin architecture allows Backstage to evolve without requiring changes to its core framework.

---

# Software Catalog

The Software Catalog is the foundation of Backstage.

It stores metadata describing software components and infrastructure resources.

Typical information includes:

- Service name
- Owner
- Team
- Repository
- APIs
- Dependencies
- Documentation
- Runtime environment
- Lifecycle stage

The Software Catalog enables:

- Service discovery
- Ownership visibility
- Dependency mapping
- Operational governance
- Platform automation

Maintaining accurate catalog metadata is essential for an effective Internal Developer Platform.

---

# Scaffolder

The Backstage Scaffolder enables self-service project creation.

Instead of manually creating repositories and configuring infrastructure, developers complete a guided workflow.

The Scaffolder can automatically:

- Create Git repositories
- Generate application code
- Configure CI/CD pipelines
- Generate Helm charts
- Register services in the Software Catalog
- Create documentation
- Apply organizational standards

This reduces onboarding time while promoting consistency across engineering teams.

---

# TechDocs

TechDocs is Backstage's documentation platform.

Documentation is written using Markdown and stored in the application's source repository.

During the documentation build process:

1. Documentation is generated.
2. Technical content is published.
3. Search indexes are updated.
4. Documentation becomes available within Backstage.

Benefits include:

- Documentation stays close to the code.
- Version history is preserved.
- Documentation is automatically published.
- Engineering knowledge becomes easier to discover.

---

# Benefits

## For Developers

- Single entry point for engineering tools
- Faster onboarding
- Self-service application creation
- Easier service discovery
- Improved documentation
- Reduced context switching

---

## For Platform Engineering

- Standardized engineering workflows
- Centralized platform governance
- Reduced manual support
- Better platform adoption
- Easier operational management

---

## For the Organization

- Improved developer productivity
- Faster software delivery
- Better engineering collaboration
- Increased operational consistency
- Stronger governance
- Higher platform reliability

---

# High-Level Architecture

```
                        Developers
                             │
                             ▼
                    Backstage Portal
                             │
     ┌──────────────┬───────────────┬──────────────┐
     ▼              ▼               ▼              ▼
Software Catalog  Scaffolder     TechDocs      Plugins
     │              │               │              │
     └──────────────┼───────────────┴──────────────┘
                    ▼
          Engineering Tool Integrations
                    │
     ┌──────────────┼──────────────┬──────────────┐
     ▼              ▼              ▼              ▼
 GitHub        Kubernetes      CI/CD        Observability
                    │
                    ▼
             Internal Developer Platform
```

Backstage acts as the presentation layer of the Internal Developer Platform, integrating engineering systems into a unified developer experience.

---

# Platform Team Responsibilities

The Platform Engineering Team is responsible for designing, operating, and continuously improving Backstage.

Key responsibilities include:

## Platform Development

- Configure Backstage
- Develop custom plugins
- Maintain software templates
- Integrate engineering tools

---

## Service Catalog Management

- Define catalog standards
- Maintain metadata quality
- Review ownership information
- Validate catalog registrations

---

## Developer Experience

- Improve usability
- Simplify engineering workflows
- Gather developer feedback
- Reduce onboarding time

---

## Platform Governance

- Establish platform standards
- Maintain Golden Paths
- Promote best practices
- Enforce organizational policies

---

## Continuous Improvement

The Platform Team should regularly evaluate:

- Platform adoption
- User feedback
- Workflow efficiency
- Plugin effectiveness
- Documentation quality
- Operational metrics

---

# Platform Engineering Principles

Our use of Backstage follows these principles:

- Treat the platform as a product.
- Provide a single entry point for engineering workflows.
- Prefer self-service over manual requests.
- Standardize engineering practices through templates.
- Keep documentation close to the source code.
- Maintain accurate service metadata.
- Enable discoverability across engineering assets.
- Improve developer experience through automation.
- Continuously evolve the platform based on customer feedback.

---

# Key Takeaways

- Backstage is an open-source framework for building Internal Developer Platforms.
- It provides a centralized developer portal that integrates engineering tools, documentation, and operational metadata.
- The Software Catalog serves as the authoritative source of service ownership and engineering metadata.
- The Scaffolder enables standardized, self-service project creation.
- TechDocs promotes documentation-as-code and keeps technical knowledge aligned with application development.
- The plugin architecture allows organizations to integrate internal and third-party engineering tools.
- The Platform Engineering Team owns and continuously improves Backstage to enhance developer productivity, governance, and operational excellence.