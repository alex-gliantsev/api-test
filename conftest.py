import pytest
from endpoints.post import CreateItem
from endpoints.delete import DeleteItem
from utils.payload_data import DEFAULT_PAYLOAD
from utils.payload_helpers import generate_payload


@pytest.fixture
def item_fixture():
    create_client = CreateItem()
    payload = generate_payload()
    create_client.create_item(payload)
    item_id = create_client.response_json.get("id")

    yield create_client

    delete_client = DeleteItem()
    delete_client.delete_item(item_id)


@pytest.fixture
def create_item():
    create_client = CreateItem()
    payload = generate_payload()
    create_client.create_item(payload)

    yield create_client
