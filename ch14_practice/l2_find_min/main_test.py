import pytest
from main import find_min

run_cases = [
    ([-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7], -4),
    ([4, 3, 2, 1, 18, 1, 2, 3, 4, 5, 6, 7], 1),
]

submit_cases = [
    pytest.param(
        [43, 234, 65465, 234, 2343, 443, 2123, 8768],
        43,
        marks=pytest.mark.submit,
    ),
    pytest.param([0], 0, marks=pytest.mark.submit),
    pytest.param([], float("inf"), marks=pytest.mark.submit),
    pytest.param([-1, -2, -3], -3, marks=pytest.mark.submit),
    pytest.param([100, 200, 300], 100, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("input_list", "expected"), run_cases + submit_cases)
def test_find_min(input_list, expected):
    print("\n---------------------------------")
    print(f"Inputs: {input_list}")
    result = find_min(input_list)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    assert result == expected
