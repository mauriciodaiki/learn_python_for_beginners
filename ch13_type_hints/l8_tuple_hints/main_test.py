import pytest
from main import get_loot_drop

run_cases = [
    (14, ("Emerald Brome", 1)),
    (3, ("Smokestone Chip", 3)),
]

submit_cases = [
    pytest.param(40, ("Emerald Brome", 1), marks=pytest.mark.submit),
    pytest.param(10, ("Smokestone Chip", 3), marks=pytest.mark.submit),
]

expected_annotations = {
    "enemy_level": int,
    "return": tuple[str, int],
}


@pytest.mark.parametrize(("enemy_level", "expected_drop"), run_cases + submit_cases)
def test_get_loot_drop(enemy_level, expected_drop):
    print("\n---------------------------------")
    print(f"Enemy level: {enemy_level}")
    print()

    actual_drop = get_loot_drop(enemy_level)

    print(f"Expected drop: {expected_drop}")
    print(f"Actual drop:   {actual_drop}")
    print()

    assert actual_drop == expected_drop

    for annotation_name, expected_type in expected_annotations.items():
        actual_type = get_loot_drop.__annotations__.get(annotation_name)

        print(f"{annotation_name}: expected {expected_type}")
        print(f"{annotation_name}: actual {actual_type}")
        print()

        assert actual_type == expected_type
