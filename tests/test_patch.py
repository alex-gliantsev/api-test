from endpoints.patch import PartiallyUpdateItem
from utils.payload_data import UPDATE_NAME


def test_full_update_item(item_fixture):
    item_id = item_fixture.item_id
    update_client = PartiallyUpdateItem()
    payload = UPDATE_NAME
    update_client.update_item(item_id, payload)

    update_client.assert_status_code_is_200()
    update_client.assert_response_json_has_key("id")
    update_client.assert_response_json_value_equals("id", item_id)
    update_client.assert_response_json_has_key("updatedAt")
    update_client.assert_response_json_value_equals("name", payload["name"])
