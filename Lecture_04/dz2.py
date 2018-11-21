"""
ДЗ №2: калькулятор вкладов


http://www.banki.ru/services/calculators/deposits/
срок размещения в месяцах


# Граничные условия:
1 <= deposit <= 100_000_000
1 <= term_in_months <= 60
0.01 <= rate <= 99.9
"""

import unittest


def deposit_calculator(deposit, term_in_months, rate):
    if not (1 <= deposit <= 100_000_000 and
            1 <= term_in_months <= 60 and
            0.01 <= rate <= 99.9):
        return None
    
    return deposit + deposit * term_in_months * rate/12/100


class TestDepositCalculator(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(deposit_calculator(100_000, 12, 8), 108_000)
        self.assertEqual(deposit_calculator(100_000, 12, 8), 108_000)
    
    def test_negative_or_zero_values_given(self):
        self.assertEqual(deposit_calculator(0, 12, 8), None)
        self.assertEqual(deposit_calculator(-100_000, 12, 8), None)

        self.assertEqual(deposit_calculator(100_000, 0, 8), None)
        self.assertEqual(deposit_calculator(100_000, -12, 8), None)

        self.assertEqual(deposit_calculator(100_000, 12, 0), None)
        self.assertEqual(deposit_calculator(100_000, 12, -8), None)
        

if __name__ == '__main__':
    unittest.main()