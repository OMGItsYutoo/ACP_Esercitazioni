from flask import Flask, request
from pymongo import MongoClient

app=Flask(__name__)

def get_database():
    client=MongoClient("localhost", 27017)
    return client["hotel_data"]
    
@app.post("/booking")
def create_booking():
    
    data=request.json
    
    try:
        client=data["client"]
        hotel=data["hotel"]
        operator=data["operator"]
        nights=int(data["nights"])
        people=int(data["people"])
        cost=int(data["cost"])
    except KeyError:
        print("[DBServer] - An error occurred: KeyError while parsing fields from request json.")
        return {"result":"bad request"}, 400
        
    db=get_database()
    collection=db["bookings"]
    
    try:
        collection.insert_one({
            "client":client,
            "hotel":hotel,
            "operator":operator,
            "nights":nights,
            "people":people,
            "cost":cost,
        })
    except Exception:
        print("[DBServer] - An error occurred: Exception while inserting into the db.")
        return {"result":"server error"}, 500
    
    print("[DBServer] - Successfully added the booking to the DB.")
    
    return {"result":"success"}, 200
     
@app.put("/booking")
def discount_bookings():
    data=request.json
    
    try:
        operator=data["operator"]
        nights=int(data["nights"])
        discount=int(data["discount"])
    except KeyError:
        print("[DBServer] - An error occurred: KeyError while parsing fields from request json.")
        return {"result":"bad request"}, 400
    
    db=get_database()
    collection=db["bookings"]
    
    try:
        query={"operator":operator,"nights":{"$gte":nights}}
        result = collection.find(query)
        
        update_cnt=0
        for res in result:
            upd_cost=max(0, res["cost"]-discount)
            collection.update_one({"_id":res["_id"]},{"$set":{"cost":upd_cost}})
            update_cnt+=1
    except Exception:
        print("[DBServer] - An error occurred: Exception while docs in the db.")
        return {"result":"server error"}, 500
        
    return {"result":f"success, updated_cnt: {update_cnt}"}, 200
    
if __name__=="__main__":
    app.run(debug=True, host="localhost")