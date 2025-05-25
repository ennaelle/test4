import unittest
from my_app.ui import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 4), 7)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -5), -7)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 5), 4)

if __name__ == "__main__":
    unittest.main()
