import pytest

from main import get_last_index

run_cases = [
    (["Potion"], 0),
    (["Potion", "Iron Breastplate"], 1),
    (["Potion", "Iron Breastplate", "Bread", "Longsword"], 3),
]

submit_cases = [
    ([], -1),
    (["Single item"], 0),
    (["Shield", "Sword", "Bow", "Arrows", "Health Potion"], 4),
    (["Shield", "Sword", "Bow"], 2),
    (["Shield", "Sword"], 1),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_get_last_index(input1, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}")
    result = get_last_index(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
