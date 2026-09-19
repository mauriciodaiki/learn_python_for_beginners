import pytest
from main import divide_list

run_cases = [
    ([6, 8, 10], 2, [3.0, 4.0, 5.0]),
    ([1, 2, 3, 4], 1, [1.0, 2.0, 3.0, 4.0]),
]

submit_cases = [
    pytest.param([15, 30, 45], 3, [5.0, 10.0, 15.0], marks=pytest.mark.submit),
    pytest.param([0], 1, [0.0], marks=pytest.mark.submit),
    pytest.param([27, 54, 81], 9, [3.0, 6.0, 9.0], marks=pytest.mark.submit),
    pytest.param(
        [100, 200, 300, 400],
        10,
        [10.0, 20.0, 30.0, 40.0],
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("input_list", "divisor", "expected"), run_cases + submit_cases
)
def test_divide_list(input_list, divisor, expected):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * List of numbers: {input_list}")
    print(f" * Divisor: {divisor}")
    result = divide_list(input_list, divisor)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    assert result == expected
