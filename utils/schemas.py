# Base schema for successful item responses (GET, POST, PUT, PATCH)
# Defines structure, required fields, and types
BASE_ITEM_SCHEMA = {
   "type": "object",
   "properties": {
      "id": {"type": "string"},
      "name": {"type": "string"},
      "createdAt": {"type": "string", "format": "date-time"},
      "updatedAt": {"type": "string", "format": "date-time"},
      "data": {
         "type": ["object", "null"],
         "properties": {
               "year": {"type": "integer"},
               "price": {"type": "number"},
               "CPU model": {"type": "string"},
               "Hard disk size": {"type": "string"},
               "color": {"type": "string"}
         }
      }
   },
   # List required top-level fields
   "required": ["id", "name"]
}

# Specific schema for POST
POST_ITEM_SCHEMA = BASE_ITEM_SCHEMA.copy()
POST_ITEM_SCHEMA["required"] = ["id", "name", "createdAt"]

# Specific schema for PUT/PATCH
UPDATE_ITEM_SCHEMA = BASE_ITEM_SCHEMA.copy()
UPDATE_ITEM_SCHEMA["required"] = ["id", "name", "updatedAt"]

# Specific schema for GET
GET_ITEM_SCHEMA = BASE_ITEM_SCHEMA.copy()
GET_ITEM_SCHEMA["required"] = ["id", "name"]

# Schema for successful DELETE response
DELETE_SUCCESS_SCHEMA = {
    "type": "object",
    "properties": {
        "message": {"type": "string"}
    },
    "required": ["message"],
    "additionalProperties": False
}