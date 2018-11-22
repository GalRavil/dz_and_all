"""
ДЗ №2: калькулятор вкладов


http://www.banki.ru/services/calculators/deposits/

срок размещения в месяцах

# Граничные условия:
1 <= deposit <= 100_000_000
1 <= term_in_months <= 60
0.01 <= rate <= 99.9
"""

def deposit_calculator(deposit, term_in_months, rate):
    if not (1 <= deposit <= 100_000_000 and
            1 <= term_in_months <= 60 and
            0.01 <= rate <= 99.9):
        return None
    
    res = deposit + deposit * term_in_months * rate/12/100
    return round(res, 2)
