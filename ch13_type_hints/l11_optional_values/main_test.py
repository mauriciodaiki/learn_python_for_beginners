import pytest
from main import summon_mount

run_cases = [
    (True, 100, "Battle Horse"),
    (False, 67, None),
]

submit_cases = [
    pytest.param(True, 800, None, marks=pytest.mark.submit),
    pytest.param(True, 420, "Battle Horse", marks=pytest.mark.submit),
]

expected_annotations = {
    "has_mount": bool,
    "distance": int,
    "return": str | None,
}


@pytest.mark.parametrize(
    ("has_mount", "distance", "expected_mount"), run_cases + submit_cases
)
def test_summon_mount(has_mount, distance, expected_mount):
    print("\n---------------------------------")
    print(f"Has mount: {has_mount}")
    print(f"Distance: {distance}")
    print()

    actual_mount = summon_mount(has_mount, distance)

    print(f"Expected mount: {expected_mount}")
    print(f"Actual mount:   {actual_mount}")
    print()

    assert actual_mount == expected_mount

    for annotation_name, expected_type in expected_annotations.items():
        actual_type = summon_mount.__annotations__.get(annotation_name)

        print(f"{annotation_name}: expected {expected_type}")
        print(f"{annotation_name}: actual {actual_type}")
        print()

        assert actual_type == expected_type
