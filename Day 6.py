# Day 6 - Data Visualization
# Task: Create Scatter Plot, Bar Chart, and Line Chart

import os
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "student_scores.csv")
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"Missing required file: {csv_path}")

df = pd.read_csv(csv_path)

# Display first few rows
print("Dataset Preview:")
print(df.head())

# -----------------------------
# Scatter Plot
# -----------------------------
plt.figure(figsize=(6,4))
plt.scatter(df['StudyHours'], df['Score'], color='blue')
plt.title("Hours Studied vs Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.grid(True)
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.close()
print("Saved scatter_plot.png")

# -----------------------------
# Bar Chart
# -----------------------------
plt.figure(figsize=(6,4))
plt.bar(df.index, df['Score'], color='green')
plt.title("Student Scores")
plt.xlabel("Student Index")
plt.ylabel("Scores")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()
print("Saved bar_chart.png")

# -----------------------------
# Line Chart
# -----------------------------
plt.figure(figsize=(6,4))
plt.plot(df['StudyHours'], df['Score'], marker='o', color='red')
plt.title("Hours Studied vs Scores (Line Chart)")
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.grid(True)
plt.tight_layout()
plt.savefig("line_chart.png")
plt.close()
print("Saved line_chart.png")
