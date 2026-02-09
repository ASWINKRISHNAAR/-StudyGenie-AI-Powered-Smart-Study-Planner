from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)

users = {}

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if data["email"] in users:
        return jsonify({"message": "User already exists"}), 400
    users[data["email"]] = data["password"]
    return jsonify({"message": "Registration successful"})
