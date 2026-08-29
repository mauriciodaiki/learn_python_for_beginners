import pytest

from main import get_odd_numbers

run_cases = [(10, [1, 3, 5, 7, 9]), (20, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])]

submit_cases = [
    (0, []),
    (1, []),
    (2, [1]),
    (300, [i for i in range(1, 300, 2)]),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_get_odd_numbers(input1, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}")
    result = get_odd_numbers(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
