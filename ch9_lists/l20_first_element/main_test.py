import pytest

from main import get_first_item

run_cases = [
    ([1, 2], 1),
    (["Healing Potion"], "Healing Potion"),
    ([], "ERROR"),
]

submit_cases = [
    (["Iron Ore", "Iron Bar", "Scimitar"], "Iron Ore"),
    (["Apple", "Banana", "Cherry"], "Apple"),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3]),
    ([False, True, False], False),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_get_first_item(input1, expected_output):
    print("\n---------------------------------")
    print(f"Input: {input1}")
    result = get_first_item(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
