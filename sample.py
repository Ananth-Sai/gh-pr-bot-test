import os

# Retrieve API key from environment variables to avoid hardcoding secrets
API_KEY = os.getenv("OPENAI_API_KEY")

def greet(name: str = "World") -> None:
    """Prints a greeting message."""
    print(f"Hello, {name}!")

def calculate_ratio(a: float, b: float) -> float | None:
    """Calculates the ratio of a to b, handling division by zero safely."""
    try:
        return a / b
    except ZeroDivisionError:
        return None

if __name__ == "__main__":
    greet()
    
    result = calculate_ratio(10, 0)
    if result is None:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Ratio: {result}")
