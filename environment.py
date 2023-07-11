import random
from datetime import datetime
from config import Parameters
from model import Data, WEEK

class Environment(): 
    generals = [
        {"name": Parameters.TEMPERATURE, "value": 32, "unit": "c"},
        {"name": Parameters.HUMIDITY, "value": 0, "unit": ""},
        {"name": Parameters.PM2_5, "value": 0, "unit": ""},
        {"name": Parameters.PM10, "value": 0, "unit": ""}
    ]
    
    polluants = [
        {"name": Parameters.C7H8, "value": 0, "unit": ""},
        {"name": Parameters.C3H6O, "value": 0, "unit": ""},
        {"name": Parameters.H2, "value": 0, "unit": ""},
        {"name": Parameters.NOX, "value": 0, "unit": ""},
        {"name": Parameters.CL2, "value": 0, "unit": ""},
        {"name": Parameters.O3, "value": 0, "unit": ""},
        {"name": Parameters.BENZENE, "value": 0, "unit": ""},
        {"name": Parameters.HEXANE, "value": 0, "unit": ""},
        {"name": Parameters.ALCOOL, "value": 0, "unit": ""},
        {"name": Parameters.METHANE, "value": 0, "unit": ""},
        {"name": Parameters.LPG, "value": 0, "unit": ""},
        {"name": Parameters.HS2, "value": 0, "unit": ""},
        {"name": Parameters.CO, "value": 0, "unit": ""},
        {"name": Parameters.CO2, "value": 0, "unit": ""},
        {"name": Parameters.NH3, "value": 0, "unit": ""},
        {"name": Parameters.AIR_QUALITY, "value": 0, "unit": ""}
    ]
    
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
        