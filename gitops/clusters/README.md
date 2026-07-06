# Multi-Cluster GitOps

This directory contains cluster-specific GitOps configuration.

Each cluster represents an independent deployment target.

## Structure

- dev/
- stage/
- prod/

Future platform components such as monitoring, ingress controllers, policies, and cluster-specific ApplicationSets will be stored here.

The goal is to separate application configuration from cluster-specific infrastructure while allowing Argo CD to manage all clusters from a single control plane.