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
    except KeyError:
        print("[Controller] - A problem occurred while gathering infos from post request")
        return {"result":"failure"},400
    
    if data_type not in ["temp", "press"]:
        print(f"[Controller] - Couldn't recognize di data type (data_type:{data_type})")
        return
    
    db=get_database()
    sensors_collection=db["sensors"]
    
    try:
        sensors_collection.insert_one({"_id":id, "data_type":data_type})
    except Exception as e:
        # l’operazione potrebbe fallire nel caso in cui il sensore sia già registrato, ovvero se _id è già presente nella collection di documents mongodb
        print(f"[Controller] - An exception occurred: {str(e)}")
        return {"result":"failure"},400

    return {"result":"success"},200

@app.post("/data/<data_type>")
def register_data_measurement(data_type):
    if data_type not in ["temp", "press"]:
        print(f"[Controller] - Couldn't recognize di data type (data_type:{data_type})")
        return

    data=request.json

    try:
        sensor_id=data["sensor_id"]
        data=data["data"]
    except KeyError:
        print("[Controller] - A problem occurred while gathering infos from post request")
        return {"result":"failure"},400
    
    db=get_database()
    collection=db[data_type+"_data"]
    
    collection.insert_one({"sensor_id":sensor_id, "data":data})
    
    return {"result":"success"},200
    
if __name__=="__main__":
    app.run(debug=True,host='localhost')