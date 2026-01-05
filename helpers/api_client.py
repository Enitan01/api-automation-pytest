import requests
from config.settings import BASE_URL

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL

    def get(self, endpoint, **kwargs):
        return requests.get(f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint, payload=None, **kwargs):
        return requests.post(f"{self.base_url}{endpoint}", json=payload, **kwargs)
