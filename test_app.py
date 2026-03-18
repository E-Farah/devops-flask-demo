from app import app


def test_add_numbers_success():
    # Test valid number inputs using Flask test client
    client = app.test_client()

    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.get_json() == {"result": 5}

    response = client.get("/add?a=-1&b=1")
    assert response.status_code == 200
    assert response.get_json() == {"result": 0}


def test_add_numbers_error():
    # Test invalid input
    client = app.test_client()

    response = client.get("/add?a=hello&b=3")
    assert response.status_code == 400
    assert "error" in response.get_json()
