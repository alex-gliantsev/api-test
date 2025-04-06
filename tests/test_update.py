from endpoints.update import UpdateItem
from endpoints.get import GetItem
from utils.payload_data import ALTERNATIVE_PAYLOAD

def test_update_item(created_item):
   item_id = created_item.response_json.get("id")
   update_client = UpdateItem()
   payload = ALTERNATIVE_PAYLOAD
   update_client.update_item(item_id, payload)

   assert update_client.status_code_is_200(), f"Expected status code 200 but got {update_client.response.status_code}"
   assert update_client.response_json.get("name") == payload["name"], f"Expected name {payload['name']} but got {update_client.response_json.get('name')}"

   get_client = GetItem()
   get_client.get_item(item_id)
   assert get_client.status_code_is_200(), f"Expected status code 200 but got {get_client.response.status_code}"