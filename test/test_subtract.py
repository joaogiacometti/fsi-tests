import unittest 
import operations

class Test(unittest.TestCase):
    def test_success_positive(self):
        self.assertEqual(operations.subtract(3, 1), 2)
        self.assertEqual(operations.subtract(5, 3), 2)
    def test_success_negative(self):
        self.assertEqual(operations.subtract(-1, -1), 0)
        self.assertEqual(operations.subtract(-3, -1), -2)
    def test_success_zero(self):
        self.assertEqual(operations.subtract(0, 0), 0)
        self.assertEqual(operations.subtract(0, 1), -1)
    def test_success_float(self):
        self.assertEqual(operations.subtract(1.5, 0.5), 1.0)
        self.assertEqual(operations.subtract(2.5, 1.5), 1.0)

if __name__ == '__main__':
    unittest.main()