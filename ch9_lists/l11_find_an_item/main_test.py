import pytest

from main import contains_leather_scraps

run_cases = [
    (["Potion", "Healing Potion", "Iron Breastplate", "Leather Scraps"], True),
    (["Potion", "Shortsword", "Buckler", "Iron Mace"], False),
]

submit_cases = [
    ([], False),
    (["Leather Scraps"], True),
    (["Potion", "Healing Potion"], False),
    (["Leather scraps"], False),
    (["Leather", "Scraps"], False),
    (["Potion", "Leather Scraps", "Healing Potion", "Iron Breastplate"], True),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_contains_leather_scraps(input1, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}")
    result = contains_leather_scraps(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
