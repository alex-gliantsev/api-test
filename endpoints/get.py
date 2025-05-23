import requests
from endpoints.base_api import BaseAPI

class GetItem(BaseAPI):
    
    # Retrieves an item by its ID and retrieves the response JSON.
    def get_item(self, item_id, **kwargs):
        endpoint = f"objects/{item_id}"
        url = f"{BaseAPI.base_url}/{endpoint}"
        self.response = requests.get(url, **kwargs)
        self.get_response_json()
        return self
