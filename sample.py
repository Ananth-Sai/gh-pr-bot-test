def calculate_ratio(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b

try:
    print(calculate_ratio(10, 0))
except ValueError as e:
    print(f"Error: {e}")
