# Multi-Cluster GitOps Architecture

## Purpose

This document describes the Platform Team's approach to managing multiple Kubernetes clusters using GitOps and Argo CD.

As our platform grows, a single Kubernetes cluster becomes insufficient for meeting requirements around availability, scalability, security, compliance, and operational isolation. This document explains why multiple clusters exist, how Argo CD manages them, and the architectural patterns used to scale GitOps across the organization.

---

# Why Multiple Clusters Exist

Running all workloads in a single Kubernetes cluster creates operational and business risks. Modern enterprises typically operate multiple clusters for several reasons.

## 1. High Availability

Each Kubernetes cluster represents an independent failure domain.

If one cluster experiences an outage, applications running in other clusters continue operating.

Example:

```
AKS-US-EAST
    │
    ├── Failure
    │
    ▼
Traffic shifts to

AKS-US-WEST
```

This improves business continuity and reduces downtime.

---

## 2. Geographic Distribution

Applications are often deployed closer to users to reduce latency.

Example:

```
North America
    │
    ▼
AKS-US

Europe
    │
    ▼
AKS-EU

Asia
    │
    ▼
AKS-ASIA
```

Users connect to the nearest region, improving application performance.

---

## 3. Regulatory Compliance

Some regulations require customer data to remain within specific geographic regions.

Examples include:

- GDPR (European Union)
- HIPAA (United States)
- Country-specific data residency laws

Using separate regional clusters helps satisfy these compliance requirements.

---

## 4. Team Isolation

Different engineering teams may own different clusters.

Example:

```
Payments Team
    │
    ▼
AKS-PAYMENTS

AI Platform Team
    │
    ▼
AKS-AI

Platform Team
    │
    ▼
AKS-PLATFORM
```

This limits the impact of operational mistakes and allows teams to work independently.

---

## 5. Resource Optimization

Different workloads require different hardware.

Examples:

- GPU clusters for AI workloads
- General-purpose clusters for web applications
- High-memory clusters for analytics

Separate clusters allow infrastructure to be optimized for workload requirements.

---

# Failure Domains

A failure domain is a boundary within which failures are contained.

Each Kubernetes cluster should be treated as an independent failure domain.

Example:

```
AKS-US-EAST

Failure

↓

Applications unavailable

↓

AKS-US-WEST continues serving traffic
```

This prevents a single infrastructure issue from affecting every application.

Designing clusters as independent failure domains improves resilience and disaster recovery.

---

# Multi-Cluster GitOps

Instead of manually deploying applications to each cluster, the Platform Team uses Argo CD as a centralized GitOps controller.

```
                    Git Repository
                          │
                          ▼
                     Argo CD
                          │
         ┌────────────────┼────────────────┐
         ▼                ▼                ▼
     AKS-DEV         AKS-STAGE        AKS-PROD
         │                │                │
         ▼                ▼                ▼
   Kubernetes Apps  Kubernetes Apps  Kubernetes Apps
```

Git remains the single source of truth.

Argo CD continuously reconciles each registered cluster with the desired configuration stored in Git.

---

# Cluster Registration

Before Argo CD can deploy applications to a cluster, the cluster must be registered.

Conceptually:

```bash
argocd cluster add aks-dev

argocd cluster add aks-stage

argocd cluster add aks-prod
```

Registering a cluster allows Argo CD to:

- Authenticate with the Kubernetes API
- Deploy applications
- Monitor health
- Detect configuration drift
- Perform self-healing

Once registered, clusters become deployment targets for GitOps workflows.

---

# Cluster Generator

Managing Application manifests manually for every cluster does not scale.

Instead, ApplicationSets use the Cluster Generator.

Example:

```yaml
generators:
  - clusters: {}
```

The Cluster Generator automatically discovers every cluster registered with Argo CD.

Example:

Registered clusters:

```
aks-dev

aks-stage

aks-prod
```

The generator automatically creates Application resources for each cluster without requiring additional YAML.

This significantly reduces manual maintenance as the platform grows.

---

# Combining Git Generator and Cluster Generator

One of the most powerful features of ApplicationSets is combining multiple generators.

For example:

Applications:

```
payment

inventory

orders
```

Clusters:

```
dev

stage

prod
```

ApplicationSet automatically generates:

```
payment → dev

payment → stage

payment → prod

inventory → dev

inventory → stage

inventory → prod

orders → dev

orders → stage

orders → prod
```

This is commonly achieved using a Matrix Generator, allowing Argo CD to deploy every application to every target cluster with minimal configuration.

---

# Centralized vs Federated GitOps

There are two common approaches for managing multiple clusters.

## Centralized GitOps

A single Argo CD instance manages every cluster.

```
                Argo CD

                   │

      ┌────────────┼────────────┐

      ▼            ▼            ▼

  AKS-DEV     AKS-STAGE     AKS-PROD
```

### Advantages

- Single control plane
- Simplified management
- Centralized governance
- Easier onboarding

### Disadvantages

- Larger blast radius
- Higher dependency on a single Argo CD instance
- May become difficult to scale for very large organizations

---

## Federated GitOps

Each environment or business unit operates its own Argo CD instance.

```
Argo CD (Development)

        │

        ▼

    AKS-DEV

------------------------

Argo CD (Staging)

        │

        ▼

    AKS-STAGE

------------------------

Argo CD (Production)

        │

        ▼

    AKS-PROD
```

### Advantages

- Better isolation
- Independent upgrades
- Reduced operational risk
- Smaller blast radius

### Disadvantages

- More infrastructure to manage
- Additional operational complexity
- More Argo CD instances to maintain

The appropriate model depends on organizational size, security requirements, and operational maturity.

---

# Multi-Cluster Architecture Diagram

```
                           GitHub
                              │
                              ▼
                    Argo CD Control Plane
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
      AKS-DEV            AKS-STAGE           AKS-PROD
          │                   │                   │
          ▼                   ▼                   ▼
    Payment API         Payment API         Payment API
    Inventory API       Inventory API       Inventory API
    Orders API          Orders API          Orders API
```

The Platform Team manages deployments centrally through Git, while each cluster operates independently.

---

# Platform Engineering Principles

Our multi-cluster GitOps strategy follows these principles:

- Git is the single source of truth.
- Kubernetes clusters are independent failure domains.
- Applications are deployed declaratively through GitOps.
- Argo CD continuously reconciles desired and actual state.
- ApplicationSets eliminate repetitive configuration.
- Platform Engineers build automation rather than performing manual deployments.
- Developers interact with Git instead of Kubernetes clusters.

---

# Key Takeaways

- Multiple clusters improve availability, scalability, compliance, and isolation.
- Each cluster should be treated as an independent failure domain.
- Argo CD manages multiple clusters through cluster registration.
- Cluster Generators automatically discover deployment targets.
- Matrix Generators combine applications and clusters to eliminate repetitive YAML.
- Centralized and Federated GitOps are both valid architectures depending on organizational needs.
- GitOps enables consistent, secure, and scalable application delivery across an enterprise Kubernetes platform.