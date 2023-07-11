import random
from datetime import datetime
from config import Parameters, polluants, general_parameters
from model import Data, WEEK

class Environment(): 
    
    generals = []
    polluants = []
    
    def get_param(self, name):
        data = Data.last(name=name)
        return {
            "name": name, 
            "value": data.value if data is not None else 0, 
            "unit": ""
        } 
    
    def update(self):
        self.generals = [self.get_param(name) for name in general_parameters]
        self.polluants = [self.get_param(name) for name in polluants]
    
    def get_dict_from_data(self, data):
        return { 
            "name": data.name, 
            "time": datetime.now(), 
            "value": data.value 
        }
        
    def get_random_data_dict(self, name):
        return { 
            "name": name, 
            "time": datetime.now(), 
            "value": random.randint(1, 10)
        }
    
    def get_random_history(self, name):
        return [self.get_random_data_dict(name) for day in (range(7))]
    
    
    def get_polluant_history(self, name): 
        return [
            self.get_dict_from_data(data) for data in Data.history(name=name, range=WEEK)
        ]
        