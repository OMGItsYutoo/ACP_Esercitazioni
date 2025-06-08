from flask import Flask, request
from pymongo import MongoClient

app=Flask(__name__)

def get_database():
    client=MongoClient("localhost",27017)
    return client["sensors_data"]
    
@app.post("/sensor")
def add_sensor():
    
    data=request.get_json()
    
    print("[Controller] - Received ",data)
    
    db=get_database()
    sensor_coll=db["sensors"]
    
    try:
        sensor_coll.insert_one(data)
    except Exception as e:
        print(f"[Controller] - DB insert failed {str(e)}")
        return {"result":f"failure {str(e)}"},500
    else:
        return {"result":"success"}

@app.post("/data/<data_type>")
def store_data(data_type):
    body=request.get_json()
    
    try:
        id=body["sensor_id"]
        data=body["data"]
    except KeyError:
        return {"result":"failure"}, 500    
    
    db=get_database()
    if data_type == "temp":
        data_collection = db['temp_data']
    elif data_type == "press":
        data_collection = db['press_data']
    else:
        return {'result' : 'Unsupported data type'}, 400
    
    try:
        data_collection.insert_one(body)
    except Exception as e:
        print(f"[Controller] - DB insert failed {str(e)}")
        return {"result":f"failure {str(e)}"},500
    else:
        return {"result":"success"}

if __name__=="__main__":
    app.run(debug=True,host='localhost',port=5001)