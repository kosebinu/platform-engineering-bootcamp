# Production Readiness Review (PRR)

## Purpose

This document defines the Platform Engineering Team's Production Readiness Review (PRR) process.

A Production Readiness Review is a structured evaluation performed before deploying a new service or significant system change into production.

The purpose of a PRR is to ensure that a service is operationally prepared, secure, observable, scalable, and supportable before it becomes customer-facing.

The review helps reduce production risk while promoting consistent engineering standards across the organization.

The objectives of a PRR are to:

- Reduce production incidents
- Verify operational readiness
- Ensure platform compliance
- Improve system reliability
- Validate observability
- Confirm ownership and support responsibilities

---

# When PRRs Are Required

A Production Readiness Review should be completed before:

- Deploying a new production service
- Introducing major architectural changes
- Migrating applications to Kubernetes
- Launching customer-facing APIs
- Deploying multi-region services
- Releasing critical infrastructure components
- Introducing significant changes to platform dependencies

Routine bug fixes and small feature updates generally do not require a formal PRR.

---

# Production Readiness Review Categories

The Platform Team evaluates the following operational areas:

- Architecture
- Reliability
- Security
- Observability
- Scalability
- Disaster Recovery
- Operational Readiness
- Documentation
- Ownership

Each category must satisfy minimum platform standards before production approval.

---

# Architecture Review

The architecture review evaluates whether the application aligns with platform engineering standards.

Checklist:

- Cloud-native architecture
- Stateless application design (where applicable)
- Twelve-Factor App principles
- Configuration externalized
- Kubernetes compatible
- Dependencies documented
- Standard platform components used
- Health probes implemented

Questions:

- Can the application run reliably on Kubernetes?
- Are external dependencies clearly identified?
- Is configuration managed outside the application?

---

# Reliability Review

The reliability review evaluates the application's ability to remain available during normal and abnormal operating conditions.

Checklist:

- Readiness probes configured
- Liveness probes configured
- Startup probes (if required)
- Resource requests defined
- Resource limits defined
- Retry policies implemented
- Request timeouts configured
- Graceful shutdown supported
- Rolling updates supported

Questions:

- Can unhealthy instances be detected automatically?
- Can deployments occur without downtime?
- Does the application fail safely?

---

# Security Review

The security review validates compliance with platform security standards.

Checklist:

- Secrets stored securely
- RBAC configured
- Containers run as non-root
- Images scanned for vulnerabilities
- TLS enabled where required
- Least privilege enforced
- Network policies implemented (where applicable)
- Sensitive information not logged

Questions:

- Are credentials protected?
- Is access restricted appropriately?
- Has the application passed security scanning?

---

# Observability Review

Every production service must be observable.

Checklist:

- Metrics exposed
- Structured logging implemented
- Distributed tracing enabled
- Dashboards available
- Alerts configured
- SLOs defined
- Health endpoints implemented

Questions:

- Can engineers detect failures quickly?
- Can incidents be investigated efficiently?
- Can platform health be monitored continuously?

---

# Scalability Review

The scalability review evaluates how the application behaves as workload increases.

Checklist:

- Horizontal Pod Autoscaler configured (if applicable)
- Stateless architecture
- Connection pooling configured
- Resource requests validated
- Performance testing completed
- Load testing completed
- Autoscaling strategy documented

Questions:

- Can the application handle increased traffic?
- Can it scale horizontally?
- Has capacity been validated?

---

# Disaster Recovery Review

The disaster recovery review evaluates the application's resilience to failures.

Checklist:

- Backup strategy documented
- Recovery procedures documented
- Recovery tested
- Recovery Time Objective (RTO) defined
- Recovery Point Objective (RPO) defined
- Multi-zone deployment (if required)
- Multi-region strategy documented (if applicable)

Questions:

- How quickly can the service recover?
- What data loss is acceptable?
- Has recovery been tested?

---

# Operational Readiness

The Platform Team verifies that operational support is in place.

