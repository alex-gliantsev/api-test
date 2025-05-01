from endpoints.get import GetItem
from utils.schemas import GET_ITEM_SCHEMA


def test_get_item_by_id(item_fixture):
    item_id = item_fixture.item_id
    payload = item_fixture.payload

    get_client = GetItem()
    get_client.get_item(item_id)

    get_client.assert_status_code_is_200()
    get_client.assert_response_matches_schema(GET_ITEM_SCHEMA)
    get_client.assert_response_json_value_equals("id", item_id)
    get_client.assert_response_json_value_equals("name", payload["name"])
    get_client.assert_response_json_value_equals("data", payload["data"])


def test_get_item_by_non_existent_id():
    get_client = GetItem()
    item_id = "non_existent_id_12345"

    get_client.get_item(item_id)

    get_client.assert_status_code_is_404()
    get_client.assert_item_not_found_error_message(item_id)
