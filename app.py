import os
from flask import Flask, request, jsonify

# Get environment variable; default to 'development' if not set
ENV = os.getenv("APP_ENV", "development")

# Set debug mode based on environment
if ENV == "development":
    DEBUG = True  # Local development: show detailed errors/info
else:
    DEBUG = False  # Production: avoid exposing internal info

app = Flask(__name__)
app.config["DEBUG"] = DEBUG  # Determines if detailed errors are shown


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
