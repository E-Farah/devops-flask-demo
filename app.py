import os
from flask import Flask, request, jsonify

ENV = os.getenv("APP_ENV", "development")


if ENV == "development":
    DEBUG = True # if its run locally (development) then it's fine to show detailed errors/info
else:
    DEBUG = False # if ran on k8s (production) then showing detailed info could leak internal/secret info

app = Flask(__name__)
app.config["DEBUG"] = DEBUG # incase of an error(like division by zero) this decided whether to show detailed info (True) or not (False)
            

@app.route("/")
def home():
    return jsonify({
        "message": "The App is running!",
        "environment": ENV
    })

@app.route("/add")
def add():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return jsonify({"result": a + b})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

@app.route("/divide")
def divide():
    try:
        x = float(request.args.get("x"))
        y = float(request.args.get("y"))
        return jsonify({"result": x / y})
    except ZeroDivisionError:
        return jsonify({"error": "Cannot divide by zero"}), 400
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
