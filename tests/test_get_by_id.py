import allure
from endpoints.get import GetItem
from utils.schemas import GET_ITEM_SCHEMA
from utils.id_generator import generate_unique_id

@allure.title("Test Get Item By ID")
@allure.description("Test getting an item by its ID and verifying the response.")
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

@allure.title("Test Get Item By Non-Existent ID")
@allure.description("Test getting an item by a non-existent ID and verifying the error response.")
def test_get_item_by_non_existent_id():
    get_client = GetItem()
    item_id = generate_unique_id()

    get_client.get_item(item_id)

    get_client.assert_status_code_is_404()
    get_client.assert_item_not_found_error(item_id=item_id)
