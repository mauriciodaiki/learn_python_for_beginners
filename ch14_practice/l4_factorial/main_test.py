import pytest
from main import factorial

run_cases = [
    (0, 1),
    (4, 24),
]

submit_cases = [
    pytest.param(1, 1, marks=pytest.mark.submit),
    pytest.param(5, 120, marks=pytest.mark.submit),
    pytest.param(7, 5040, marks=pytest.mark.submit),
    pytest.param(9, 362880, marks=pytest.mark.submit),
    pytest.param(13, 6227020800, marks=pytest.mark.submit),
    pytest.param(15, 1307674368000, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("n", "expected"), run_cases + submit_cases)
def test_factorial(n, expected):
    print("\n---------------------------------")
    print(f"Input: {n}")
    print()
    result = factorial(n)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    assert result == expected
