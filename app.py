import joblib
import numpy as np
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# ✅ Load trained model and scaler
model = joblib.load("artifacts/model_training/model.joblib")
scaler = joblib.load("artifacts/data_transformation/scaler.joblib")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Extract user input
            credit_score = float(request.form["CreditScore"])
            geography = request.form["Geography"]
            gender = request.form["Gender"]
            age = int(request.form["Age"])
            tenure = int(request.form["Tenure"])
            balance = float(request.form["Balance"])
            num_of_products = int(request.form["NumOfProducts"])
            has_cr_card = int(request.form["HasCrCard"])
            is_active_member = int(request.form["IsActiveMember"])
            estimated_salary = float(request.form["EstimatedSalary"])

            # One-hot encoding for categorical values
            geography_map = {"France": [1, 0], "Germany": [0, 1], "Spain": [0, 0]}
            gender_map = {"Male": 1, "Female": 0}

            geography_encoded = geography_map[geography]
            gender_encoded = gender_map[gender]

            # Convert input into numpy array
            input_data = np.array([[
                credit_score, age, tenure, balance, num_of_products,
                has_cr_card, is_active_member, estimated_salary,
                *geography_encoded, gender_encoded
            ]])

            # ✅ Apply Scaling (only required features)
            scaled_values = scaler.transform(input_data[:, [0, 3, 7]])  # Scale CreditScore, Balance, EstimatedSalary
            input_data[:, [0, 3, 7]] = scaled_values  # Replace original values

            # ✅ Make prediction
            prediction = model.predict(input_data)
            result = "Churn" if prediction[0] == 1 else "No Churn"

            # ✅ Convert scaled values to dictionary for display
            scaled_features = {
                "Credit Score (scaled)": round(scaled_values[0][0], 4),
                "Balance (scaled)": round(scaled_values[0][1], 4),
                "Estimated Salary (scaled)": round(scaled_values[0][2], 4),
            }

            return render_template("index.html", prediction=result, scaled_features=scaled_features)

        except Exception as e:
            print(f"Error: {e}")
            return render_template("index.html", prediction="Error in prediction", scaled_features=None)

    return render_template("index.html", prediction=None, scaled_features=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
