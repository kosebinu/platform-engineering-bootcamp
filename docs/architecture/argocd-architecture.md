# Argo CD Architecture

## Purpose

This document explains the architecture of Argo CD and how it supports the GitOps deployment model used by the Platform Engineering Team.

Argo CD is used to continuously reconcile Kubernetes clusters with the desired state stored in Git.

---

## What is Argo CD?

Argo CD is a GitOps continuous delivery tool for Kubernetes.

It monitors Git repositories that contain Kubernetes manifests, Helm charts, or Kustomize configurations and ensures that the Kubernetes cluster matches the desired state defined in Git.

Instead of engineers manually running `kubectl apply` or `helm install`, Argo CD continuously compares Git with the cluster and applies changes when needed.

---

## Why We Use Argo CD

The Platform Team uses Argo CD because it provides:

- Git as the single source of truth
- Declarative deployments
- Automated synchronization
- Drift detection
- Self-healing
- Rollback through Git history
- Improved auditability
- Consistent deployments across environments

---

## High-Level Architecture

```text
Git Repository
      |
      v
Argo CD Repository Server
      |
      v
Rendered Kubernetes Manifests
      |
      v
Argo CD Application Controller
      |
      v
Kubernetes API Server
      |
      v
AKS Cluster