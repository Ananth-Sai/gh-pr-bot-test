import os

API_KEY = os.getenv("API_KEY")

def greet(name="World"):
    """Prints a greeting message."""
    print(f"Hello, {name}!")

def calculate_ratio(a, b):
    """Calculates the ratio of a to b. Returns None if b is zero."""
    if b == 0:
        return None
    return a / b

if __name__ == "__main__":
    greet()
    ratio = calculate_ratio(10, 0)
    if ratio is None:
        print("Cannot divide by zero.")
    else:
        print(f"Ratio: {ratio}")
