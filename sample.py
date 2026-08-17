def calculate_ratio(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b


def greet(name="World"):
    return f"Hello, {name}!"


if __name__ == "__main__":
    try:
        print(calculate_ratio(10, 2))
    except ValueError as e:
        print(f"Error: {e}")

    print(greet())
