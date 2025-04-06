from endpoints.delete import DeleteItem
from endpoints.post import CreateItem
from endpoints.get import GetItem
from utils.query_factory import QueryPayload


def test_delete_item():
    create_client = CreateItem()
    delete_client = DeleteItem()
    get_client = GetItem()
    payload = QueryPayload.create_laptop_payload()
    print(payload)
    # Call the create_item method with the sample payload
    response = create_client.create_item(payload)
    response_json = create_client.response_json
    item_id = response_json.get("id")
    response = delete_client.delete_item(item_id)

    # Check if the item was deleted successfully
    response = get_client.get_item(item_id)