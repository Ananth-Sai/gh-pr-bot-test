def add(a: int | float, b: int | float) -> int | float:
    """Returns the sum of two numbers."""
    return a + b


def multiply(a: int | float, b: int | float) -> int | float:
    """Returns the product of two numbers."""
    return a * b


if __name__ == "__main__":
    result = add(10, 20)
    print(f"Result: {result}")
