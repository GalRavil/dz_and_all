import pytest
from deposit_calc import deposit_calculator as dc


def test_positive():
    assert dc(100_000, 12, 8) == 108_000
    assert dc(1000, 18, 50) == 1750


@pytest.mark.parametrize('input, expected', [
    ([0, 12, 8], None),
    ([-100_000, 12, 8], None),

    ([100_000, 0, 8], None),
    ([100_000, -12, 8], None),

    ([100_000, 12, 0], None),
    ([100_000, 0, -8], None),
])
def test_negative_or_zero_values_given(input, expected):
    assert expected == dc(*input)


@pytest.mark.parametrize('input, expected', [
    ([1, 12, 10], 1.1),
    ([100_000_000, 12, 10], 110_000_000),

    ([100_000, 1, 10], 100833.33),
    ([100_000, 60, 10], 150_000),

    ([100_000, 12, 0.01], 100_010),
    ([100_000, 12, 99.9], 199_900),
])
def test_boundaries(input, expected):
    assert expected == dc(*input)
