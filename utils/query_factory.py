import random


class QueryPayload:
   GADGETS = ["Huawei MateBook X Pro", "Apple MacBook Pro"]
   YEAR = [2023, 2024]
   CPU = ["Intel Core i9", "Intel Core i7"]
   HARD_DISK = ["1 TB", "512 GB"]
   COLOR = ["black", "silver"]

   def generate_price():
      price = random.uniform(1000, 2000)
      return "{:.2f}".format(price)

   @staticmethod
   def create_laptop_payload(**overrides) -> dict:
      # Default values
      name = overrides.get("name", QueryPayload.GADGETS[0])
      year = overrides.get("year", QueryPayload.YEAR[0])
      cpu = overrides.get("cpu", QueryPayload.CPU[0])
      hard_disk = overrides.get("hard_disk", QueryPayload.HARD_DISK[0])
      price = overrides.get("price") or QueryPayload.generate_price()

      # Create default data dictionary
      data = {
         "year": year,
         "price": price,
         "CPU model": cpu,
         "Hard disk size": hard_disk,
      }

      payload = {"name": name, "data": data}
      
      optional_fields = ["color", "generation"]
      for field in optional_fields:
         if field in overrides:
               payload[field] = overrides[field]

      payload.update(overrides)

      return payload
