from threading import Thread
from random import choice, randint
import requests

N_MEAS=5

class SensorThread(Thread):
    def __init__(self, name, id, base_url):
        super().__init__(name=name)
        self.id=id
        self.base_url=base_url
        
    def run(self):
        
        data_type=choice(["temp", "press"])
        
        registering_data={
            "_id": self.id,
            "data_type": data_type
        }
        
        req=requests.post(self.base_url+"/sensor", json=registering_data)
        
        try:
            req.raise_for_status()
            print(f"[{self.name}] - Response from controller: {req.text}")
        except requests.HTTPError:
            print(f"[{self.name}] - An error occurred: {req.text}")
        
        for _ in range(N_MEAS):
            
            meas_data={
                "sensor_id":self.id,
                "data": randint(1,50)
            }
            
            req=requests.post(self.base_url+f"/data/{data_type}", json=meas_data)
            
            try:
                req.raise_for_status()
                print(f"[{self.name}] - Response from controller: {req.text}")
            except requests.HTTPError:
                print(f"[{self.name}] - An error occurred: {req.text}")
                
            
        
            
        