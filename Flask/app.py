from flask import Flask, render_template, request
import time

app=Flask(__name__)

@app.route("/")
def index():
    return "<script>alert(1)</script>"

@app.route("/user/<name>")
def hello_user(name):
    return render_template("user.html", template_name=name)

@app.post("/postroute")
def hello():
    json=request.get_json()
    a=json["a"]
    return f"hello {a}"

@app.route("/api/items", methods=['GET'])
def get_items():
    # Simulate a list of items
    items = [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
        {"id": 3, "name": "Item 3"}
    ]
    return {"items": items}

@app.route("/api/items/<int:item_id>", methods=['GET'])
def get_item(item_id):
    # Example of path parameter with type checking
    return {"id": item_id, "name": f"Item {item_id}"}

@app.route("/api/calculate", methods=['POST'])
def calculate():
    data = request.get_json()
    if not data or 'x' not in data or 'y' not in data:
        return {"error": "Missing required parameters"}, 400
    
    try:
        result = float(data['x']) + float(data['y'])
        return {"result": result}
    except ValueError:
        return {"error": "Invalid numeric values"}, 400

@app.route("/template-example")
def template_example():
    context = {
        "title": "Template Example",
        "items": ["Apple", "Banana", "Orange"],
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return render_template("example.html", **context)
    
if __name__=="__main__":
    app.run(host="0.0.0.0", port="5001",debug=True)