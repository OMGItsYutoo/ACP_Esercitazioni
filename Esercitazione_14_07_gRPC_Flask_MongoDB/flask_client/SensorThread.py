from threading import Thread
from random import randint, choice
import requests

class SensorThread(Thread):
    def __init__(self, name, id, server_base_url):
        super().__init__(name=name)
        self.id=id
        self.server_base_url=server_base_url
        
    def run(self):
        
        data_type=choice(["temp", "press"])
        
        data={
            "_id":self.id,
            "data_type": data_type
        }
        req=requests.post(self.server_base_url+"/sensor", json=data)
        
        try:
            req.raise_for_status()
        except requests.HTTPError as e:
            print(f"[{self.name}] - An error occurred: {str(e)}")
        
        print(f"[{self.name}] - Response from flask server is: {req.text}")
        
        for _ in range(5):
            meas_value=randint(1,50)
            
            data_meas={
                "sensor_id":self.id,
                "data": meas_value
            }
            
            req=requests.post(self.server_base_url+f"/data/{data_type}", json=data_meas)
            
            try:
                req.raise_for_status()
            except requests.HTTPError as e:
                print(f"[{self.name}] - An error occurred: {str(e)}")
            
            print(f"[{self.name}] - Response from flask server is: {req.text}")
            
        
        

            
        
        
