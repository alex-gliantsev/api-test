import pytest
from endpoints.post import CreateItem
from endpoints.delete import DeleteItem
from utils.payload_data import DEFAULT_PAYLOAD


@pytest.fixture
def created_item():
    """
    Fixture to create an object before a test and delete it afterwards.
    Yields the ID of the created object.
    """
    # Setup: Create the object
    create_client = CreateItem()
    payload = DEFAULT_PAYLOAD
    create_client.create_item(payload)
    item_id = create_client.response_json.get("id")

    yield create_client
    # Delete the object
    delete_client = DeleteItem()
    delete_client.delete_item(item_id)


@pytest.fixture
def only_create_item():
    create_client = CreateItem()
    payload = DEFAULT_PAYLOAD
    create_client.create_item(payload)

    yield create_client
