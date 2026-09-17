import pytest
from main import get_character_status

run_cases = [
    (
        "Gandalf",
        80,
        99.5,
        True,
        "Gandalf is level 80 with 99.5 HP, and can cast spells",
    ),
    (
        "Frodo",
        12,
        24.0,
        False,
        "Frodo is level 12 with 24.0 HP, and cannot cast spells",
    ),
]

submit_cases = [
    pytest.param(
        "Aragorn",
        45,
        82.5,
        False,
        "Aragorn is level 45 with 82.5 HP, and cannot cast spells",
        marks=pytest.mark.submit,
    ),
]

expected_annotations = {
    "name": str,
    "level": int,
    "health": float,
    "has_magic": bool,
}


@pytest.mark.parametrize(
    ("char_name", "char_level", "char_health", "has_magic", "expected_status"),
    run_cases + submit_cases,
)
def test_get_character_status(
    char_name, char_level, char_health, has_magic, expected_status
):
    print("\n---------------------------------")
    print(f"Inputs: {char_name}, {char_level}, {char_health}, {has_magic}")
    print()

    actual_status = get_character_status(char_name, char_level, char_health, has_magic)

    print(f"Expected status: {expected_status}")
    print(f"Actual status:   {actual_status}")
    print()

    assert actual_status == expected_status

    for param_name, expected_type in expected_annotations.items():
        actual_type = get_character_status.__annotations__.get(param_name)

        print(f"{param_name}: expected {expected_type.__name__}")
        print(f"{param_name}: actual {getattr(actual_type, '__name__', None)}")
        print()

        assert actual_type is expected_type
