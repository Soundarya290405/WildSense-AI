from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Animal Detection Backend Running"

@app.route("/detect", methods=["POST"])
def detect():

    data = request.json

    animal = data.get("animal")
    location = data.get("location")

    print(f"Animal detected: {animal}")
    print(f"Location: {location}")

    return jsonify({
        "status": "success",
        "animal": animal,
        "location": location
    })

app.run(host="0.0.0.0", port=5000)