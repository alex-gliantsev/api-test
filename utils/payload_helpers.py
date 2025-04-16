
import copy
from .payload_data import DEFAULT_PAYLOAD


def generate_payload(**overrides) -> dict:
    payload = copy.deepcopy(DEFAULT_PAYLOAD)

    # Override 'name' if provided
    if "name" in overrides:
        payload["name"] = overrides.pop("name")

    # Update the 'data' sub-dictionary if 'data' override is provided as a dict
    if "data" in overrides and isinstance(overrides.get("data"), dict):
        data_overrides = overrides.pop("data")  # pop it
        payload["data"].update(data_overrides)

    payload.update(overrides)

    return payload
