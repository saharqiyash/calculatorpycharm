
import sys
import os
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), '../'))

import unittest
from calculator.calculator import Calculator
from csv_reader.csv_reader import CsvReader
from pprint import pprint

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    # Unit test 1
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    # Unit test 2
    def test_subtraction(self):
        test_data = CsvReader( BASE_DIR + "/data/UnitTestSubtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    # Unit test 3
    def test_addition(self):
        test_data = CsvReader(BASE_DIR + "/data/UnitTestAddition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    # Unit test 4
    def test_multiplication(self):
        test_data = CsvReader(BASE_DIR + "/data/UnitTestMultiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    # Unit test 5
    def test_division(self):
        test_data = CsvReader(BASE_DIR + "/data/UnitTestDivision.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(round(self.calculator.divide(row['Value 1'], row['Value 2'])), round(result))
            self.assertEqual(round(self.calculator.result), round(result))

    # Unit test 6
    def test_square(self):
        test_data = CsvReader(BASE_DIR + "/data/UnitTestSquare.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    # Unit test 7
    def test_square_root(self):
        test_data = CsvReader(BASE_DIR + "/data/UnitTestSquareRoot.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(round(self.calculator.squareroot(row['Value 1'])), round(result))
            self.assertEqual(round(self.calculator.result), round(result))

if __name__ == '__main__':
    # test_data = CsvReader(BASE_DIR + "/data/UnitTestSubtraction.csv").data
    # pprint(test_data)

    unittest.main()