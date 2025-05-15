import requests
import jsonschema
from jsonschema import validate
from config import BASE_URL

class BaseAPI:
    response = None
    response_json = None
    base_url = BASE_URL
    endpoint: str

    # Asserts that the response status code matches the expected code.
    def assert_status_code(self, expected_code: int):
        actual_code = self.response.status_code
        assert actual_code == expected_code, (
            f"Assertion Failed: Expected status code {expected_code} but got {actual_code}. Response: {self.response.text}"
        )

    # Asserts that the response status code is 200 (OK).
    def assert_status_code_is_200(self):
        self.assert_status_code(200)

    # Asserts that the response status code is 404 (Not Found).
    def assert_status_code_is_404(self):
        self.assert_status_code(404)

    # Asserts that the response status code is 400 (Bad Request).
    def assert_status_code_is_400(self):
        self.assert_status_code(400)

    def get_response_json(self):
        """
        Attempts to parse the response content as JSON and store it in self.response_json.
        """
        try:
            self.response_json = self.response.json()
            return self.response_json
        except requests.exceptions.JSONDecodeError:
            self.response_json = None
            return None

    def assert_response_json_value_is_not_none(self, key: str):
        """
        Asserts that the value for the given key in the response JSON is not None.
        """
        value = self.response_json.get(key)
        assert value is not None, (
            f"Assertion Failed: Value for key '{key}' is None. Response: {self.response_json}"
        )

    def assert_response_json_value_equals(self, key: str, expected_value):
        """
        Asserts that the value for the given key in the response JSON equals the expected value.
        """
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
        
    def assert_response_message_contains_keywords(self, error_field_key: str, keywords: list[str], item_id: str = None):
        """
        Checks if the message in 'error_field_key' contains all specified keywords and optionally the item_id.
        Case-insensitive.
        """
        message = self.response_json.get(error_field_key)
        assert message is not None, f"Key '{error_field_key}' not in response: {self.response_json}"

        message_lower = message.lower()
        if item_id:
            assert item_id.lower() in message_lower, \
                f"Expected ID '{item_id}' not in message: '{message}'"
        for kw in keywords:
            assert kw.lower() in message_lower, \
                f"Expected keyword '{kw}' not in message: '{message}'"
        return self

    def assert_item_not_found_error(self, item_id: str, error_key: str = "error"):
        """Asserts that the error message indicates item not found with its ID."""
        self.assert_response_message_contains_keywords(
            error_field_key=error_key,
            keywords=["object", "not found"],
            item_id=item_id
        )
        return self

    def assert_item_does_not_exist_error(self, item_id: str, error_key: str = "error"):
        """Asserts that the error message indicates item doesn't exist with its ID."""
        self.assert_response_message_contains_keywords(
            error_field_key=error_key,
            keywords=["object", "doesn't exist"],
            item_id=item_id
        )
        return self

    def assert_no_valid_fields_error(self, error_key: str = "error"):
        """Asserts error for no valid fields, checking message keywords."""
        self.assert_response_message_contains_keywords(
            error_field_key=error_key,
            keywords=["no valid field", "update"]
        )
        return self
