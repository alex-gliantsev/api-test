import requests
from endpoints.base_endpoint import BaseEndpoint


class CreateGadget(BaseEndpoint):
   
   def new_gadget(self, endpoint="", payload=None, **kwargs):
      url = f"{BaseEndpoint.base_url}/{endpoint}".rstrip('/')
      self.response = requests.post(url, json=payload, **kwargs)
      self.response_json = self.response.json()
