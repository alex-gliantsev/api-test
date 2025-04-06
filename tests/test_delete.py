from endpoints.delete import DeleteItem
from endpoints.get import GetItem


def test_delete_item(only_create_item):
    item_id = only_create_item.response_json.get("id")
    delete_client = DeleteItem()
    delete_client.delete_item(item_id)
    assert delete_client.status_code_is_200(), f"Expected status code 200 but got {delete_client.response.status_code}"
    
    get_client = GetItem()
    get_client.get_item(item_id)
    assert get_client.status_code_is_404(), f"Expected status code 404 but got {get_client.response.status_code}"