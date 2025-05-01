import unittest 
import operations

class Test(unittest.TestCase):
    def test_success_positive(self):
        self.assertEqual(operations.add(1, 1), 2)
        self.assertEqual(operations.add(2, 3), 5)
    def test_success_negative(self):
        self.assertEqual(operations.add(-1, -1), -2)
        self.assertEqual(operations.add(-2, -3), -5)
    def test_success_zero(self):
        self.assertEqual(operations.add(0, 0), 0)
        self.assertEqual(operations.add(0, 1), 1)
    def test_success_float(self):
        self.assertEqual(operations.add(1.5, 0.5), 2.0)
        self.assertEqual(operations.add(2.5, 3.5), 6.0)
    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            operations.add("1", 1)
        with self.assertRaises(TypeError):
            operations.add(1, "1")

if __name__ == '__main__':
    unittest.main()