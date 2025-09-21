from flask import Blueprint, jsonify

# Blueprint for disease routes
disease_bp = Blueprint("disease_bp", __name__)

SYMPTOMS = [
    "Fever",
    "Nausea",
    "Vomiting",
    "Diarrhea",
    "Abdominal pain",
    "Jaundice",
    "Headache",
    "Fatigue",
    "Loss of appetite",
    "Rash"
]


# API endpoint: GET /api/diseases
@disease_bp.route("/api/diseases", methods=["GET"])
def get_diseases():
    return jsonify({"diseases": SYMPTOMS})
