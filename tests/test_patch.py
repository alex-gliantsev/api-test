from endpoints.patch import PartiallyUpdateItem
from endpoints.get import GetItem
from utils.payload_data import UPDATE_NAME
from utils.schemas import UPDATE_ITEM_SCHEMA


def test_partial_update_item(item_fixture):
    item_id = item_fixture.item_id
    update_client = PartiallyUpdateItem()
    payload = UPDATE_NAME
    update_client.update_item(item_id, payload)

    update_client.assert_status_code_is_200()
    update_client.assert_response_matches_schema(UPDATE_ITEM_SCHEMA)
    update_client.assert_response_json_value_equals("id", item_id)
    update_client.assert_response_json_value_equals("name", payload["name"])
    
def test_verify_unchanged_fields(item_fixture):
    item_id = item_fixture.item_id
    update_client = PartiallyUpdateItem()
    get_client = GetItem()
    get_client.get_item(item_id)
    original_data = get_client.response_json
    update_payload = UPDATE_NAME

    update_client.update_item(item_id, update_payload)
    updated_data = update_client.response_json
    
    assert updated_data.get("name") == update_payload.get("name")
    assert updated_data.get("data") == original_data.get("data")
    assert updated_data.get("id") == original_data.get("id")