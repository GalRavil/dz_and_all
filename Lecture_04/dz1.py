""" ДЗ №1: кэшбэк по карте

Напишите функцию, которая расчитывает кэшбэк по карте:

В зависимости от категории покупки кэшбэк может быть выше или ниже:
• за обычные покупки банк начислит 1%
• за покупки в категориях повышенного кэшбэка — 5%
• за покупки по спецпредложениям — 30%

Не забудьте написать DocTest'ы

"""

import unittest


# cashback types
usual = 1
increased = 5
special = 30


def calculate_cashback(money_spend, cashback_type=usual):
    if money_spend <= 0:
        raise ValueError('The amount of money spent shold be more than 0.00$')
    return money_spend * cashback_type / 100

       


class TestCalculateCashback(unittest.TestCase):
    def test_usual_cashback(self):
        self.assertEqual(calculate_cashback(1000), 10)
        self.assertEqual(calculate_cashback(1000, cashback_type=usual), 10)
    
    def test_increased_cashback(self):
        self.assertEqual(calculate_cashback(1000, cashback_type=increased), 50)
    
    def test_special_cashback(self):
        self.assertEqual(calculate_cashback(1000, cashback_type=special), 300)

    def test_negative_or_zero_money_spend(self):
        # with self.assertRaises(ValueError): calculate_cashback(-1000)
        self.assertRaises(ValueError, lambda: calculate_cashback(-1000))
        self.assertRaises(ValueError, lambda: calculate_cashback(0))
        

if __name__ == '__main__':
    unittest.main()