import pytest
from main import get_item_count

run_cases = [
    ({"Wooden Arrow": 30, "Small Amethyst": 2}, "Small Amethyst", 2),
    ({"Torch": 5, "Rope": 2}, "Rope", 2),
]

submit_cases = [
    pytest.param(
        {"Arrow": 30, "Mana Crystal": 4},
        "Dragon Scale",
        0,
        marks=pytest.mark.submit,
    ),
]

expected_annotations = {"item_counts": dict[str, int], "item_name": str, "return": int}


@pytest.mark.parametrize(
    ("item_counts", "item_name", "expected_count"), run_cases + submit_cases
)
def test_get_item_count(item_counts, item_name, expected_count):
    print("\n---------------------------------")
    print(f"Item counts: {item_counts}")
    print(f"Item name: {item_name}")
    print()

    actual_count = get_item_count(item_counts, item_name)

    print(f"Expected count: {expected_count}")
    print(f"Actual count:   {actual_count}")
    print()

    assert actual_count == expected_count

    for annotation_name, expected_type in expected_annotations.items():
        actual_type = get_item_count.__annotations__.get(annotation_name)

        print(f"{annotation_name}: expected {expected_type}")
        print(f"{annotation_name}: actual {actual_type}")
        print()

        assert actual_type == expected_type
