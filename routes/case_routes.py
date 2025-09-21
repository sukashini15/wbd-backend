# routes/case_routes.py
from flask import Blueprint, request, jsonify
from models.case import Case
from database.db import SessionLocal

case_bp = Blueprint("case_bp", __name__)

@case_bp.route("/api/cases", methods=["POST"])
def submit_case():
    try:
        data = request.json
        # Validate required fields
        required_fields = ["area", "ph", "turbidity", "temperature", "rainfall", "disease_reported"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"{field} is required"}), 400

        session = SessionLocal()
        case = Case(
            area=data["area"],
            ph=data["ph"],
            turbidity=data["turbidity"],
            temperature=data["temperature"],
            rainfall=data["rainfall"],
            disease_reported=data["disease_reported"]
        )
        session.add(case)
        session.commit()
        session.close()
        return jsonify({"message": "Report submitted successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
