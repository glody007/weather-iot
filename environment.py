import random

class Environment(): 
    generals = [
        {"name": "Temperature", "value": 32, "unit": "c"},
        {"name": "Humidite", "value": 0, "unit": ""},
        {"name": "PM2.5", "value": 0, "unit": ""},
        {"name": "PM10", "value": 0, "unit": ""}
    ]
    polluants = [
        {"name": "C7H8", "value": 0, "unit": ""},
        {"name": "C3H6O", "value": 0, "unit": ""},
        {"name": "H2", "value": 0, "unit": ""},
        {"name": "NOx", "value": 0, "unit": ""},
        {"name": "CL2", "value": 0, "unit": ""},
        {"name": "O3", "value": 0, "unit": ""},
        {"name": "Benzene", "value": 0, "unit": ""},
        {"name": "Hexane", "value": 0, "unit": ""},
        {"name": "Alcool", "value": 0, "unit": ""},
        {"name": "Methane", "value": 0, "unit": ""},
        {"name": "LPG", "value": 0, "unit": ""},
        {"name": "HS2", "value": 0, "unit": ""},
        {"name": "CO", "value": 0, "unit": ""},
        {"name": "CO2", "value": 0, "unit": ""},
        {"name": "NH3", "value": 0, "unit": ""},
        {"name": "Air quality", "value": 0, "unit": ""}
    ]
    
    def get_polluant_history(self, name): 
        return [random.randint(1, 10) for day in (range(7))]