Checklist:

- Runbooks available
- Incident procedures documented
- On-call ownership assigned
- Alert routing configured
- Monitoring dashboards available
- Escalation procedures documented

Questions:

- Can the Platform Team support this service at 2 AM?
- Is operational knowledge documented?
- Are engineers prepared to respond to incidents?

---

# Documentation Requirements

Every production service should include the following documentation:

- System architecture
- Deployment guide
- Configuration guide
- Dependency documentation
- Runbooks
- Dashboard documentation
- Alert documentation
- Disaster recovery procedures
- SLO documentation
- API documentation (if applicable)

Documentation should be version-controlled and reviewed alongside application changes.

---

# Ownership Requirements

Every production service must have clearly defined ownership.

Required ownership includes:

- Engineering owner
- Product owner
- On-call rotation
- Escalation contacts
- Team communication channel
- Source repository
- Infrastructure ownership

Ownership must never be ambiguous.

---

# Production Readiness Checklist

| Category | Status |
|-----------|:------:|
| Architecture Reviewed | ☐ |
| Kubernetes Health Probes | ☐ |
| Resource Requests Defined | ☐ |
| Resource Limits Defined | ☐ |
| Security Review Completed | ☐ |
| Metrics Available | ☐ |
| Structured Logging Enabled | ☐ |
| Distributed Tracing Enabled | ☐ |
| Dashboards Created | ☐ |
| Alerts Configured | ☐ |
| SLO Defined | ☐ |
| Runbooks Completed | ☐ |
| Disaster Recovery Plan Reviewed | ☐ |
| Performance Testing Completed | ☐ |
| Load Testing Completed | ☐ |
| Ownership Assigned | ☐ |
| Documentation Complete | ☐ |
| Platform Team Approval | ☐ |

All mandatory items must be completed before production deployment approval.

---

# Common PRR Failures

The following issues commonly prevent services from passing a Production Readiness Review:

- Missing readiness or liveness probes
- No resource requests or limits
- Secrets committed to source control
- Missing dashboards
- Missing alerts
- No structured logging
- No distributed tracing
- Missing runbooks
- Undefined service ownership
- No rollback strategy
- No disaster recovery documentation
- Performance testing not completed
- Missing SLOs
- Insufficient documentation

Applications that fail a PRR should address identified gaps before production deployment.

---

# Platform Engineering Responsibilities

The Platform Engineering Team is responsible for:

- Maintaining PRR standards
- Reviewing production readiness
- Verifying platform compliance
- Validating observability
- Reviewing operational readiness
- Confirming security controls
- Providing deployment guidance
- Approving or rejecting production readiness based on platform standards

Application teams remain responsible for implementing and maintaining their services.

---

# High-Level PRR Workflow

```
Application Ready

↓

Production Readiness Review

↓

Architecture Review

↓

Reliability Review

↓

Security Review

↓

Observability Review

↓

Scalability Review

↓

Operational Readiness

↓

Documentation Review

↓

Ownership Verification

↓

Production Approval
```

---

# Platform Engineering Principles

Our Production Readiness Review process follows these principles:

- Production readiness is an operational decision.
- Every production service must be observable.
- Security and reliability are mandatory requirements.
- Documentation is part of the product.
- Ownership must be clearly defined.
- Operational excellence is verified before deployment.
- Platform standards are applied consistently across all services.
- Production readiness reduces operational risk and improves long-term reliability.

---

# Key Takeaways

- A Production Readiness Review evaluates whether a service is operationally prepared for production.
- PRRs assess architecture, reliability, security, observability, scalability, disaster recovery, operations, documentation, and ownership.
- Platform Engineers ensure services meet organizational standards before deployment.
- Standardized PRRs reduce production incidents and improve operational consistency.
- Documentation, monitoring, runbooks, and ownership are essential components of production readiness.
- A successful PRR demonstrates that a service can be safely deployed, monitored, supported, and maintained in production.