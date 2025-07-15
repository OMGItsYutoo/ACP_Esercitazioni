from flask import Flask, request

app=Flask(__name__)

@app.post("/update_history") # not really an API REST, it should be somth like "/history_record"
def update_history():
    data=request.json
    
    try:
        operation=data["operation"]
        serial_number=data["serial_number"]        
    except KeyError:
        print("[HistoryServer] - Bad post request")
        return {"result": "failure"}, 400
    
    with open("server/history.txt", 'a') as f:
        f.write('-'.join([operation, str(serial_number)])+'\n')
        
    return {"result":"success"}, 200

if __name__=="__main__":
    app.run(debug=True, host="localhost")