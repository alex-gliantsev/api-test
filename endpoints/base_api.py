import requests
import jsonschema
from jsonschema import validate
from config import BASE_URL


class BaseAPI:
    response = None
    response_json = None
    base_url = BASE_URL
    endpoint: str

    # The general status code assertion helper
    def assert_status_code(self, expected_code: int):
        actual_code = self.response.status_code
        assert actual_code == expected_code, (
            f"Assertion Failed: Expected status code {expected_code} but got {actual_code}. Response: {self.response.text}"
        )

    def assert_status_code_is_200(self):
        self.assert_status_code(200)

    def assert_status_code_is_404(self):
        self.assert_status_code(404)

    def assert_status_code_is_400(self):
        self.assert_status_code(400)

    def get_response_json(self):
        try:
            self.response_json = self.response.json()
            return self.response_json
        except requests.exceptions.JSONDecodeError:
            self.response_json = None
            return None

    def assert_respnse_json_value_is_not_none(self, key: str):
        value = self.response_json.get(key)
        assert value is not None, (
            f"Assertion Failed: Value for key '{key}' is None. Response: {self.response_json}"
        )

    def assert_response_json_value_equals(self, key: str, expected_value):
        actual_value = self.response_json.get(key)
        assert actual_value == expected_value, (
            f"Assertion Failed: Expected value for key '{key}' to be '{expected_value}', but got '{actual_value}'. Response: {self.response_json}"
        )

    def assert_response_matches_schema(self, schema: dict):
        """
        Validates the response JSON against the provided JSON schema.
        """
        assert self.response_json is not None, (
            f"Assertion Failed: Cannot validate schema, response_json is None. Status: {self.response.status_code}"
        )
        try:
            validate(instance=self.response_json, schema=schema)
        except jsonschema.exceptions.ValidationError as e:
            # Raise assertion error with details from the validation error
            assert False, (
                f"Assertion Failed: JSON response does not match schema.\nSchema: {schema}\nResponse: {self.response_json}\nValidation Error: {e.message}"
            )
        except jsonschema.exceptions.SchemaError as e:
            # This indicates an error in the schema definition itself
            assert False, (
                f"Assertion Failed: Invalid Schema provided.\nSchema: {schema}\nSchema Error: {e.message}"
            )

    def assert_item_not_found_error_message(self, item_id: str):
        """
        Asserts that the response JSON contains the correct error message.
        """
        expected_message = f"Oject with id={item_id} was not found."
        self.assert_response_json_value_equals("error", expected_message)

    def assert_item_do_not_exist_error_message(self, item_id: str, error_key: str = "error"):
        """
        Asserts that the response JSON contains the correct error message.
        """
        actual_message = self.response_json.get(error_key)
        expected_substring = f"Object with id = {item_id} doesn't exist."
        assert expected_substring in actual_message, (
            f"Assertion Failed: Expected substring '{expected_substring}' not found in error message."
            f"Actual message: '{actual_message}'. Response: {self.response_json}"
        )
        
    def assert_no_valid_fields_error_message(self):
        """
        Asserts that the response JSON contains the correct error message.
        """
        expected_message = "No valid field(s) to update have been passed as part of a request body."
        self.assert_response_json_value_equals("error", expected_message)
