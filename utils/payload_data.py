
# Default data block for a standard laptop
DEFAULT_DATA = {
   "year": 2023,
   "price": 1849.99,
   "CPU model": "Intel Core i9",
   "Hard disk size": "1 TB"
}

# Default full payload structure
DEFAULT_PAYLOAD = {
   "name": "Apple MacBook Pro 16",
   "data": DEFAULT_DATA
}

# Example of another complete payload for parameterization
ALTERNATIVE_PAYLOAD = {
    "name": "Huawei MateBook X Pro",
    "data": {
       "year": 2024,
       "price": 1799.00,
       "CPU model": "Intel Core i7",
       "Hard disk size": "1 TB",
       "color": "silver" # Example adding optional field directly
   }
}

# Example of data variations for parameterization
UPDATE_DATA_PRICE_ONLY = {
    "data": {
        "price": 999.99
    }
}

UPDATE_DATA_FULL = {
    "data": {
       "year": 2025,
       "price": 2199.50,
       "CPU model": "Intel Core i9 Raptor Lake",
       "Hard disk size": "2 TB",
       "color": "space gray"
   }
}

