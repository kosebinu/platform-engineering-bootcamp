# Progressive Delivery Architecture

## Purpose

This document describes the Platform Team's approach to deploying application updates safely using Progressive Delivery.

Traditional deployment strategies expose all users to a new application version immediately after deployment. While simple, this approach increases the risk of widespread outages when defects reach production.

Progressive Delivery reduces deployment risk by gradually exposing new versions to users while continuously monitoring application health. If issues are detected, the platform automatically pauses or rolls back the deployment before the majority of users are affected.

This approach enables safer software releases while maintaining Git as the single source of truth through GitOps.

---

# What is Progressive Delivery?

Progressive Delivery is a deployment strategy that gradually releases new versions of an application instead of exposing every user to the new version immediately.

Rather than replacing all running application instances at once, traffic is shifted incrementally while platform monitoring continuously evaluates application health.

Typical deployment progression:

```
Version 1

↓

Deploy Version 2

↓

5% Traffic

↓

Monitor

↓

20% Traffic

↓

Monitor

↓

50% Traffic

↓

Monitor

↓

100% Traffic
```

Each stage provides an opportunity to detect failures before impacting all users.

---

# Why Progressive Delivery?

Modern software systems are complex.

Even after:

- Unit testing
- Integration testing
- End-to-end testing
- Staging validation

Unexpected issues can still occur in production.

Examples include:

- Increased latency
- Memory leaks
- Database bottlenecks
- External API failures
- Traffic-specific bugs
- Regional failures

Progressive Delivery reduces the blast radius of these failures.

---

# Deployment Strategies

## Rolling Update

Rolling Update is Kubernetes' default deployment strategy.

```
Old Pods

↓

Gradually replaced

↓

New Pods
```

Example:

```
10 Pods

↓

9 Old
1 New

↓

8 Old
2 New

↓

...

↓

10 New
```

### Advantages

- Built into Kubernetes
- No additional tooling
- Simple deployment model
- Minimal resource overhead

### Disadvantages

- Rollback may take time
- Every user eventually receives the new version
- Difficult to validate before full rollout

---

## Blue/Green Deployment

Blue/Green maintains two complete environments simultaneously.

```
Blue

Version 1

---------------------

Green

Version 2
```

Users continue accessing the Blue environment while Green is validated.

After validation:

```
Blue

0% Traffic

↓

Green

100% Traffic
```

### Advantages

- Fast rollback
- Complete environment validation
- Zero-downtime switch

### Disadvantages

- Requires duplicate infrastructure
- Higher temporary infrastructure costs

---

## Canary Deployment

Canary deployments expose a small percentage of production traffic to the new version before gradually increasing traffic.

Example:

```
95%

↓

Version 1

5%

↓

Version 2
```

If monitoring indicates healthy behavior:

```
80%

↓

Version 1

20%

↓

Version 2
```

Eventually:

```
100%

↓

Version 2
```

### Advantages

- Lowest deployment risk
- Early detection of production issues
- Automatic rollback supported
- Excellent customer experience

### Disadvantages

- More complex implementation
- Requires traffic management
- Requires monitoring and automated analysis

---

# Comparison of Deployment Strategies

| Strategy | Downtime | Rollback Speed | Infrastructure Cost | Risk |
|-----------|----------|----------------|---------------------|------|
| Rolling Update | None | Moderate | Low | Medium |
| Blue/Green | None | Very Fast | High | Low |
| Canary | None | Fast | Medium | Very Low |

---

# Argo Rollouts

Argo Rollouts extends Kubernetes with advanced deployment strategies.

Instead of using the standard Kubernetes Deployment resource:

```yaml
kind: Deployment
```

Applications use:

```yaml
kind: Rollout
```

The Rollout controller manages:

- Canary deployments
- Blue/Green deployments
- Traffic shifting
- Pause steps
- Automated promotion
- Automated rollback
- Health analysis

This enables safer production releases without changing application code.

---

# Argo Rollouts Architecture

```
Developer

        │

        ▼

GitHub Pull Request

        │

        ▼

Merge

        │

        ▼

Argo CD

        │

        ▼

Argo Rollouts

        │

        ▼

Canary Deployment

        │

        ▼

Metrics Evaluation

        │

        ├──────────────┐

Healthy              Unhealthy

│                    │

▼                    ▼

Promote         Automatic Rollback

│

▼

Production
```

Argo CD is responsible for synchronizing Git with Kubernetes.

Argo Rollouts is responsible for controlling how new versions are released.

---

# GitOps Integration

The Platform Team follows GitOps principles for all deployments.

Deployment workflow:

1. Developer updates application code.
2. CI builds a new container image.
3. Developer updates the image tag in Git.
4. Pull Request is reviewed and merged.
5. Argo CD synchronizes the new configuration.
6. Argo Rollouts performs a progressive deployment.
7. Metrics determine whether the rollout continues or rolls back.

Git remains the authoritative source for deployment configuration throughout the process.

---

# Automatic Rollback

One of the most valuable capabilities of Progressive Delivery is automatic rollback.

During deployment, Argo Rollouts continuously evaluates application health using metrics such as:

- Error rate
- Request latency
- CPU utilization
- Memory utilization
- Availability
- Custom Prometheus metrics

If configured thresholds are exceeded:

```
Canary

↓

Health Check Failed

↓

Abort Rollout

↓

Restore Previous Version
```

This minimizes customer impact while preserving platform stability.

---

# When to Use Each Deployment Strategy

## Rolling Update

Recommended for:

- Internal tools
- Development environments
- Low-risk services
- Stateless applications

---

## Blue/Green

Recommended for:

- Critical business applications
- Large infrastructure upgrades
- Applications requiring rapid rollback
- Database migrations with careful planning

---

## Canary

Recommended for:

- Customer-facing APIs
- Payment systems
- AI services
- High-traffic web applications
- Mission-critical production systems

The Platform Team recommends Canary deployments whenever production risk should be minimized.

---

# Platform Engineering Principles

Our platform follows these deployment principles:

- Git is the single source of truth.
- Every deployment is declarative.
- Production changes occur through Pull Requests.
- Progressive Delivery reduces deployment risk.
- Metrics drive deployment decisions.
- Rollbacks should be automatic whenever possible.
- Platform automation replaces manual deployment operations.

---

# Key Takeaways

- Progressive Delivery reduces deployment risk by gradually exposing new versions to users.
- Rolling Updates are simple but provide limited deployment control.
- Blue/Green deployments offer fast rollback at the cost of additional infrastructure.
- Canary deployments provide the safest production rollout strategy through gradual traffic shifting.
- Argo CD manages Git synchronization, while Argo Rollouts manages deployment strategy.
- Automated monitoring and rollback enable safer, more reliable software delivery.
- Progressive Delivery is a foundational capability of modern Platform Engineering.