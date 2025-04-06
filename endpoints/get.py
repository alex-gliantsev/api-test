import requests
from endpoints.base_api import BaseAPI


class GetItem(BaseAPI):
    def get_item(self, item_id, **kwargs):
        endpoint = f"/objects/{item_id}"
        url = f"{BaseAPI.base_url}/{endpoint}".rstrip("/")
        self.response = requests.get(url, **kwargs)