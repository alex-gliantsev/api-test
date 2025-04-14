from endpoints.get import GetItem

def test_get_item_by_id(item_fixture):
   get_client = GetItem()
   item_id = item_fixture.response_json.get("id")
   get_client.get_item(item_id)

   assert get_client.status_code_is_200(), f"Expected status code 200 but got {get_client.response.status_code}"
   assert get_client.response_json.get("id") == item_id, f"Expected ID {item_id} but got {get_client.response_json.get('id')}"
