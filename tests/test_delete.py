from endpoints.delete import DeleteItem


def test_delete_item(create_item):
    item_id = create_item.response_json.get("id")
    delete_client = DeleteItem()
    delete_client.delete_item(item_id)
    assert delete_client.status_code_is_200(), (
        f"Expected status code 200 but got {delete_client.response.status_code}"
    )
