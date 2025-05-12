import pytest
from typing import Callable
from endpoints.post import CreateItem
from endpoints.delete import DeleteItem
from utils.payload_helpers import generate_payload

@pytest.fixture
def item_fixture() -> CreateItem:
    """
    Fixture to create an item before a test and delete it after the test.

    This fixture creates an item using the CreateItem client and generates a payload.
    The created item's ID and payload are stored in the client for use during the test.
    After the test, the item is automatically deleted using the DeleteItem client.

    Return:
        CreateItem: The client instance with the created item's details.
    """
    create_client = CreateItem()
    payload = generate_payload()
    create_client.create_item(payload)
    item_id = create_client.response_json.get("id")
    create_client.item_id = item_id
    create_client.payload = payload

    yield create_client

    delete_client = DeleteItem()
    delete_client.delete_item(item_id)

@pytest.fixture
def create_item():
    """
    Fixture to create an item before a test.

    This fixture uses the CreateItem client to generate a payload and create an item.
    The created item's ID and payload are stored in the client for use during the test.

    Yields:
        CreateItem: The client instance with the created item's details.
    """
    create_client = CreateItem()
    payload = generate_payload()
    create_client.create_item(payload)
    item_id = create_client.response_json.get("id")
    create_client.item_id = item_id
    create_client.payload = payload

    yield create_client

RegisterCleanupFunc = Callable[[str], None]

@pytest.fixture(scope="function")
def register_item_for_cleanup() -> RegisterCleanupFunc:
    """
    Provides a function to register an item ID created during a test
    for automatic deletion afterwards.
    """
    # List to store IDs within this fixture's execution for this test
    item_ids_to_delete = []

    # Define the function that the test will call
    def register(item_id: str):
        """Registers an item ID to be deleted after the test."""
        if item_id:
            item_ids_to_delete.append(item_id)

    yield register

    # --- Teardown Phase (runs after the test finishes) ---
    if not item_ids_to_delete:
        return # Nothing to do

    # Delete all registered items
    delete_client = DeleteItem()
    for item_id in item_ids_to_delete:
        delete_client.delete_item(item_id)