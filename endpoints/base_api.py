class BaseAPI:
    response = None
    response_json = None
    base_url = "https://api.restful-api.dev"
    endpoint: str

    def status_code_is_200(self):
        return self.response.status_code == 200, (
            f"Expected status code 200 but got {self.response.status_code}"
        )
