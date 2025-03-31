import unittest
from main import check_pythagorean  

class TestPythagorean(unittest.TestCase):
    def test_valid_triplet(self):
        self.assertTrue(check_pythagorean(3, 4, 5))

    def test_invalid_triplet(self):
        self.assertFalse(check_pythagorean(3, 4, 6))

    def test_zero_values(self):
        self.assertFalse(check_pythagorean(0, 0, 0))

if __name__ == '__main__':
    unittest.main()
