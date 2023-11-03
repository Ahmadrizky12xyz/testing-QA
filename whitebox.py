# Function to calculate the sum of two numbers
def add_numbers(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        result = a + b
        return result
    else:
        raise ValueError("Both input values must be numbers")

# Test cases for the add_numbers function


def test_add_numbers():
    # Positive test cases
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0

    # Negative test cases
    try:
        add_numbers("2", 3)  # This should raise a ValueError
        print("Test case failed: String input not detected")
    except ValueError:
        print("Test case passed: String input detected")

    try:
        add_numbers(2, "3")  # This should raise a ValueError
        print("Test case failed: String input not detected")
    except ValueError:
        print("Test case passed: String input detected")


if __name__ == "__main__":
    test_add_numbers()
