# from flask import Blueprint, request, jsonify
# import joblib

# alert_bp = Blueprint('alerts', __name__)

# # Load models (reuse same as predict)
# model_regressor = joblib.load("ml_models/lgbm_model.pkl")
# model_classifier = joblib.load("ml_models/rf_model.pkl")

# @alert_bp.route("/api/alerts", methods=["POST"])
# def alerts():
#     try:
#         data = request.get_json()

#         ph = data.get("ph")
#         turbidity = data.get("turbidity")
#         temperature = data.get("temperature")
#         rainfall = data.get("rainfall")

#         features = [[ph, turbidity, temperature, rainfall]]

#         # Predict using models
#         risk_score = model_regressor.predict(features)[0]
#         disease_class = model_classifier.predict(features)[0]

#         # Define alert logic
#         if turbidity > 5 or ph < 6.5 or ph > 8.5:
#             water_status = "Unsafe"
#         else:
#             water_status = "Safe"

#         if risk_score > 0.7:
#             disease_risk = "High risk of outbreak"
#         else:
#             disease_risk = "Low risk"

#         return jsonify({
#             "water_status": water_status,
#             "risk_score": float(risk_score),
#             "predicted_disease": str(disease_class),
#             "alert_message": f"Water is {water_status}, Disease Risk: {disease_risk}"
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
