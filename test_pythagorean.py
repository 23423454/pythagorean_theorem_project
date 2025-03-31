import unittest
from main import check_pythagorean

class TestPythagoreanTheorem(unittest.TestCase):
    def test_pythagorean_true(self):
        self.assertTrue(check_pythagorean(3, 4, 5))
    
    def test_pythagorean_false(self):
        self.assertFalse(check_pythagorean(5, 5, 10))

    def test_pythagorean_another_true(self):
        self.assertTrue(check_pythagorean(6, 8, 10))

if __name__ == '__main__':
    unittest.main()
