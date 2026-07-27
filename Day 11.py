from pathlib import Path

import joblib
import pandas as pd


base_dir = Path(__file__).resolve().parent
model_path = base_dir / "linear_regression_model.pkl"


def load_model(path=model_path):
    try:
        model = joblib.load(path)
        return model
    except FileNotFoundError:
        print(f"Error: '{path}' not found. Run Day 8's script first to generate it.")
        exit()


def predict_score(model, hours):
    input_df = pd.DataFrame({"Hours_Studied": [hours]})
    prediction = model.predict(input_df)[0]
    return prediction


def main():
    model = load_model()
    print("=== Student Score Predictor ===")
    print("Type 'quit' at any time to exit.\n")

    while True:
        user_input = input("Enter hours studied: ").strip()

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        try:
            hours = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number (e.g. 5.5) or 'quit'.\n")
            continue

        if hours < 0:
            print("Hours studied cannot be negative. Try again.\n")
            continue

        score = predict_score(model, hours)

        # Cap displayed score at a realistic maximum
        display_score = min(score, 100)

        print(f"Predicted Exam Score: {display_score:.2f}")
        if score > 100:
            print("(Note: raw model output exceeded 100 - capped for realism)")
        print()


if __name__ == "__main__":
    main()