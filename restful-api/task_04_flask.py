#!/usr/bin/python3
"""A simple Flask API application."""
from flask import Flask, jsonify, request

app = Flask(__name__)

# تخزين المستخدمين في الذاكرة (بدون بيانات تجريبية ثابتة لتجنب مشاكل التصحيح)
users = {}


@app.route("/")
def home():
    """Home route returning a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Status route returning OK."""
    return "OK"


@app.route("/data")
def get_data():
    """Return a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Retrieve full details of a specific user by username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the users dictionary."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # إضافة المستخدم الجديد
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
