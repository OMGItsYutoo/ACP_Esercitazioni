from flask import Flask, request
from pymongo import MongoClient

app=Flask(__name__)

def get_database():
    client=MongoClient("localhost", 27017)
    return client["sensors_data"]

@app.post("/sensor")
def register_sensor():
    
    data=request.json
    
    try: 
        id=data["_id"]
        data_type=data["data_type"]
    except IndexError:
        print("[Controller] - Bad request")
        return {"result":"failure"},400
    
    db=get_database()
    collection=db["sensors"]
    
    try:
        collection.insert_one({"_id":id, "data_type":data_type})
    except Exception:
        print("[Controller] - An error occurred.")
        return {"result":"failure"}, 500
    
    print(f"[Controller] - Successfully added sensor {id} to the db")
    return {"result":"success"}, 200
    
@app.post("/data/<data_type>")
def register_measurement(data_type):
    
    if data_type not in ["temp","press"]:
        print("[Controller] - Couldn't recognize the data type, bad request")
        return {"result":"failure"}, 400
    
    data=request.json
    
    try:
        sensor_id=data["sensor_id"]
        measurement=data["data"]
    except IndexError:
        print("[Controller] - Bad request")
        return {"result":"failure"},400
        
    db=get_database()
    collection=db[data_type+"_data"]
    
    try:
        collection.insert_one({"sensor_id":sensor_id, "data":measurement})
    except Exception:
        print("[Controller] - An error occurred.")
        return {"result":"failure"}, 500
    
    return {"result":"success"},200

if __name__=="__main__":
    app.run(debug=True, host="localhost")