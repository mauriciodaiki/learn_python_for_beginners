import pytest

from main import check_ingredient_match

run_cases = [
    pytest.param(
        [
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
        ],
        [
            "Elf Dust",
            "Goblin Ear",
        ],
        (50.0, ["Mandrake Root", "Griffin Feather"]),
        id="half-match",
    ),
    pytest.param(
        [
            "Dragon Scale",
            "Unicorn Hair",
            "Phoenix Feather",
            "Troll Tusk",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
        ],
        [
            "Dragon Scale",
            "Phoenix Feather",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
        ],
        (75.0, ["Unicorn Hair", "Troll Tusk"]),
        id="three-quarter-match",
    ),
]

submit_cases = [
    pytest.param(
        [
            "Dragon Scale",
            "Phoenix Feather",
            "Troll Tusk",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
            "Unicorn Hair",
        ],
        [
            "Goblin Ear",
            "Elf Dust",
            "Griffin Feather",
            "Mermaid Tear",
            "Goblin Ear",
            "Phoenix Feather",
            "Troll Tusk",
            "Unicorn Hair",
        ],
        (
            75.0,
            [
                "Dragon Scale",
                "Mandrake Root",
            ],
        ),
        marks=pytest.mark.submit,
        id="duplicate-inventory-item",
    ),
    pytest.param(
        [
            "Orc Tears",
            "Ogre Ear",
            "Goblin Giggles",
            "Witch Broom",
            "Giant Toenail Clipping",
            "Centipede Foot",
            "Dog Hair",
            "Bald Eagle Dandruff",
        ],
        [
            "Unicorn Hair",
            "Dragon Scale",
            "Phoenix Feather",
            "Troll Tusk",
            "Griffin Feather",
            "Mandrake Root",
            "Goblin Ear",
            "Bald Eagle Dandruff",
        ],
        (
            12.5,
            [
                "Orc Tears",
                "Ogre Ear",
                "Goblin Giggles",
                "Witch Broom",
                "Giant Toenail Clipping",
                "Centipede Foot",
                "Dog Hair",
            ],
        ),
        marks=pytest.mark.submit,
        id="single-match",
    ),
]


@pytest.mark.parametrize(("recipe", "inventory", "expected"), run_cases + submit_cases)
def test_check_ingredient_match(recipe, inventory, expected):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" - Recipe: {recipe}")
    print(f" - Inventory: {inventory}")
    print()
    result = check_ingredient_match(recipe, inventory)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")

    assert isinstance(result, (tuple, list)) and len(result) == 2
    percentage, missing = result
    expected_percentage, expected_missing = expected

    assert percentage == expected_percentage
    assert sorted(missing) == sorted(expected_missing)
