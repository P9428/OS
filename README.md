# Symphony Orchestration Operating System

This repository contains scaffolding for Symphony, a microservices-based orchestration platform for music professionals.

## Services

- **api-gateway** – entrypoint routing requests to backend services
- **user-service** – user authentication APIs
- **connector-service** – manages third-party OAuth integrations
- **ingestion-service** – ingests data and publishes events
- **timeline-service** – aggregates events for the frontend

## Kubernetes

Kubernetes manifests for each service are located in the `k8s/` directory.
