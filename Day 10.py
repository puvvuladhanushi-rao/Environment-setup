from pathlib import Path

import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

base_dir = Path(__file__).resolve().parent
model_path = base_dir / "linear_regression_model.pkl"

# 1. Recreate the same dataset used in Day 7/8/9
data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Exam_Score":    [35, 40, 50, 55, 60, 65, 70, 78, 85, 95]
}
df = pd.DataFrame(data)

X = df[["Hours_Studied"]]
y = df["Exam_Score"]

# 2. Reproduce the same train-test split (same random_state as Day 8)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Load the trained model
if not model_path.exists():
    raise FileNotFoundError(f"Model file not found: {model_path}")

model = joblib.load(model_path)
print("Model loaded successfully!")

# 4. Predict on the test set
y_pred = model.predict(X_test)

comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred.round(2)
})
print("\nActual vs Predicted:\n", comparison)

# 5. Evaluate using MAE, MSE, R²
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R² Score: {r2:.4f}")

# 6. Interpretation
print("\n--- Interpretation ---")
print(f"On average, predictions are off by about {mae:.2f} points (MAE).")
print(f"The model explains {r2*100:.2f}% of the variance in exam scores (R²).")