import pytest

from main import is_top_weapon

run_cases = [
    ("sword of justice", True),
    ("bronze mace", False),
    ("sword of slashing", True),
]

submit_cases = [
    ("", False),
    ("great axe", True),
    ("silver bow", True),
    ("golden spear", False),
    ("spiked knuckles", True),
    ("spellbook", True),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_is_top_weapon(input1, expected_output):
    print("\n---------------------------------")
    print("Input:")
    print(f" * Weapon: {input1}")
    result = is_top_weapon(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
