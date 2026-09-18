import pytest
from main import get_reward_summary

run_cases = [
    (
        ["Master Key", "Jadeite Gwethdesuan"],
        {"Master Key": 1, "Jadeite Gwethdesuan": 3},
        ("Master Key", 4),
    ),
    (
        ["Poison Arrow", "Ruby-Hilted Dagger"],
        {"Poison Arrow": 30, "Ruby-Hilted Dagger": 2},
        ("Poison Arrow", 32),
    ),
]

submit_cases = [
    pytest.param(
        ["Torch", "Rope", "Iron Key"],
        {"Torch": 2, "Rope": 1, "Iron Key": 1},
        ("Torch", 4),
        marks=pytest.mark.submit,
    ),
]

expected_annotations = {
    "items": list[str],
    "item_counts": dict[str, int],
    "return": tuple[str, int],
}


@pytest.mark.parametrize(
    ("items", "item_counts", "expected_summary"), run_cases + submit_cases
)
def test_get_reward_summary(items, item_counts, expected_summary):
    print("\n---------------------------------")
    print(f"Items: {items}")
    print(f"Item counts: {item_counts}")
    print()

    actual_summary = get_reward_summary(items, item_counts)

    print(f"Expected summary: {expected_summary}")
    print(f"Actual summary:   {actual_summary}")
    print()

    assert actual_summary == expected_summary

    for annotation_name, expected_type in expected_annotations.items():
        actual_type = get_reward_summary.__annotations__.get(annotation_name)

        print(f"{annotation_name}: expected {expected_type}")
        print(f"{annotation_name}: actual {actual_type}")
        print()

        assert actual_type == expected_type
