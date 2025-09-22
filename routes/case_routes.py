# routes/case_routes.py
from flask import Blueprint, request, jsonify
from models.case import Case
from database.db import SessionLocal
import uuid

case_bp = Blueprint("case_bp", __name__)

@case_bp.route("/api/cases", methods=["POST"])
def submit_case():
    try:
        data = request.json
        session = SessionLocal()

        # Must have user_id
        if "user_id" not in data:
            return jsonify({"error": "user_id is required"}), 400

        # If report_id is sent, use it; else generate new
        report_id = data.get("report_id", str(uuid.uuid4()))

        # Check if record exists
        existing_case = session.query(Case).filter_by(report_id=report_id).first()
        if existing_case:
            # Update existing record
            if "symptoms" in data:
                existing_case.symptoms = data["symptoms"]
            if "ph" in data:
                existing_case.ph = data["ph"]
            if "turbidity" in data:
                existing_case.turbidity = data["turbidity"]
            if "temperature" in data:
                existing_case.temperature = data["temperature"]
            if "rainfall" in data:
                existing_case.rainfall = data["rainfall"]
            if "disease_reported" in data:
                existing_case.disease_reported = data["disease_reported"]

            session.commit()
            session.close()
            return jsonify({"message": "Report updated successfully", "report_id": report_id}), 200

        else:
            # Create new record
            case = Case(
                user_id=data["user_id"],
                report_id=report_id,
                symptoms=data.get("symptoms"),
                ph=data.get("ph"),
                turbidity=data.get("turbidity"),
                temperature=data.get("temperature"),
                rainfall=data.get("rainfall"),
                disease_reported=data.get("disease_reported")
            )
            session.add(case)
            session.commit()
            session.close()
            return jsonify({"message": "Report submitted successfully", "report_id": report_id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
