import requests
from config import BASE_URL


class BaseAPI:
    response = None
    response_json = None
    base_url = BASE_URL
    endpoint: str

    # The general assertion helper
    def assert_status_code(self, expected_code: int):
        actual_code = self.response.status_code if self.response else "N/A"
        assert actual_code == expected_code, (
            f"Assertion Failed: Expected status code {expected_code} but got {actual_code}. Response: {self.response.text if self.response else 'No response'}"
        )

    def assert_status_code_is_200(self):
        self.assert_status_code(200)

    def assert_status_code_is_404(self):
        self.assert_status_code(404)

    def get_response_json(self):
        try:
            self.response_json = self.response.json()
            return self.response_json
        except requests.exceptions.JSONDecodeError:
            self.response_json = None
            return None

    def assert_response_json_has_key(self, key: str):
        assert isinstance(self.response_json, dict), (
            f"Assertion Failed: Expected JSON response to be a dictionary, but got {type(self.response_json)}. Response: {self.response_json}"
        )
        assert key in self.response_json, (
            f"Assertion Failed: Response JSON does not contain expected key '{key}'. Keys found: {list(self.response_json.keys())}. Response: {self.response_json}"
        )

    def assert_respnse_json_value_is_not_none(self, key: str):
        self.assert_response_json_has_key(key)
        value = self.response_json.get(key)
        assert value is not None, (
            f"Assertion Failed: Value for key '{key}' is None. Response: {self.response_json}"
        )

    def assert_response_json_value_equals(self, key: str, expected_value):
        self.assert_response_json_has_key(key)
        actual_value = self.response_json.get(key)
        assert actual_value == expected_value, (
            f"Assertion Failed: Expected value for key '{key}' to be '{expected_value}', but got '{actual_value}'. Response: {self.response_json}"
        )
