def add(a, b):
            return a + b

def subtract(a, b):
            return a - b

def divide(a, b):
            return a / b

import unittest

class TestCalculator(unittest.TestCase):
            def test_add(self):
                            self.assertEqual(add(2, 3), 5)

            def test_subtract(self):
                            self.assertEqual(subtract(5, 3), 2)

            def test_divide(self):
                            self.assertEqual(divide(10, 0), 0)

        if __name__ == '__main__':
                    unittest.main()
