def test_healthcheck(api_client):
    response = api_client.get("/health")
    assert response.status_code == 200
    assert response.json().get("status") == "ok"
