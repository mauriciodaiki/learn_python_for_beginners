import pytest
from main import number_sum

run_cases = [
    (3, 6),
    (5, 15),
]

submit_cases = [
    pytest.param(1, 1, marks=pytest.mark.submit),
    pytest.param(18, 171, marks=pytest.mark.submit),
    pytest.param(0, 0, marks=pytest.mark.submit),
    pytest.param(227, 25878, marks=pytest.mark.submit),
    pytest.param(100, 5050, marks=pytest.mark.submit),
    pytest.param(500, 125250, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("n", "expected"), run_cases + submit_cases)
def test_number_sum(n, expected):
    print("\n---------------------------------")
    print(f"Inputs: {n}")
    result = number_sum(n)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    assert result == expected
