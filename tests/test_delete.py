from endpoints.delete import DeleteItem


def test_delete_item(create_item):
    item_id = create_item.item_id
    delete_client = DeleteItem()
    delete_client.delete_item(item_id)

    delete_client.assert_status_code_is_200()
    delete_client.assert_response_json_has_key("message")
    delete_client.assert_delete_success_message(item_id)
