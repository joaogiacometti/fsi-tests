import unittest 
import operations

class Test(unittest.TestCase):
    def test_success_positive(self):
        self.assertEqual(operations.divide(4, 2), 2)
        self.assertEqual(operations.divide(10, 5), 2)
    def test_success_negative(self):
        self.assertEqual(operations.divide(-4, -2), 2)
        self.assertEqual(operations.divide(-10, -5), 2)
    def test_error_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            operations.perform_operation(1, 0, '/')
    def test_success_float(self):
        self.assertAlmostEqual(operations.divide(5.0, 2.0), 2.5)
        self.assertAlmostEqual(operations.divide(7.5, 3.0), 2.5)

if __name__ == '__main__':
    unittest.main()