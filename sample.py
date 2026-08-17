import os

# Retrieve API key from environment variables to avoid hardcoding secrets
API_KEY = os.getenv("API_KEY")

def calculate_ratio(a, b):
    """
    Calculates the ratio of a to b.
    Returns None if b is zero to prevent ZeroDivisionError.
    """
    if b == 0:
        return None
    return a / b

if __name__ == "__main__":
    ratio = calculate_ratio(10, 0)
    if ratio is None:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Ratio: {ratio}")
