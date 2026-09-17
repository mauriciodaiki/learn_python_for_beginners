import pytest
from main import get_unique_items

run_cases = [
    (
        ["Iron Sword", "Healing Potion", "Iron Sword"],
        {"Iron Sword", "Healing Potion"},
    ),
    (
        ["Leather Armor", "Mage Robe", "Leather Armor", "Mage Robe"],
        {"Leather Armor", "Mage Robe"},
    ),
]

submit_cases = [
    pytest.param(
        ["Gold Coin", "Silver Ring", "Gold Coin", "Torch"],
        {"Gold Coin", "Silver Ring", "Torch"},
        marks=pytest.mark.submit,
    ),
]

expected_annotations = {
    "inventory": list[str],
    "return": set[str],
}


@pytest.mark.parametrize(("inventory", "expected_items"), run_cases + submit_cases)
def test_get_unique_items(inventory, expected_items):
    print("\n---------------------------------")
    print(f"Inventory: {inventory}")
    print()

    actual_items = get_unique_items(inventory)

    print(f"Expected unique items: {expected_items}")
    print(f"Actual unique items:   {actual_items}")
    print()

    assert actual_items == expected_items

    for annotation_name, expected_type in expected_annotations.items():
        actual_type = get_unique_items.__annotations__.get(annotation_name)

        print(f"{annotation_name}: expected {expected_type}")
        print(f"{annotation_name}: actual {actual_type}")
        print()

        assert actual_type == expected_type
