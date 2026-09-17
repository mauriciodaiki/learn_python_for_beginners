import pytest
from main import get_item_description

run_cases = [
    (
        "Iron Sword",
        12,
        False,
        "Iron Sword deals 12 damage and has no magical properties",
    ),
    (
        "Crystal Staff",
        8,
        True,
        "Crystal Staff deals 8 damage and glows with arcane power",
    ),
]

submit_cases = [
    pytest.param(
        "Dragonbone Axe",
        25,
        True,
        "Dragonbone Axe deals 25 damage and glows with arcane power",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("item_name", "damage", "is_magical", "expected_description"),
    run_cases + submit_cases,
)
def test_get_item_description(item_name, damage, is_magical, expected_description):
    print("\n---------------------------------")
    print(f"Inputs: {item_name}, {damage}, {is_magical}")
    print()

    actual_description = get_item_description(item_name, damage, is_magical)

    print(f"Expected description: {expected_description}")
    print(f"Actual description:   {actual_description}")
    print()

    assert actual_description == expected_description

    expected_type = str
    actual_type = get_item_description.__annotations__.get("return")

    print(f"Expected return type hint: {expected_type.__name__}")
    print(f"Actual return type hint:   {getattr(actual_type, '__name__', None)}")
    print()

    assert actual_type is expected_type
