"""
ДЗ №3: калькулятор кредитов

Опустить время

# Граничных условия
1000 <= credit_amount <= 600_000
10 <= rate <= 32
6 <= term_in_months <= 60
"""
import unittest


def loan_calculator(credit_amount, rate, term_in_months):
    """
    http://www.banki.ru/wikibank/annuitetnyie_plateji_po_kreditu/
    http://www.banki.ru/wikibank/raschet_annuitetnogo_plateja/
    """

    if credit_amount == None or rate == None or term_in_months ==  None:
        raise ValueError('Fill in all the data')
    
    
    if not (1000 <= credit_amount <= 600_000 and 
        10 <= rate <= 32 and 
        6 <= term_in_months <= 60):    
        raise ValueError('Loan conditions do not match.')
    
    # i -> monthly_interest_rate
    i = rate / 12 / 100

    # K -> annuity_ratio
    # n -> term_in_months
    n = term_in_months
    K = (i * (1 + i)**n) / ((1+i)**n - 1)

    # A -> monthly annuity payment
    # s -> credit ammount
    S = credit_amount
    A = K * S

    monthly_annuity_payment = int(round(A))
    entire_payment = monthly_annuity_payment * term_in_months
    credit_overpayment = entire_payment - credit_amount

    return [
        monthly_annuity_payment,
        credit_overpayment,
        entire_payment
    ]



class TestCreditCalculator(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(
            loan_calculator(10_000, 10, 12), [879, 548, 10548])
        self.assertEqual(
            loan_calculator(100_000, 20, 36), [3716, 33776, 133776])

    def test_inputs_are_None(self):
        self.assertRaises(ValueError, lambda: loan_calculator(None, 10, 12))
        self.assertRaises(ValueError, lambda: loan_calculator(10_000, None, 12))
        self.assertRaises(ValueError, lambda: loan_calculator(10_000, 10, None))

    def test_inputs_are_negative(self):
        self.assertRaises(ValueError, lambda: loan_calculator(-10_000, 10, 12))
        self.assertRaises(ValueError, lambda: loan_calculator(10_000, -10, 12))
        self.assertRaises(ValueError, lambda: loan_calculator(10_000, 10, -12))
    
    def test_boundaries(self):
        self.assertEqual(loan_calculator(1_000, 10, 6), [172, 32, 1032])
        self.assertEqual(loan_calculator(600_000, 32, 60), [20156, 609360, 1209360])
        
        self.assertRaises(ValueError, lambda: loan_calculator(999, 10, 12))
        self.assertRaises(ValueError, lambda: loan_calculator(1_000, 33, 12))
        self.assertRaises(ValueError, lambda: loan_calculator(1_000, 10, 61))



if __name__ == '__main__':
    unittest.main()
