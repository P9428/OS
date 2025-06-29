from fastapi import FastAPI

app = FastAPI(title="Timeline Service")

@app.get("/health")
def health():
    return {"status": "ok"}
