from flask import Flask, request, jsonify
from functools import wraps


app = Flask(__name__)

users = {"testuser@example.com": "password123"}
tasks = []
token_store = {"testuser@example.com": "testtoken"}


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"message": "Missing or invalid token"}), 401
        token = auth_header.split(" ")[1]
        if token != "testtoken":
            return jsonify({"message": "Invalid token"}), 403
        return f(*args, **kwargs)
    return decorated

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    if users.get(email) == password:
        return jsonify({"token": token_store[email]})
    return jsonify({"message": "Invalid credentials"}), 403

@app.route("/api/tasks", methods=["POST"])
@token_required
def create_task():
    data = request.get_json()
    if not data.get("title"):
        return jsonify({"message": "Title is required"}), 400
    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "description": data.get("description", ""),
        "status": data.get("status", "To Do")
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route("/api/tasks", methods=["GET"])
@token_required
def get_tasks():
    return jsonify(tasks), 200

@app.route("/api/tasks/search", methods=["GET"])
@token_required
def search_tasks():
    query = request.args.get("query", "").lower()
    filtered = [task for task in tasks if query in task["title"].lower() or query in task["description"].lower()]
    return jsonify(filtered), 200

if __name__ == "__main__":
    app.run(debug=True)