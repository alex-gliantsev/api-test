from endpoints.put import UpdateItem
from utils.payload_data import FULL_PAYLOAD
from utils.schemas import UPDATE_ITEM_SCHEMA, GET_ITEM_SCHEMA


def test_full_update_item(item_fixture):
    item_id = item_fixture.item_id
    update_client = UpdateItem()
    payload = FULL_PAYLOAD
    update_client.update_item(item_id, payload)

    update_client.assert_status_code_is_200()
    update_client.assert_response_matches_schema(UPDATE_ITEM_SCHEMA)
    update_client.assert_response_json_value_equals("id", item_id)
    update_client.assert_response_json_value_equals("name", payload["name"])
    update_client.assert_response_json_value_equals("data", payload["data"])
    
def test_get_updated_item(item_fixture):
    item_id = item_fixture.item_id
    update_client = UpdateItem()
    payload = FULL_PAYLOAD
    update_client.update_item(item_id, payload)

    # Get the updated item
    get_client = UpdateItem()
    get_client.get_item(item_id)

    # Assert that the item is updated correctly
    get_client.assert_status_code_is_200()
    get_client.assert_response_matches_schema(GET_ITEM_SCHEMA)
    get_client.assert_response_json_value_equals("id", item_id)
    get_client.assert_response_json_value_equals("name", payload["name"])
    get_client.assert_response_json_value_equals("data", payload["data"])

def test_uupdate_non_existent_item():
    update_client = UpdateItem()
    item_id = "non_existent_id_12345"
    payload = FULL_PAYLOAD

    update_client.update_item(item_id, payload)

    update_client.assert_status_code_is_404()
    update_client.assert_item_not_found_error_message(item_id)