import pytest

from main import find_missing_ids

run_cases = [
    ([1, 1, 1, 2, 2, 2, 3], [1, 2], {3}),
    ([1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 9, 10], [1, 2, 2, 3, 4, 5, 6, 7, 8], {9, 10}),
]

submit_cases = [
    ([], [], set()),
    ([1, 1, 1], [], {1}),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], set()),
    ([1, 1, 2, 2, 3, 3], [1, 2, 3], set()),
    ([1, 2, 3, 4, 5], [1, 2, 3], {4, 5}),
    ([1, 2, 3, 4, 5], [1, 3, 5], {2, 4}),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(
    ("input1", "input2", "expected_output"), run_cases + submit_cases
)
def test_find_missing_ids(input1, input2, expected_output):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" - first_ids:  {input1}")
    print(f" - second_ids: {input2}")
    result = find_missing_ids(input1, input2)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
