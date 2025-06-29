from fastapi import FastAPI

app = FastAPI(title="Connector Service")

@app.get("/health")
def health():
    return {"status": "ok"}
