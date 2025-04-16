from endpoints.put import UpdateItem
from utils.payload_data import FULL_PAYLOAD


def test_full_update_item(item_fixture):
    item_id = item_fixture.item_id
    update_client = UpdateItem()
    payload = FULL_PAYLOAD
    update_client.update_item(item_id, payload)

    assert update_client.status_code_is_200(), (
        f"Expected status code 200 but got {update_client.response.status_code}"
    )
    assert update_client.response_json.get("name") == payload["name"], (
        f"Expected name {payload['name']} but got {update_client.response_json.get('name')}"
    )
