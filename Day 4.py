import pandas as pd
from pathlib import Path


def main():
    # Welcome to Day 4!
    print("Day 4 - Pandas Basics\n")

    # ---------- Load Dataset ----------
    data_file = Path(__file__).resolve().parent / "student_scores.csv"
    if not data_file.exists():
        raise FileNotFoundError(
            f"Could not find student_scores.csv.\n"
            f"Expected file at: {data_file}\n"
            "Run the script from the codomax folder or place the CSV next to Day 4.py."
        )

    df = pd.read_csv(data_file)
    print("Dataset loaded successfully!\n")

    # ---------- Explore Rows ----------
    print("First 5 rows:")
    print(df.head(), "\n")

    print("Last 5 rows:")
    print(df.tail(), "\n")

    print("Random 3 rows:")
    print(df.sample(3), "\n")

    # ---------- Explore Columns ----------
    print("Column Names:", list(df.columns), "\n")

    # ---------- Dataset Shape ----------
    print("Dataset Shape (rows, columns):", df.shape, "\n")

    # ---------- Dataset Info ----------
    print("Dataset Info:")
    print(df.info(), "\n")

    # ---------- Statistical Summary ----------
    print("Statistical Summary:")
    print(df.describe(), "\n")

    # ---------- Check for Missing Values ----------
    print("Missing Values per Column:")
    print(df.isnull().sum(), "\n")

    # ---------- Access Specific Column ----------
    print("StudyHours column:")
    print(df["StudyHours"].head(), "\n")

    print("Average Study Hours:", df["StudyHours"].mean())
    print("Average Score:", df["Score"].mean())


if __name__ == "__main__":
    main()