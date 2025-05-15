import allure
from endpoints.patch import PartiallyUpdateItem
from endpoints.get import GetItem
from utils.payload_data import UPDATE_NAME, UPDATE_DATA
from utils.schemas import UPDATE_ITEM_SCHEMA, GET_ITEM_SCHEMA
from utils.id_generator import generate_unique_id


@allure.title("Test Update Item Name")
@allure.description("Test updating an item's name and verifying the response.")
def test_update_item_name(item_fixture):
    item_id = item_fixture.item_id
    update_client = PartiallyUpdateItem()
    payload = UPDATE_NAME
    update_client.update_item(item_id, payload)

    update_client.assert_status_code_is_200()
    update_client.assert_response_matches_schema(UPDATE_ITEM_SCHEMA)
    update_client.assert_response_json_value_equals("id", item_id)
    update_client.assert_response_json_value_equals("name", payload["name"])


@allure.title("Test Verify Unchanged Fields After Update Name")
@allure.description("Test verifying unchanged fields after updating an item's name.")
def test_verify_unchanged_fields_after_update_name(item_fixture):
    item_id = item_fixture.item_id
    update_client = PartiallyUpdateItem()
    get_client = GetItem()
    get_client.get_item(item_id)
    original_data = get_client.response_json
    update_payload = UPDATE_NAME

    update_client.update_item(item_id, update_payload)
    updated_data = update_client.response_json

    assert updated_data.get("data") == original_data.get("data")
    assert updated_data.get("id") == original_data.get("id")


@allure.title("Test Update Item Data")
@allure.description("Test updating an item's data and verifying the response.")
def test_update_item_data(item_fixture):
    item_id = item_fixture.item_id
    update_client = PartiallyUpdateItem()
    payload = UPDATE_DATA
    update_client.update_item(item_id, payload)

    update_client.assert_status_code_is_200()
    update_client.assert_response_matches_schema(UPDATE_ITEM_SCHEMA)
    update_client.assert_response_json_value_equals("data", payload["data"])


@allure.title("Test Verify Unchanged Fields After Update Data")
@allure.description("Test verifying unchanged fields after updating an item's data.")
def test_verify_unchanged_fields_after_update_data(item_fixture):
    item_id = item_fixture.item_id
    update_client = PartiallyUpdateItem()
    get_client = GetItem()
    get_client.get_item(item_id)
    original_response = get_client.response_json
    update_payload = UPDATE_DATA

    update_client.update_item(item_id, update_payload)
    updated_response = update_client.response_json

    assert updated_response.get("name") == original_response.get("name")
    assert updated_response.get("id") == original_response.get("id")


@allure.title("Test Get Updated Item After Patch")
@allure.description(
    "Test getting an item after it has been partially updated and verifying the response."
)
def test_get_updated_item_after_patch(item_fixture):
    item_id = item_fixture.item_id
    original_payload = item_fixture.payload
    update_client = PartiallyUpdateItem()
    payload = UPDATE_NAME
    update_client.update_item(item_id, payload)

    # Get the updated item
    get_client = GetItem()
    get_client.get_item(item_id)

    # Assert that the item is updated correctly
    get_client.assert_status_code_is_200()
    get_client.assert_response_matches_schema(GET_ITEM_SCHEMA)
    get_client.assert_response_json_value_equals("id", item_id)
    get_client.assert_response_json_value_equals("name", payload["name"])
    get_client.assert_response_json_value_equals("data", original_payload["data"])


@allure.title("Test Attempt To Update A Non-Existent Item")
@allure.description(
    "Test updating an item that does not exist and verifying the error response."
)
def test_update_non_existent_item():
    update_client = PartiallyUpdateItem()
    item_id = generate_unique_id()
    payload = UPDATE_NAME

    update_client.update_item(item_id, payload)

    update_client.assert_status_code_is_404()
    update_client.assert_item_does_not_exist_error(item_id=item_id)


@allure.title("Test Update Item With Empty Payload")
@allure.description(
    "Test updating an item with an empty payload and verifying the error response."
)
def test_update_item_with_empty_payload(item_fixture):
    item_id = item_fixture.item_id
    update_client = PartiallyUpdateItem()
    payload = {}

    update_client.update_item(item_id, payload)

    update_client.assert_status_code_is_404()
    update_client.assert_no_valid_fields_error()
