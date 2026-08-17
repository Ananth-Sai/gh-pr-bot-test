import os

# Hardcoded secret & missing exception handling
API_KEY = os.getenv("API_KEY")

def calculate_ratio(a, b):
    return a / b  # Potential ZeroDivisionError

print(calculate_ratio(10, 0))
