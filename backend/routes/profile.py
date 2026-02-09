from flask import Blueprint, request, jsonify

profile_bp = Blueprint("profile", __name__)

profiles = {}

@profile_bp.route("/study-details", methods=["POST"])
def study_details():
    data = request.json
    profiles[data["email"]] = data
    return jsonify({"message": "Profile saved"})
