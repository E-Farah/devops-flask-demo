from flask import Flask, request, jsonify

app = Flask(__name__)

# existing add function
def add(a, b):
    return a + b

# health check
@app.route("/")
def home():
    return {"message": "DevOps app is running"}

# addition endpoint
@app.route("/add", methods=["GET"])
def add_numbers():
    try:
        a = int(request.args.get("a"))
        b = int(request.args.get("b"))
        result = add(a, b)
        return jsonify({"result": result})
    except:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)