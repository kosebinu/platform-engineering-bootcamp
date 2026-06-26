# GitOps

## What is GitOps?

GitOps is an operational model where Git serves as the single source of truth for infrastructure and application configuration.

Changes are made through Git commits instead of manual operations.

A GitOps controller continuously reconciles the actual state of the system with the desired state stored in Git.

---

## Benefits

- Version controlled deployments
- Auditability
- Rollback through Git
- Drift detection
- Continuous reconciliation
- Improved security
- Consistent deployments

---

## Desired State

The desired state is the configuration stored in Git.

---

## Actual State

The actual state is the configuration currently running in Kubernetes.

---

## Reconciliation

GitOps controllers continuously compare desired state with actual state.

If differences exist, the controller automatically updates the cluster.

---

## GitOps Workflow

Developer

↓

Git Commit

↓

Pull Request

↓

Merge

↓

ArgoCD detects change

↓

Deploys to AKS

↓

Continuously monitors for drift