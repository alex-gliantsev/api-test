from endpoints.get import GetItem


def test_get_item_by_id(item_fixture):
    item_id = item_fixture.item_id
    payload = item_fixture.payload

    get_client = GetItem()
    get_client.get_item(item_id)

    get_client.assert_status_code_is_200()
    get_client.assert_response_json_has_key("id")
    get_client.assert_response_json_value_equals("id", item_id)
    get_client.assert_response_json_value_equals("name", payload["name"])
    get_client.assert_response_json_value_equals("data", payload["data"])
