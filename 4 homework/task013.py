import unittest
from task011 import amount_of_newborn_people_prediction
import task012


class TestNewBornFunction(unittest.TestCase):

    def test_correct_res(self):
        self.assertEqual(amount_of_newborn_people_prediction(12, 12, 1), 182)

    # def test_wrong_datatype(self):
    #     with self.assertRaises(TypeError) as e:
    #         amount_of_newborn_people_prediction(12, 18, 'pesok')
    #     #self.assertTrue('Wrong data type!!!' in str(e.exception))


class TestCalculate(unittest.TestCase):

    def test_calculate_function(self):
        self.assertEqual(task012.calculate(1,"+",1,"+",1,"+",1,"+",1), 5)

    def test_curried_calculate(self):
        self.assertEqual(task012.curried_calculate(1)("+")(2)("+")(3)("+")(2)("-")(1), 7)

    def test_calc_partial(self):
        self.assertEqual(task012.calculate_for_partial([1, 2, 3, 2, 1], ["+", "+", "+", "-"]), 7)

# я так и не поняла, как правильно сделать тест с TypeError :((
