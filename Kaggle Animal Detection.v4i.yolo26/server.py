from flask import Flask

app = Flask(__name__)

@app.route("/animal")
def animal():
    print("Animal detected! Alert received.")
    return "Alert received"

app.run(host="0.0.0.0", port=5000)