
def test_create_item(created_item):
   print(created_item.response_json)
   assert created_item.status_code_is_200(), f"Expected status code 200 but got {created_item.response.status_code}"