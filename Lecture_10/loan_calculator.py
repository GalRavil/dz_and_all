"""
ДЗ №3: калькулятор кредитов

Опустить время

# Граничных условия
1000 <= credit_amount <= 600_000
10 <= rate <= 32
6 <= term_in_months <= 60
"""

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
