import unittest

# The function we want to test
def add_numbers(a, b):
    return a + b

# Test case class for the add_numbers function
class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add_numbers(3, 4)
        self.assertEqual(result, 7)

    def test_add_negative_numbers(self):
        result = add_numbers(-2, -5)
        self.assertEqual(result, -7)

    def test_add_mixed_numbers(self):
        result = add_numbers(8, -3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
