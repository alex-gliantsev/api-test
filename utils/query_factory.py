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
   
   def create_payload(
      name=None, 
      year=None, 
      cpu=None, 
      hard_disk=None, 
      price=None, 
      color=None, 
      include_fields=None, 
      exclude_fields=None
      ):
      
      # Default values
      name = name or QueryPayload.GADGETS[0]
      year = year or QueryPayload.YEAR[0]
      cpu = cpu or QueryPayload.CPU[0]
      hard_disk = hard_disk or QueryPayload.HARD_DISK[0]
      color = color or QueryPayload.COLOR[0]
      price = price or QueryPayload.generate_price()
      
      # Create default data dictionary
      data = {
         "year": year,
         "price": price,
         "CPU model": cpu,
         "Hard disk size": hard_disk
      }
      
      # Handle inclusion/exclusion
      if exclude_fields:
         for field in exclude_fields:
            if field in data:
                  del data[field]
      
      if include_fields:
         data = {k: v for k, v in data.items() if k in include_fields}
      
      payload = {
         "name": name,
         "data": data
      }
      
      return payload
   
   # Такой подход позволяет выборочно контролировать, какие поля отображаются в данных, 
   # путем добавления двух необязательных параметров:
   # include_fields: Список конкретных полей для включения
   # exclude_fields: Список полей для исключения