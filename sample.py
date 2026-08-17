import os

API_KEY = os.getenv("API_KEY", "default-fallback-key")

def calculate_ratio(a, b):
    if b == 0:
        return None
    return a / b

if __name__ == "__main__":
    result = calculate_ratio(10, 0)
    print(result)
