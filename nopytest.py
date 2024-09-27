from webapp.app import app

def test_request_example(client):
    response = client.get("/")
    assert b"Helloo" in response.data

test_request_example(app.test_client())