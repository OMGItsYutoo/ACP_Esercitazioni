from threading import Thread
import random
import requests

types=["temp", "press"]
SERVER_BASE_URL="http://localhost:5001"

def thr_fun(sensor_id):
    data_type=random.choice(types)
    
    #sensor registration
    sensor_spec={
        "_id":sensor_id,
        "data_type":data_type
    }
    
    resp=requests.post(SERVER_BASE_URL+"/sensor", json=sensor_spec)
    
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f"[Sensor - {sensor_id}] -{resp.status_code} Registration error")
    
    else: 
        print(f"[Sensor - {sensor_id}] - {resp.text}")
    
    #sending measuraments
    for _ in range(5):
        data=random.randint(1,50)
        sensor_meas={
            "sensor_id":sensor_id,
            "data":data
        }
        
        resp=requests.post(SERVER_BASE_URL+"/data/"+data_type, json=sensor_meas)
        
        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError:
            print(f"[Sensor - {sensor_id}] -{resp.status_code} InsertMeasurement {sensor_meas} error")
        
        else: 
            print(f"[Sensor - {sensor_id}] - {resp.text}")

def main():
    ths=[]
    for i in range(5):
        th=Thread(target=thr_fun, args=(i,))
        ths.append(th)
        th.start()
        
    for _ in range(5):
        th.join()
        
        
if __name__=="__main__": 
    main()