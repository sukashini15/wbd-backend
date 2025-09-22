from flask import Blueprint, request, jsonify
import pickle
import numpy as np

predict_bp = Blueprint('predict', __name__)

# Load trained models
with open("ml_models/lgbm_model.pkl", "rb") as f:
    lgbm_model = pickle.load(f)

with open("ml_models/rf_model.pkl", "rb") as f:
    rf_model = pickle.load(f)

@predict_bp.route("/api/predict", methods=["POST"])
def predict_disease():
    try:
        data = request.get_json()

        # Extract features
        ph = float(data.get("ph"))
        turbidity = float(data.get("turbidity"))
        temperature = float(data.get("temperature"))
        rainfall = float(data.get("rainfall"))

        features = np.array([[ph, turbidity, temperature, rainfall]])

        # Model predictions
        risk_score = lgbm_model.predict(features)[0]   # e.g., 0.85 → 85% risk
        disease_prediction = rf_model.predict(features)[0]  # e.g., "Cholera"

        return jsonify({
            "status": "success",
            "risk_score": round(float(risk_score), 2),
            "predicted_disease": str(disease_prediction)
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
