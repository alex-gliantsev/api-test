from endpoints.post import CreateItem
from utils.query_factory import QueryPayload


def test_create_item():
    new_item = CreateItem()
    payload = QueryPayload.create_laptop_payload()
    print(payload)

    # Call the create_item method with the sample payload
    new_item.create_item(payload)
    print(new_item.response_json)

    assert new_item.status_code_is_200()
    assert new_item.check_name(payload["name"])
