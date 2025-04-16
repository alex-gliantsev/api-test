
def test_create_item(item_fixture):
   create_client = item_fixture
   assert create_client.status_code_is_200(), f"Expected status code 200 but got {create_client.response.status_code}"