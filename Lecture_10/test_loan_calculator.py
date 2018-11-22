import pytest

from loan_calculator import loan_calculator as lc


@pytest.mark.parametrize('inputs, expected', [
    ([10_000, 10, 12], [879, 548, 10548]),
    ([100_000, 20, 36], [3716, 33776, 133776]),
])
def test_positive(inputs, expected):
    assert expected == lc(*inputs)


@pytest.mark.parametrize('inputs', [
    ([None, 10, 12]),
    ([10_000, None, 12]),
    ([10_000, 10, None]),
])
def test_inputs_are_None(inputs):
    with pytest.raises(ValueError):
        lc(*inputs)


@pytest.mark.parametrize('inputs', [
    ([-10_000, 10, 12]),
    ([10_000, -10, 12]),
    ([10_000, 10, -12]),
])
def test_inputs_are_negative(inputs):
    with pytest.raises(ValueError):
        lc(*inputs)


@pytest.mark.parametrize('inputs, expected', [
    ([1_000, 10, 6], [172, 32, 1032]),
    ([600_000, 32, 60], [20156, 609360, 1209360]),
])
def test_boundaries(inputs, expected):
    assert expected == lc(*inputs)


@pytest.mark.parametrize('inputs', [
    ([999, 10, 12]),
    ([1_000, 33, 12]),
    ([1_000, 10, 61]),
])
def test_fail_out_of_bondaries(inputs):
    with pytest.raises(ValueError):
        lc(*inputs)
