import requests
from endpoints.base_api import BaseAPI

class UpdateItem(BaseAPI):
    
    # Updates an item by its ID with the provided payload and retrieves the response JSON.
    def update_item(self, item_id, payload, **kwargs):
        endpoint = f"objects/{item_id}"
        url = f"{BaseAPI.base_url}/{endpoint}"
        self.response = requests.put(url, json=payload, **kwargs)
        self.get_response_json()
        return self