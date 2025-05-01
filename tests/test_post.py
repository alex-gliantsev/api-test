from endpoints.post import CreateItem
from utils.schemas import POST_ITEM_SCHEMA

def test_create_item(item_fixture: CreateItem):
    create_client = item_fixture
    payload = create_client.payload

    create_client.assert_status_code_is_200()
    create_client.assert_response_matches_schema(POST_ITEM_SCHEMA)
    create_client.assert_response_json_value_equals("name", payload["name"])
    create_client.assert_response_json_value_equals("data", payload["data"])
