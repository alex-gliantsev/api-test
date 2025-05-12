import requests
from endpoints.base_api import BaseAPI

class CreateItem(BaseAPI):
    
    # Creates a new item with the provided payload and retrieves the response JSON.
    def create_item(self, payload, **kwargs):
        endpoint = "objects"
        url = f"{BaseAPI.base_url}/{endpoint}"
        self.response = requests.post(url, json=payload, **kwargs)
        self.get_response_json()
        return self
