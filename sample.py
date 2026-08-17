import os

# Hardcoded secret & missing exception handling
API_KEY = os.getenv("API_KEY")

def calculate_ratio(a, b):
def calculate_ratio(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b

print(calculate_ratio(10, 0))
