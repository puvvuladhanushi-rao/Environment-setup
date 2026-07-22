import pandas as pd
import numpy as np
data = {
    "Name":    ["Alice", "Bob", "Charlie", "David", "Eva", "Bob", None, "Frank"],
    "Age":     [25, np.nan, 30, 22, np.nan, np.nan, 28, 40],
    "City":    ["NY", "LA", "NY", None, "SF", "LA", "NY", "LA"],
    "Salary":  [50000, 60000, np.nan, 45000, 52000, 60000, 47000, np.nan],
}
df = pd.DataFrame(data)
 
print("=" * 60)
print("ORIGINAL DATASET")
print("=" * 60)
print(df)

print("\n" + "=" * 60)
print("BASIC INFO")
print("=" * 60)
print(df.info())
 
print("\n" + "=" * 60)
print("MISSING VALUES PER COLUMN")
print("=" * 60)
print(df.isnull().sum())
 
print("\n" + "=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)
print(f"Number of duplicate rows: {df.duplicated().sum()}")
 
print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS (before cleaning)")
print("=" * 60)
print(df.describe(include="all"))

numeric_cols = df.select_dtypes(include=np.number).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
 

categorical_cols = df.select_dtypes(include=["object", "str"]).columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])
 
print("\n" + "=" * 60)
print("AFTER HANDLING MISSING VALUES")
print("=" * 60)
print(df)
print("\nRemaining missing values:\n", df.isnull().sum())
 

before_rows = len(df)
df = df.drop_duplicates()
after_rows = len(df)
 
print("\n" + "=" * 60)
print("AFTER REMOVING DUPLICATES")
print("=" * 60)
print(f"Rows before: {before_rows}, Rows after: {after_rows}")
print(df)
 

df = df.reset_index(drop=True)
 
# 
print("\n" + "=" * 60)
print("FINAL DESCRIPTIVE STATISTICS")
print("=" * 60)
print(df.describe(include="all"))
 
print("\n" + "=" * 60)
print("FINAL CLEAN DATASET")
print("=" * 60)
print(df)
 

output_path = "cleaned_dataset.csv"
df.to_csv(output_path, index=False)
print(f"\nClean dataset saved to: {output_path}")