from webapp.app import app
import pytest

@pytest.fixture()
def client():
    return app.test_client()

def test_root(client):
    response = client.get("/")
    print(response.data)
    assert b"Hello" in response.data

def test_add(client):
    response = client.get("/add?a=5&b=6")
    assert b"11" in response.data

