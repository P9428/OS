from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_status():
    resp = client.get('/status')
    assert resp.status_code == 200
    assert resp.json() == {'status': 'ok'}
