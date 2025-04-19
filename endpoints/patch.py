import requests
from endpoints.base_api import BaseAPI


class PartiallyUpdateItem(BaseAPI):
    def update_item(self, item_id, payload, **kwargs):
        endpoint = f"/objects/{item_id}"
        url = f"{BaseAPI.base_url}/{endpoint}".rstrip("/")
        self.response = requests.patch(url, json=payload, **kwargs)
        self.response_json = self.response.json()
        self.get_response_json()
        return self
