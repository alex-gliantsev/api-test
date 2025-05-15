import uuid

def generate_unique_id() -> str:
   """
   Generates a unique ID (UUID4) suitable for testing non-existent items.
   """
   return str(uuid.uuid4())