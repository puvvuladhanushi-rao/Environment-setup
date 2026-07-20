def main():
    # Welcome to Day 2!
    print("Day 2 - Python Basics\n")

    # ---------- Variables & Data Types ----------
    name = "Dhanush"          # string
    age = 21                  # integer
    height = 5.9               # float
    is_learning = True        # boolean

    print("Name:", name)
    print("Age:", age)
    print("Height:", height)
    print("Is Learning:", is_learning)
    print("Data Types:", type(name), type(age), type(height), type(is_learning))

    # ---------- Operators ----------
    a, b = 10, 3
    print("\nOperators:")
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Modulus:", a % b)
    print("Exponent:", a ** b)
    print("Is a > b?", a > b)

    # ---------- Loops ----------
    print("\nFor Loop (1 to 5):")
    for i in range(1, 6):
        print("Count:", i)

    print("\nWhile Loop (Countdown):")
    count = 5
    while count > 0:
        print(count)
        count -= 1

    # ---------- Functions ----------
    print("\nFunctions:")
    print("Square of 4:", square(4))
    print("Sum of 5 and 7:", add(5, 7))
    greet(name)


def square(num):
    return num * num


def add(x, y):
    return x + y


def greet(person_name):
    print(f"Hello, {person_name}! Keep learning Python basics.")


if __name__ == "__main__":
    main()