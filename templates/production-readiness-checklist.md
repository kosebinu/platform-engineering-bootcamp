# Production Readiness Checklist (PRC)

> **Purpose**
>
> This checklist must be completed by the application team before requesting production deployment approval from the Platform Engineering Team.
>
> The objective is to ensure that every production service meets the organization's operational, reliability, security, and observability standards.

---

# Service Information

| Field | Value |
|--------|-------|
| Service Name | |
| Application Description | |
| Business Owner | |
| Engineering Team | |
| Engineering Owner | |
| Product Owner | |
| Repository URL | |
| Environment | |
| Kubernetes Namespace | |
| Primary Contact | |
| On-Call Team | |
| Planned Deployment Date | |
| PRR Review Date | |

---

# Architecture Checklist

Verify that the application follows the organization's architecture standards.

| Requirement | Status | Notes |
|------------|:------:|------|
| Stateless architecture (where applicable) | ☐ | |
| Twelve-Factor App principles followed | ☐ | |
| Configuration externalized | ☐ | |
| Secrets stored outside application code | ☐ | |
| Health endpoints implemented | ☐ | |
| Kubernetes deployment manifests reviewed | ☐ | |
| Dependencies documented | ☐ | |
| Platform standards followed | ☐ | |

---

# Reliability Checklist

Verify the application can operate reliably in production.

| Requirement | Status | Notes |
|------------|:------:|------|
| Readiness Probe configured | ☐ | |
| Liveness Probe configured | ☐ | |
| Startup Probe configured (if required) | ☐ | |
| Resource Requests configured | ☐ | |
| Resource Limits configured | ☐ | |
| Graceful Shutdown implemented | ☐ | |
| Retry policy implemented | ☐ | |
| Request timeouts configured | ☐ | |
| Rolling Update strategy verified | ☐ | |
| Pod Disruption Budget configured (if required) | ☐ | |

---

# Security Checklist

Verify compliance with security requirements.

| Requirement | Status | Notes |
|------------|:------:|------|
| Secrets managed securely | ☐ | |
| RBAC configured | ☐ | |
| Container runs as non-root | ☐ | |
| Security Context configured | ☐ | |
| Container image vulnerability scan completed | ☐ | |
| TLS enabled where required | ☐ | |
| Least Privilege Principle followed | ☐ | |
| Network Policies implemented (if applicable) | ☐ | |
| Sensitive data excluded from logs | ☐ | |

---

# Observability Checklist

Verify the application can be monitored and supported in production.

| Requirement | Status | Notes |
|------------|:------:|------|
| Prometheus metrics exposed | ☐ | |
| Structured logging implemented | ☐ | |
| OpenTelemetry instrumentation enabled | ☐ | |
| Distributed tracing verified | ☐ | |
| Grafana dashboard available | ☐ | |
| Alerting rules configured | ☐ | |
| Health endpoint verified | ☐ | |
| Service Level Objectives (SLOs) defined | ☐ | |
| Logs searchable in Grafana/Loki | ☐ | |

---

# Scalability Checklist

Verify the application can scale as demand increases.

| Requirement | Status | Notes |
|------------|:------:|------|
| Horizontal Pod Autoscaler configured (if applicable) | ☐ | |
| Load testing completed | ☐ | |
| Performance testing completed | ☐ | |
| Resource sizing validated | ☐ | |
| Database connection pooling configured | ☐ | |
| Autoscaling strategy documented | ☐ | |
| Capacity planning completed | ☐ | |

---

# Disaster Recovery Checklist

Verify recovery procedures have been defined and validated.

| Requirement | Status | Notes |
|------------|:------:|------|
| Backup strategy documented | ☐ | |
| Restore procedure documented | ☐ | |
| Recovery procedure tested | ☐ | |
| Recovery Time Objective (RTO) defined | ☐ | |
| Recovery Point Objective (RPO) defined | ☐ | |
| Multi-zone deployment verified (if required) | ☐ | |
| Multi-region strategy documented (if required) | ☐ | |

---

# Operational Readiness Checklist

Verify operational support is available.

| Requirement | Status | Notes |
|------------|:------:|------|
| Runbooks completed | ☐ | |
| Incident response documented | ☐ | |
| Alert routing verified | ☐ | |
| Monitoring dashboards validated | ☐ | |
| Escalation procedure documented | ☐ | |
| On-call rotation established | ☐ | |
| Maintenance procedures documented | ☐ | |

---

# Documentation Checklist

Verify documentation is complete and accessible.

| Requirement | Status | Notes |
|------------|:------:|------|
| Architecture documentation | ☐ | |
| Deployment guide | ☐ | |
| Configuration guide | ☐ | |
| Dashboard documentation | ☐ | |
| Alert documentation | ☐ | |
| API documentation (if applicable) | ☐ | |
| Dependency documentation | ☐ | |
| Disaster recovery documentation | ☐ | |
| Operational runbooks | ☐ | |

---

# Ownership Checklist

Verify ownership has been clearly established.

| Requirement | Status | Notes |
|------------|:------:|------|
| Engineering owner assigned | ☐ | |
| Product owner assigned | ☐ | |
| On-call team assigned | ☐ | |
| Escalation contacts documented | ☐ | |
| Team Slack / Microsoft Teams channel defined | ☐ | |
| Source repository maintained | ☐ | |
| Service ownership documented | ☐ | |

---

# Risks and Exceptions

Document any known risks, accepted exceptions, or outstanding action items.

| Risk / Exception | Mitigation | Owner | Target Date |
|------------------|------------|-------|-------------|
| | | | |
| | | | |
| | | | |

---

# Platform Engineering Review

| Review Item | Status |
|-------------|:------:|
| Architecture Approved | ☐ |
| Reliability Approved | ☐ |
| Security Approved | ☐ |
| Observability Approved | ☐ |
| Scalability Approved | ☐ |
| Disaster Recovery Approved | ☐ |
| Operational Readiness Approved | ☐ |
| Documentation Approved | ☐ |
| Ownership Verified | ☐ |

---

# Final Decision

**Production Readiness Status**

- ☐ Approved
- ☐ Approved with Conditions
- ☐ Rejected

---

## Platform Engineering Comments

```
____________________________________________________________

____________________________________________________________

____________________________________________________________
```

---

## Required Follow-up Actions

| Action | Owner | Due Date |
|---------|-------|----------|
| | | |
| | | |
| | | |

---

# Approval Signatures

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Application Owner | | | |
| Platform Engineer | | | |
| Security Reviewer | | | |
| Engineering Manager | | | |

---

# Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | | | Initial Production Readiness Checklist |