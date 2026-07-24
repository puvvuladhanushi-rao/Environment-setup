import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Prepare the dataset
data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Exam_Score":    [35, 40, 50, 55, 60, 65, 70, 78, 85, 95]
}
df = pd.DataFrame(data)
print("Dataset:\n", df)

# 2. Define features (X) and target (y)
X = df[["Hours_Studied"]]
y = df["Exam_Score"]

# 3. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTraining samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# 4. Create the Linear Regression model
model = LinearRegression()

# 5. Train the model
model.fit(X_train, y_train)
print("\nModel trained successfully!")
print("Learned Slope (m):", model.coef_[0])
print("Learned Intercept (c):", model.intercept_)

# 6. Sanity check on training data
train_predictions = model.predict(X_train)
comparison = pd.DataFrame({
    "Actual": y_train.values,
    "Predicted": train_predictions
})
print("\nTraining Data Comparison:\n", comparison)

# 7. Save the trained model
model_path = os.path.join(os.path.dirname(__file__), "linear_regression_model.pkl")
with open(model_path, "wb") as file:
    pickle.dump(model, file)
print(f"\nModel saved as {model_path}")