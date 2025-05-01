from endpoints.post import CreateItem
from conftest import RegisterCleanupFunc
from utils.schemas import POST_ITEM_SCHEMA
from utils.payload_data import FULL_PAYLOAD

def test_create_item(item_fixture: CreateItem):
    create_client = item_fixture
    payload = create_client.payload

    create_client.assert_status_code_is_200()
    create_client.assert_response_matches_schema(POST_ITEM_SCHEMA)
    create_client.assert_response_json_value_equals("name", payload["name"])
    create_client.assert_response_json_value_equals("data", payload["data"])
    
def test_create_item_with_full_payload(register_item_for_cleanup: RegisterCleanupFunc):
    create_client = CreateItem()
    payload = FULL_PAYLOAD
    create_client.create_item(payload)
    create_client.assert_status_code_is_200()
    create_client.assert_response_matches_schema(POST_ITEM_SCHEMA)
    create_client.assert_response_json_value_equals("name", payload["name"])
    create_client.assert_response_json_value_equals("data", payload["data"])
    
    # Delete the item after the test
    item_id = create_client.response_json.get("id")
    register_item_for_cleanup(item_id)