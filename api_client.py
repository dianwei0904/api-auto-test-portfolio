import requests


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def _url(self, path: str) -> str:
        if path.startswith("/"):
            return f"{self.base_url}{path}"
        return f"{self.base_url}/{path}"

    def get(self, path: str, **kwargs):
        return self.session.get(self._url(path), **kwargs)

    def post(self, path: str, json=None, **kwargs):
        return self.session.post(self._url(path), json=json, **kwargs)

    def put(self, path: str, json=None, **kwargs):
        return self.session.put(self._url(path), json=json, **kwargs)

    def delete(self, path: str, **kwargs):
        return self.session.delete(self._url(path), **kwargs)