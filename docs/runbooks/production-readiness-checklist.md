# Production Readiness Checklist

## Security

- [ ] Secrets stored outside Git
- [ ] Containers run as non-root
- [ ] Privilege escalation disabled
- [ ] Read-only root filesystem
- [ ] NetworkPolicies configured

## Reliability

- [ ] Liveness probes configured
- [ ] Readiness probes configured
- [ ] Resource requests defined
- [ ] Resource limits defined
- [ ] HPA configured
- [ ] PodDisruptionBudget configured

## Operations

- [ ] Metrics exposed
- [ ] Logging centralized
- [ ] Alerts configured
- [ ] Dashboards available

## Platform

- [ ] Helm lint passes
- [ ] Helm template passes
- [ ] Documentation complete
- [ ] CI validation configured
- [ ] Semantic versioning followed