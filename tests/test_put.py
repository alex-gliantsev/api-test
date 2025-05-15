import allure
from endpoints.put import UpdateItem
from endpoints.get import GetItem
from utils.payload_data import FULL_PAYLOAD
from utils.schemas import UPDATE_ITEM_SCHEMA, GET_ITEM_SCHEMA
from utils.id_generator import generate_unique_id


@allure.title("Test Full Update Item")
@allure.description("Test fully updating an item and verifying the response.")
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


@allure.title("Test Verify Unchanged Fields After Full Update")
@allure.description(
    "Test updating an item and verifying that unchanged fields remain the same."
)
def test_get_updated_item_after_put(item_fixture):
    item_id = item_fixture.item_id
    update_client = UpdateItem()
    payload = FULL_PAYLOAD
    update_client.update_item(item_id, payload)

    # Get the updated item
    get_client = GetItem()
    get_client.get_item(item_id)

    # Assert that the item is updated correctly
    get_client.assert_status_code_is_200()
    get_client.assert_response_matches_schema(GET_ITEM_SCHEMA)
    get_client.assert_response_json_value_equals("id", item_id)
    get_client.assert_response_json_value_equals("name", payload["name"])
    get_client.assert_response_json_value_equals("data", payload["data"])


@allure.title("Test Attempt to Update a Non-Existent Item")
def test_update_non_existent_item():
    update_client = UpdateItem()
    item_id = generate_unique_id()
    payload = FULL_PAYLOAD

    update_client.update_item(item_id, payload)

    update_client.assert_status_code_is_404()
    update_client.assert_item_does_not_exist_error(item_id=item_id)
