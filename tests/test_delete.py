import allure
from endpoints.delete import DeleteItem
from endpoints.get import GetItem
from utils.schemas import DELETE_SUCCESS_SCHEMA


@allure.title("Test Delete Item")
@allure.description("Test deleting an item and verifying the response.")
def test_delete_item(create_item):
    item_id = create_item.item_id
    delete_client = DeleteItem()
    delete_client.delete_item(item_id)

    delete_client.assert_status_code_is_200()
    delete_client.assert_response_matches_schema(DELETE_SUCCESS_SCHEMA)
    delete_client.assert_delete_success_message(item_id)


@allure.title("Test Get Deleted Item")
@allure.description(
    "Test getting an item after it has been deleted and verifying the response."
)
def test_get_deleted_item(create_item):
    item_id = create_item.item_id

    delete_client = DeleteItem()
    delete_client.delete_item(item_id)

    # Attempt to get the deleted item
    get_client = GetItem()
    get_client.get_item(item_id)

    # Assert that the item is no longer found
    get_client.assert_status_code_is_404()


@allure.title("Test Attempt To Delete A Non-Existent Item")
@allure.description(
    "Test deleting an item that does not exist and verifying the error response."
)
def test_delete_non_existent_item():
    delete_client = DeleteItem()
    item_id = "non_existent_id_12345"

    delete_client.delete_item(item_id)

    delete_client.assert_status_code_is_404()
    delete_client.assert_item_does_not_exist_error_message(item_id)
