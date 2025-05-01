from endpoints.delete import DeleteItem
from endpoints.get import GetItem
from utils.schemas import DELETE_SUCCESS_SCHEMA


def test_delete_item(create_item):
    item_id = create_item.item_id
    delete_client = DeleteItem()
    delete_client.delete_item(item_id)

    delete_client.assert_status_code_is_200()
    delete_client.assert_response_matches_schema(DELETE_SUCCESS_SCHEMA)
    delete_client.assert_delete_success_message(item_id)


def test_get_deleted_item(create_item):
    item_id = create_item.item_id

    delete_client = DeleteItem()
    delete_client.delete_item(item_id)

    # Attempt to get the deleted item
    get_client = GetItem()
    get_client.get_item(item_id)

    # Assert that the item is no longer found
    get_client.assert_status_code_is_404()


def test_delete_non_existent_item():
    delete_client = DeleteItem()
    item_id = "non_existent_id_12345"

    delete_client.delete_item(item_id)

    delete_client.assert_status_code_is_404()
    delete_client.assert_item_do_not_exist_error_message(item_id)
