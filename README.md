# Dodo Payments DevSecOps Assignment

## Overview

This repository contains my submission for the **Dodo Payments DevSecOps Assignment**, demonstrating secure application deployment, Kubernetes hardening, DevSecOps CI/CD practices, service mesh security, reconnaissance, penetration testing, and centralized logging.

The project focuses on implementing security best practices across the software delivery lifecycle—from application containerization and Kubernetes deployment to CI/CD security, runtime protection, and infrastructure observability.

---

## Objectives

- Secure a containerized Flask application
- Harden Kubernetes workloads
- Implement a secure GitHub Actions CI/CD pipeline
- Secure application communication using Istio Service Mesh
- Perform passive reconnaissance and penetration testing
- Centralize logs using Grafana Loki & Promtail

---

# Repository Structure

```text
.
├── app/                         # Flask application
├── deploy/                      # Kubernetes manifests
├── docs/
│   └── TASK2.md                 # CI/CD documentation
├── monitoring/
│   └── loki-values.yaml         # Loki Helm configuration
├── task4-recon-pentest/
│   ├── README.md
│   ├── attack-surface-report.md
│   ├── pentest-report.md
│   └── recon/
├── .github/
│   └── workflows/
├── Dockerfile
└── README.md
```

---

# Task 1 – Kubernetes Hardening

Implemented Kubernetes security best practices including:

- Non-root containers
- Read-only root filesystem
- Dropped Linux capabilities
- Security Context configuration
- Resource requests and limits
- ServiceAccount
- RBAC
- ConfigMap support
- Ingress configuration
- Health probes (Liveness & Readiness)
- Least privilege deployment

Deployment manifests are available under:

```
deploy/
```

---

# Task 2 – Secure CI/CD Pipeline

Implemented a secure GitHub Actions pipeline including:

- Docker image build
- Dependency installation
- Trivy vulnerability scanning
- Gitleaks secret scanning
- Static Application Security Testing (SAST)
- Supply-chain provenance workflow
- Security gates before build completion

Workflow files:

```
.github/workflows/
```

Documentation:

```
docs/TASK2.md
```

---

# Task 3 – Service Mesh Security

Implemented Istio security controls including:

- Istio installation
- STRICT mTLS
- Authorization Policies
- Network Policies
- Secure service-to-service communication

Deployment manifests are located under:

```
deploy/
```

---

# Task 4 – Reconnaissance & Penetration Testing

Performed security assessment of the target application.

Activities included:

### Passive Reconnaissance

- Subfinder
- Assetfinder
- Amass
- HTTPX

### Attack Surface Analysis

- Subdomain enumeration
- Live host identification
- Service discovery

### Penetration Testing

- Manual verification
- Security assessment
- Vulnerability validation
- Remediation recommendations

Reports:

```
task4-recon-pentest/
```

---

# Bonus – Centralized Logging

Implemented centralized logging using:

- Grafana Loki
- Promtail

Configuration:

```
monitoring/loki-values.yaml
```

---

# Technology Stack

- Python
- Flask
- Docker
- Kubernetes
- Istio
- GitHub Actions
- Trivy
- Gitleaks
- Grafana Loki
- Promtail

---

# Getting Started

## Prerequisites

- Docker
- Kubernetes Cluster
- kubectl
- Helm
- Istio
- Python 3.x

---

## Build Docker Image

```bash
docker build -t ledger-api .
```

---

## Deploy Application

```bash
kubectl apply -f deploy/
```

---

## Verify Deployment

```bash
kubectl get pods

kubectl get svc

kubectl get ingress
```

---

# Security Improvements

The following security controls were implemented:

- Principle of Least Privilege
- Non-root containers
- Read-only filesystem
- Secure RBAC
- Service Accounts
- Resource limits
- Secret scanning
- Vulnerability scanning
- Static code analysis
- Secure CI/CD pipeline
- Istio mTLS
- Authorization Policies
- Centralized logging

---

# Reports

| Document | Description |
|----------|-------------|
| `docs/TASK2.md` | CI/CD implementation |
| `task4-recon-pentest/attack-surface-report.md` | Attack surface assessment |
| `task4-recon-pentest/pentest-report.md` | Penetration testing report |
| `task4-recon-pentest/README.md` | Reconnaissance documentation |

---

# Future Improvements

Potential future enhancements include:

- Admission Controllers
- OPA/Gatekeeper policies
- Falco runtime security
- Prometheus monitoring
- Automated DAST
- Image signing using Cosign
- GitOps deployment using ArgoCD

---

# Author

**Kanan Bajaj**

DevOps | Cloud | Kubernetes | DevSecOps
