from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_non_existent_perfil():
    response = client.get("/perfil/9999")
    assert response.status_code == 404