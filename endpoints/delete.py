import requests
from endpoints.base_api import BaseAPI


class DeleteItem(BaseAPI):
    def delete_item(self, item_id, **kwargs):
        endpoint = f"objects/{item_id}"
        url = f"{BaseAPI.base_url}/{endpoint}"
        self.response = requests.delete(url, **kwargs)
        self.get_response_json()
        return self
    
    def assert_delete_success_message(self, item_id: str):
        """
        Asserts that the response JSON contains the correct success message
        for deleting the specified item ID.
        """
        expected_message = f"Object with id = {item_id} has been deleted."

        # Check the value of the 'message' key
        self.assert_response_json_value_equals("message", expected_message)
