import pytest

from main import get_item_counts

run_cases = [
    pytest.param(
        ["Bread", "Potion", "Shortsword", "Bread"], (1, 2, 1), id="mixed-items"
    ),
    pytest.param(
        ["Potion", "Potion", "Shortsword", "Buckler", "Iron Mace"],
        (2, 0, 1),
        id="no-bread",
    ),
]

submit_cases = [
    pytest.param([], (0, 0, 0), marks=pytest.mark.submit, id="empty"),
    pytest.param(
        [
            "Potion",
            "Leather Scraps",
            "Bread",
            "Iron Ore",
            "Light Leather",
            "Bread",
            "Shortsword",
            "Longsword",
            "Ironwood Branch",
            "Shortsword",
            "Shortsword",
        ],
        (1, 2, 3),
        marks=pytest.mark.submit,
        id="large-inventory",
    ),
    pytest.param(
        ["Bread", "Bread", "Bread", "Bread"],
        (0, 4, 0),
        marks=pytest.mark.submit,
        id="only-bread",
    ),
    pytest.param(
        ["Shortsword", "Shortsword", "Shortsword", "Shortsword"],
        (0, 0, 4),
        marks=pytest.mark.submit,
        id="only-shortswords",
    ),
    pytest.param(["Potion"], (1, 0, 0), marks=pytest.mark.submit, id="single-potion"),
    pytest.param(
        ["Potion", "Bread", "Shortsword"],
        (1, 1, 1),
        marks=pytest.mark.submit,
        id="one-of-each",
    ),
]


@pytest.mark.parametrize(("items", "expected"), run_cases + submit_cases)
def test_get_item_counts(items, expected):
    print("\n---------------------------------")
    print(f"Inputs: {items}")
    result = get_item_counts(items)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    assert result == expected
