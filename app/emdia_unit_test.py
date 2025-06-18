from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

# Instrução: Para testar as seguintes rotas, use o comando: PYTHONPATH=app pytest app/emdia_unit_test.py.
#
# Além disso, é necessário estar na pasta "MVP02-emdia/", não em "app/".

def test_home_route():
    response = client.get("/openapi.json")
    assert response.status_code == 200

def test_get_non_existent_perfil():
    response = client.get("/perfil/9999")
    assert response.status_code == 404
