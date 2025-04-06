import requests
from endpoints.base_api import BaseAPI


class DeleteItem(BaseAPI):
    def delete_item(self, item_id, **kwargs):
        endpoint = f"objects/{item_id}"
        url = f"{BaseAPI.base_url}/{endpoint}"
        self.response = requests.delete(url, **kwargs)
        self.get_json()
        return self
