# Grafana Architecture

## Purpose

This document describes how Grafana is used within the Platform Engineering observability platform.

Grafana provides a centralized interface for visualizing metrics, logs, and traces collected from Kubernetes clusters and cloud-native applications. It enables Platform Engineers, developers, Site Reliability Engineers (SREs), and engineering leadership to understand platform health through dashboards and real-time operational insights.

Our platform manages Grafana as code using Git, allowing dashboards, data sources, and provisioning configuration to be version-controlled alongside the rest of the platform.

---

# What is Grafana?

Grafana is an open-source visualization and observability platform.

Unlike Prometheus, Grafana does not collect or store monitoring data. Instead, it connects to one or more data sources and presents the information through dashboards.

Grafana allows engineers to:

- Visualize metrics
- Search logs
- Explore traces
- Build dashboards
- Configure alerts
- Investigate production incidents

Grafana acts as the primary user interface for the observability platform.

---

# Data Sources

A data source tells Grafana where to retrieve telemetry data.

Our platform primarily uses the following data sources:

| Data Source | Purpose |
|-------------|---------|
| Prometheus | Metrics |
| Loki | Logs |
| Tempo / Jaeger | Distributed Traces |
| Azure Monitor | Azure resources |
| Elasticsearch (optional) | Search and analytics |

Example:

```
Grafana

├── Prometheus

├── Loki

├── Tempo

└── Azure Monitor
```

Grafana queries these systems in real time to build dashboards.

---

# Dashboard Hierarchy

Different teams require different levels of information.

Our dashboards are organized by audience.

## Executive Dashboards

Audience:

- Engineering Leadership
- CTO
- Engineering Managers

Focus:

- Platform Availability
- Deployment Success Rate
- Incident Count
- Overall Health
- Service Availability

These dashboards avoid technical implementation details.

---

## Platform Dashboards

Audience:

- Platform Engineers
- SRE Team

Focus:

- Kubernetes Cluster Health
- Node Health
- Namespace Health
- Resource Utilization
- Platform Capacity
- Failed Deployments

These dashboards support day-to-day platform operations.

---

## Application Dashboards

Audience:

- Development Teams

Focus:

- Request Rate
- Request Latency
- Error Rate
- Replica Count
- Rollout Status
- Resource Usage

Each application should have a standardized dashboard template.

---

## Infrastructure Dashboards

Audience:

- Infrastructure Engineers

Focus:

- CPU Utilization
- Memory Usage
- Disk Usage
- Network Traffic
- Filesystem Health
- Node Availability

Infrastructure dashboards focus on Kubernetes worker nodes rather than applications.

---

# Dashboard Design Principles

A well-designed dashboard should answer a specific operational question.

Examples:

- Is the cluster healthy?
- Is the application responding?
- Which deployment introduced errors?
- Which namespace is consuming the most resources?

Our Platform Team follows these principles:

- Keep dashboards simple.
- Show the most important information first.
- Avoid unnecessary visualizations.
- Use consistent layouts.
- Standardize colors and terminology.
- Prefer reusable dashboard templates.
- Design dashboards around operational workflows.

Dashboards should reduce cognitive load rather than increase it.

---

# Golden Signals

Google's Site Reliability Engineering practices identify four key application metrics known as the **Golden Signals**.

## 1. Latency

Measures how long requests take to complete.

Example:

```
Average Response Time

95th Percentile

99th Percentile
```

---

## 2. Traffic

Measures application workload.

Examples:

- Requests per second
- Transactions per minute
- Active users

---

## 3. Errors

Measures request failures.

Examples:

- HTTP 5xx responses
- Failed requests
- Application exceptions

---

## 4. Saturation

Measures how close the system is to capacity.

Examples:

- CPU Utilization
- Memory Usage
- Thread Pool Usage
- Database Connections

Together these four metrics provide an excellent overview of application health.

---

# RED Method

The RED Method is commonly used for APIs and microservices.

RED stands for:

- **Rate** – Requests processed per second
- **Errors** – Failed requests
- **Duration** – Request latency

Example dashboard:

```
Payment API

------------------------

Request Rate

Error Rate

Request Duration
```

The RED Method is recommended for application-level dashboards.

---

# USE Method

The USE Method is commonly used for infrastructure monitoring.

USE stands for:

- **Utilization**
- **Saturation**
- **Errors**

Examples include:

CPU

- Utilization
- Saturation
- Hardware Errors

Memory

- Utilization
- Saturation
- Allocation Failures

Storage

- Utilization
- I/O Saturation
- Disk Errors

The USE Method is recommended for node and infrastructure dashboards.

---

# Dashboard as Code

Our platform manages Grafana dashboards using Git.

Rather than manually creating dashboards through the web interface, dashboards are exported as JSON files and stored within the repository.

Example:

```
monitoring/

grafana/

dashboards/

├── platform-overview.json

├── cluster-health.json

├── application-overview.json

├── payment-api.json
```

Benefits include:

- Version control
- Peer review
- Repeatable deployments
- Environment consistency
- Disaster recovery

Dashboards become part of the platform's Infrastructure as Code strategy.

---

# Grafana Provisioning

Grafana supports automatic provisioning of dashboards and data sources.

Instead of manually configuring Grafana after installation, configuration files are stored in Git.

Provisioning automatically creates:

- Data Sources
- Dashboard Folders
- Dashboards
- Alert Rules

Workflow:

```
Git Repository

↓

Grafana Provisioning

↓

Dashboards Created

↓

Ready for Engineers
```

This ensures every environment contains identical dashboard configurations.

---

# High-Level Architecture

```
                  Kubernetes Cluster

                          │

      ┌───────────────────┼───────────────────┐

      ▼                   ▼                   ▼

 Metrics              Logs               Traces

      │                   │                   │

      ▼                   ▼                   ▼

 Prometheus           Loki              Tempo

      └───────────────────┼───────────────────┘

                          ▼

                      Grafana

                          │

        ┌─────────────────┼─────────────────┐

        ▼                 ▼                 ▼

 Platform Team      Developers         Executives

                          │

                          ▼

             Dashboards • Alerts • Analysis
```

Grafana serves as the unified visualization layer for the platform's observability stack.

---

# Platform Engineering Principles

Our Grafana platform follows these principles:

- Dashboards are managed as code.
- Dashboards should answer operational questions.
- Platform dashboards are standardized.
- Data sources are centrally managed.
- Dashboard provisioning is automated.
- Engineers should not manually recreate dashboards.
- Visualization should reduce operational complexity.
- Grafana integrates seamlessly with GitOps and the observability platform.

---

# Key Takeaways

- Grafana is the visualization layer of the observability platform.
- Grafana retrieves telemetry from systems such as Prometheus, Loki, and Tempo.
- Dashboards should be organized around operational responsibilities.
- The Golden Signals provide a standard approach to application monitoring.
- RED is recommended for application dashboards.
- USE is recommended for infrastructure dashboards.
- Dashboards should be managed as code using Git.
- Automatic provisioning ensures consistent dashboard deployment across all environments.
- Grafana enables Platform Engineers to understand platform health through centralized, real-time visualization.