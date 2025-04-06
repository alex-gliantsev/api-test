from endpoints.get import GetItem

def test_get_item_by_id(created_item):
   item_id = created_item.response_json.get("id")
   get_client = GetItem()
   get_client.get_item(item_id)

   assert get_client.status_code_is_200(), f"Expected status code 200 but got {get_client.response.status_code}"
   assert get_client.response_json.get("id") == item_id, f"Expected item ID {item_id} but got {get_client.response_json.get('id')}"