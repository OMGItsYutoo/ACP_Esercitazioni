from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello patatino</h1>"

@app.route("/user/<name>")
def hello_user(name):
    return render_template("user.html", template_name=name)

if __name__=="__main__":
    app.run(host="0.0.0.0", port="5001",debug=True)