import pytest

from main import smelt_ore

run_cases = [
    (
        ["Potion", "Iron Bar", "Iron Sword", "Leather Armor"],
        ["Potion", "Iron Bar", "Iron Sword", "Leather Armor"],
    ),
    ([None, None, None, None], [None, None, None, None]),
    (["Potion", "Iron Ore", None, None], ["Potion", "Iron Bar", None, None]),
]

submit_cases = [
    (
        [None, "Iron Ore", None, "Leather Armor"],
        [None, "Iron Bar", None, "Leather Armor"],
    ),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_smelt_ore(input1, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}")
    result = smelt_ore(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
