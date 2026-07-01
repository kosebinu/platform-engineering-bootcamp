# GitOps Philosophy

## Purpose

This document describes the GitOps philosophy adopted by the Platform Engineering Team for managing Kubernetes applications and infrastructure.

Our goal is to provide a deployment model that is secure, repeatable, observable, and easy for developers to use while reducing operational risk.

---

# What is GitOps?

GitOps is an operational model in which Git serves as the single source of truth for both application and infrastructure configuration.

Instead of engineers manually deploying resources to Kubernetes using tools such as `kubectl apply`, all desired system state is stored declaratively in Git.

A GitOps controller, such as Argo CD, continuously compares the desired state stored in Git with the actual state running inside the Kubernetes cluster. Whenever differences are detected, the controller automatically reconciles the cluster so that it matches the configuration stored in Git.

---

# Why Git?

Git provides several capabilities that make it an ideal source of truth:

- Version control
- Complete change history
- Pull request workflow
- Code review
- Rollback capability
- Auditability
- Collaboration

Every infrastructure or application change is tracked, reviewed, and reproducible.

---

# Why Git is the Single Source of Truth

The Platform Team has chosen Git as the authoritative source for platform configuration.

This means:

- Developers propose changes through Pull Requests.
- Approved changes are merged into Git.
- Git becomes the desired state of the platform.
- The cluster should always converge toward the state defined in Git.

Manual changes made directly inside the Kubernetes cluster are considered configuration drift and should be corrected automatically.

---

# The Problem GitOps Solves

Without GitOps, engineers often deploy applications manually using commands such as:

```bash
kubectl apply -f deployment.yaml
```

or

```bash
helm upgrade --install
```

While these commands work, they introduce several problems:

- Manual deployments are difficult to audit.
- Configuration drift occurs when clusters differ from Git.
- Rollbacks become more complicated.
- Production changes may bypass code review.
- Different engineers may deploy different versions.

As systems grow, these inconsistencies become operational risks.

---

# Reconciliation

Reconciliation is the core concept behind GitOps.

The GitOps controller continuously performs the following cycle:

1. Read the desired configuration from Git.
2. Read the current state of the Kubernetes cluster.
3. Compare both states.
4. Detect differences.
5. Apply the necessary changes so that the cluster matches Git.

This process runs continuously rather than only during deployments.

---

# Configuration Drift

Configuration drift occurs when the actual state of the Kubernetes cluster no longer matches the configuration stored in Git.

For example:

Git:

```yaml
replicas: 3
```

Cluster:

```yaml
replicas: 8
```

This inconsistency creates uncertainty because engineers no longer know which version represents the intended system.

GitOps automatically detects and corrects this drift.

---

# Self-Healing

One of the most valuable capabilities of GitOps is self-healing.

Examples include:

- Recreating deleted resources
- Restoring modified configurations
- Reapplying desired replica counts
- Correcting accidental manual changes

Because Git remains the source of truth, the platform continuously restores the desired state.

---

# Benefits of GitOps

The Platform Team adopts GitOps because it provides:

- Consistent deployments
- Improved security
- Full audit history
- Easier rollback
- Reduced operational errors
- Automatic drift detection
- Self-healing infrastructure
- Better developer experience

---

# Platform Engineering Principles

Our platform follows these principles:

- Git is the single source of truth.
- Infrastructure is managed declaratively.
- All production changes occur through Pull Requests.
- Developers interact with Git rather than Kubernetes.
- Platform controllers reconcile desired and actual state automatically.
- Manual production changes should be avoided.

---

# High-Level GitOps Workflow

```text
Developer
    │
    ▼
Pull Request
    │
    ▼
Code Review
    │
    ▼
Merge to Main
    │
    ▼
Git Repository
    │
    ▼
Argo CD
    │
    ▼
Compare Desired State
    │
    ▼
Synchronize Cluster
    │
    ▼
Application Running
```

---

# Our GitOps Vision

Our Internal Developer Platform is designed so that developers never need to manually deploy applications using Kubernetes commands.

Instead, developers define their desired application configuration in Git, and the platform automatically delivers, monitors, and maintains that application through continuous reconciliation.

This approach provides a secure, scalable, and reliable deployment model that aligns with modern Platform Engineering best practices.