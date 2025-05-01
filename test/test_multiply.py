import unittest 
import operations

class Test(unittest.TestCase):
    def test_success_positive(self):
        self.assertEqual(operations.multiply(2, 3), 6)
        self.assertEqual(operations.multiply(4, 5), 20)
    def test_success_negative(self):
        self.assertEqual(operations.multiply(-2, -3), 6)
        self.assertEqual(operations.multiply(-4, -5), 20)
    def test_success_zero(self):
        self.assertEqual(operations.multiply(0, 0), 0)
        self.assertEqual(operations.multiply(0, 5), 0)
    def test_success_float(self):
        self.assertEqual(operations.multiply(1.5, 2), 3.0)
        self.assertEqual(operations.multiply(2.5, 4), 10.0)
    def test_signal(self):
        self.assertEqual(operations.multiply(1, 1), 1)
        self.assertEqual(operations.multiply(-1, -1), 1)
        self.assertEqual(operations.multiply(-1, 1), -1)
        self.assertEqual(operations.multiply(1, -1), -1)

if __name__ == '__main__':
    unittest.main()