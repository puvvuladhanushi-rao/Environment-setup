import pandas as pd
from statistics import mean

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Exam_Score":    [35, 40, 50, 55, 60, 65, 70, 78, 85, 95]
}

def train_test_split(df, test_size=0.2, random_state=None):
    if random_state is not None:
        df = df.sample(frac=1, random_state=random_state).reset_index(drop=True)
    split_index = int(len(df) * (1 - test_size))
    train = df.iloc[:split_index].reset_index(drop=True)
    test = df.iloc[split_index:].reset_index(drop=True)
    return train, test


def fit_linear_regression(x_values, y_values):
    x_mean = mean(x_values)
    y_mean = mean(y_values)
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, y_values))
    denominator = sum((x - x_mean) ** 2 for x in x_values)
    slope = numerator / denominator if denominator != 0 else 0.0
    intercept = y_mean - slope * x_mean
    return slope, intercept


def predict(x_values, slope, intercept):
    return [slope * x + intercept for x in x_values]


df = pd.DataFrame(data)
print("Dataset:\n", df)

train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

X_train = train_df["Hours_Studied"].tolist()
y_train = train_df["Exam_Score"].tolist()
X_test = test_df["Hours_Studied"].tolist()
y_test = test_df["Exam_Score"].tolist()

slope, intercept = fit_linear_regression(X_train, y_train)

y_pred = predict(X_test, slope, intercept)

mse = sum((actual - pred) ** 2 for actual, pred in zip(y_test, y_pred)) / len(y_test)
ss_res = sum((actual - pred) ** 2 for actual, pred in zip(y_test, y_pred))
ss_tot = sum((actual - mean(y_test)) ** 2 for actual in y_test)
r2 = 1 - ss_res / ss_tot if ss_tot != 0 else 0.0

print("\nSlope (m):", slope)
print("Intercept (c):", intercept)
print("Mean Squared Error:", mse)
print("R² Score:", r2)

hours = 6.5
predicted_score = slope * hours + intercept
print(f"\nPredicted score for {hours} hours studied: {predicted_score:.2f}")