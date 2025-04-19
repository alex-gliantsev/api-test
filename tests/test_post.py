from endpoints.post import CreateItem

def test_create_item(item_fixture: CreateItem):
    create_client = item_fixture
    payload = create_client.payload

    create_client.assert_status_code_is_200()
    create_client.assert_response_json_has_key("id")
    create_client.assert_respnse_json_value_is_not_none("id")
    create_client.assert_response_json_has_key("createdAt")
    create_client.assert_response_json_value_equals("name", payload["name"])
    create_client.assert_response_json_value_equals("data", payload["data"])
