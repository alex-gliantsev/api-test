import requests
from endpoints.base_api import BaseAPI


class PartiallyUpdateItem(BaseAPI):
    
    # Partially updates an item by its ID with the provided payload and retrieves the response JSON.
    def update_item(self, item_id, payload, **kwargs):
        endpoint = f"objects/{item_id}"
        url = f"{BaseAPI.base_url}/{endpoint}"
        self.response = requests.patch(url, json=payload, **kwargs)
        self.response_json = self.response.json()
        self.get_response_json()
        return self
