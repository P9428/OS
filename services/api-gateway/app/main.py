from fastapi import FastAPI

app = FastAPI(title="Symphony API Gateway")

@app.get("/status")
def status():
    return {"status": "ok"}
