def test_get_users(api_client):
    response = api_client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
