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

addition = [
    (1,1,2),
    (1,2,3),
    (0,0,0),
    (-1,2,1),
]
@pytest.mark.parametrize("a,b,expected", addition)
def test_add_parameterized(client, a, b, expected):
    response = client.get(f"/add?a={a}&b={b}")
    assert str(expected).encode() in response.data

