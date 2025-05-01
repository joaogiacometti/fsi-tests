import unittest 
import operations

class Test(unittest.TestCase):
    def test_success_add(self):
        self.assertEqual(operations.perform_operation(1, 1, '+'), 2)
        self.assertEqual(operations.perform_operation(1, 1, 'add'), 2)
    def test_success_subtract(self):
        self.assertEqual(operations.perform_operation(2, 1, '-'), 1)
        self.assertEqual(operations.perform_operation(2, 1, 'subtract'), 1)
    def test_success_multiply(self):
        self.assertEqual(operations.perform_operation(2, 3, '*'), 6)
        self.assertEqual(operations.perform_operation(2, 3, 'multiply'), 6)
    def test_success_divide(self):
        self.assertEqual(operations.perform_operation(4, 2, '/'), 2)
        self.assertEqual(operations.perform_operation(4, 2, 'divide'), 2)
    def test_error_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            operations.perform_operation(1, 0, '/')
        with self.assertRaises(ZeroDivisionError):
            operations.perform_operation(1, 0, 'divide')
    def test_error_invalid_operation(self):
        with self.assertRaises(ValueError):
            operations.perform_operation(1, 1, 'invalid')
        with self.assertRaises(ValueError):
            operations.perform_operation(1, 1, 'invalid_operation')
    

if __name__ == '__main__':
    unittest.main()