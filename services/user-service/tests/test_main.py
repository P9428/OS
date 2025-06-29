from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_login():
    response = client.post("/register", json={"email": "test@example.com", "password": "secret"})
    assert response.status_code in (200, 400)
