from .config_manager import *
from .models.single_postcodes_model import SinglePCModel
import requests

class SinglePC():
    
    def __init__(self, single_post_code):
        self.url = base_url() + f"postcodes/{single_post_code}"
        self.request = requests.get(self.url)
        self.header_details = self.request.headers
        self.response_json = self.request.json()

    def response_data(self):
        return SinglePCModel(self.response_json)

