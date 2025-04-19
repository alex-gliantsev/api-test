import requests
from endpoints.base_api import BaseAPI


class CreateItem(BaseAPI):
    endpoint = "objects"

    def create_item(self, payload, **kwargs):
        url = f"{BaseAPI.base_url}/{self.endpoint}"
        self.response = requests.post(url, json=payload, **kwargs)
        self.get_response_json()
        return self

    def check_name(self, name):
        return self.response_json.get("name") == name
