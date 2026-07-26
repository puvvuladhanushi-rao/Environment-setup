from pathlib import Path

import pandas as pd
import joblib

base_dir = Path(__file__).resolve().parent
model_path = base_dir / "linear_regression_model.pkl"
output_csv = base_dir / "predictions.csv"

# 1. Load the trained model from Day 8
if not model_path.exists():
    raise FileNotFoundError(f"Model file not found: {model_path}")

model = joblib.load(model_path)
print("Model loaded successfully!")
print("Slope (m):", model.coef_[0])
print("Intercept (c):", model.intercept_)

# 2. Predict for a single value
hours = [[6.5]]
predicted_score = model.predict(hours)
print(f"\nPredicted score for 6.5 hours studied: {predicted_score[0]:.2f}")

# 3. Predict for multiple new values at once
new_hours = pd.DataFrame({"Hours_Studied": [1.5, 3.5, 5.5, 7.5, 9.5, 11, 12]})
predictions = model.predict(new_hours)

results = pd.DataFrame({
    "Hours_Studied": new_hours["Hours_Studied"],
    "Predicted_Score": predictions.round(2)
})

# 4. Flag unrealistic predictions (above max possible exam score)
results["Realistic"] = results["Predicted_Score"].apply(
    lambda x: "Yes" if x <= 100 else "No (exceeds max score)"
)

print("\nPredictions:\n", results)

# 5. Save predictions to CSV
results.to_csv(output_csv, index=False)
print(f"\nPredictions saved to {output_csv}")