# Task 2 – Secure CI/CD Pipeline

## Overview

A GitHub Actions workflow was implemented to automate the build, security validation, and publication of the application container image.

The pipeline follows a security-first approach by validating the source code before publishing any container image.

## Pipeline Flow

```
Checkout Repository
        ↓
Setup Python
        ↓
Install Dependencies
        ↓
Gitleaks Secret Scan
        ↓
Semgrep SAST Scan
        ↓
Docker Build
        ↓
Push Image to GitHub Container Registry
        ↓
Trivy Container Scan
        ↓
Cosign Image Signing
```

## Security Controls

### Gitleaks

- Detects hardcoded secrets committed to the repository.
- Prevents accidental credential leakage.

### Semgrep

- Performs static application security testing (SAST).
- Detects insecure coding patterns based on OWASP rules.

### Trivy

- Scans the built container image for known vulnerabilities.
- The workflow fails if High or Critical vulnerabilities are detected.

### Cosign

- Signs the published container image.
- Provides image authenticity and integrity verification.

## Container Registry

The application image is published to GitHub Container Registry:

```
ghcr.io/kanan06/dodo-payments-api-assignment
```

Images are tagged with:

- latest
- Git commit SHA

## Security Improvements

Compared to a basic CI pipeline, this implementation adds:

- Secret scanning
- Static code analysis
- Container vulnerability scanning
- Container image signing
- Automated container publishing

## Outcome

The pipeline ensures that only security-validated and signed container images are published, improving the integrity and security of the software delivery process.
