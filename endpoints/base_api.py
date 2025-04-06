import requests
from config import BASE_URL

class BaseAPI:
    response = None
    response_json = None
    base_url = BASE_URL
    endpoint: str

    def status_code_is(self, expected_code: int) -> bool:
        """Returns True if the response status code matches the expected code, False otherwise."""
        if self.response is None:
            return False
        return self.response.status_code == expected_code

    def status_code_is_200(self) -> bool:
        """Returns True if the response status code is 200, False otherwise."""
        return self.status_code_is(200)

    def status_code_is_404(self) -> bool:
        """Returns True if the response status code is 404, False otherwise."""
        return self.status_code_is(404)

    def get_json(self):
        try:
            self.response_json = self.response.json()
            return self.response_json
        except requests.exceptions.JSONDecodeError:
            self.response_json = None
            return None