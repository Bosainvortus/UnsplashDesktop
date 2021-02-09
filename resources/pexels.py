import requests


class API:
    def __init__(self, api_key):
        self._api_key = api_key
        self._base_url = "https://api.pexels.com/v1/"

    def _get_headers(self):
        headers = {}

        if self._api_key:
            headers["Authorization"] = self._api_key

        return headers

    def _request(self, endpoint, params={}):
        url = f"{self._base_url}{endpoint}"
        headers = self._get_headers()
        response = requests.request("GET", url, params=params, headers=headers)
        return response.json()

    def get_photos(
        self,
        query,
        orientation="landscape",
        size="large",
        color=None,
        locale="en-US",
        per_page="15",
        page="1",
    ):
        params = {
            "query": query,
            "orientation": orientation,
            "size": size,
            "color": None,
            "locale": locale,
            "page": page,
        }
        return self._request("search", params)
