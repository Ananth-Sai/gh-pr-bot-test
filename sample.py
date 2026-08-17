import os

# Retrieve API key from environment variables securely
API_KEY = os.getenv("API_KEY")

def greet(name="World"):
    """Prints a greeting message."""
    print(f"Hello, {name}!")

def calculate_ratio(a, b):
    """Calculates the ratio of a to b, handling division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return None

if __name__ == "__main__":
    greet()
    ratio = calculate_ratio(10, 0)
    if ratio is None:
        print("Calculation failed: Division by zero.")
    else:
        print(f"Ratio: {ratio}")
