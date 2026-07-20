import numpy as np


def main():
    # Welcome to Day 3!
    print("Day 3 - NumPy Fundamentals\n")

    # ---------- Creating Arrays ----------
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])

    print("1D Array:", arr1)
    print("2D Array:\n", arr2)
    print("Shape of arr1:", arr1.shape)
    print("Shape of arr2:", arr2.shape)

    # ---------- Special Arrays ----------
    print("\nSpecial Arrays:")
    print("Zeros:\n", np.zeros((2, 3)))
    print("Ones:\n", np.ones((2, 3)))
    print("Range Array:", np.arange(0, 10, 2))
    print("Linspace:", np.linspace(0, 1, 5))

    # ---------- Indexing & Slicing ----------
    print("\nIndexing & Slicing:")
    print("First element of arr1:", arr1[0])
    print("Last element of arr1:", arr1[-1])
    print("Slice arr1[1:4]:", arr1[1:4])
    print("Element at row 1, col 2 of arr2:", arr2[1, 2])
    print("First row of arr2:", arr2[0, :])
    print("Second column of arr2:", arr2[:, 1])

    # ---------- Mathematical Operations ----------
    print("\nMathematical Operations:")
    a = np.array([10, 20, 30])
    b = np.array([1, 2, 3])

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Square Root:", np.sqrt(a))
    print("Sum:", np.sum(a))
    print("Mean:", np.mean(a))
    print("Max:", np.max(a))
    print("Min:", np.min(a))
    print("Standard Deviation:", np.std(a))

    # ---------- Array-based Calculation Example ----------
    print("\nArray-based Calculation Example:")
    study_hours = np.array([1, 2, 3, 4, 5])
    scores = study_hours * 10 + 5   # simple linear relationship
    print("Study Hours:", study_hours)
    print("Predicted Scores:", scores)


if __name__ == "__main__":
    main()