# Ingestion Service

Consumes data from connectors and publishes events to Kafka.

### Development

```bash
uvicorn app.main:app --reload --port 8002
```
