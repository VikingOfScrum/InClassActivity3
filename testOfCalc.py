import unittest
import calc

class testCases(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(calc.addition(5, 5), 10)
        self.assertEqual(calc.addition(-3, 5), 2)
        self.assertEqual(calc.subtraction(5, 5), 0)
        self.assertEqual(calc.subtraction(-5, 3), -8)
        self.assertEqual(calc.mutliplication(5, 3), 15)
        self.assertEqual(calc.mutliplication(-5, 3), -15)
        self.assertEqual(calc.division(15, 3), 5)
        self.assertEqual(calc.division(-15, 3), -5)
class testCasesFail(unittest.TestCase):
    def test_of_numbers(self):
        self.assertNotEqual(calc.addition(5, 5), 11)
        self.assertNotEqual(calc.subtraction(5, 5), 5)
        self.assertNotEqual(calc.mutliplication(5, 3), 12)
        self.assertNotEqual(calc.division(15, 3), 5) #should fail on this line
if __name__ == '__main__':
    unittest.main(verbosity=2)