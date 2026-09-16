import pytest
from main import (
    __annotations__ as main_annotations,
)
from main import (
    character_health,
    character_level,
    character_name,
    has_magic,
)

run_cases = [
    ("character_name", character_name, "Gandalf", str),
    ("character_level", character_level, 80, int),
]

submit_cases = [
    pytest.param(
        "character_health",
        character_health,
        99.5,
        float,
        marks=pytest.mark.submit,
    ),
    pytest.param("has_magic", has_magic, True, bool, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("variable_name", "actual_value", "expected_value", "expected_type"),
    run_cases + submit_cases,
)
def test_basic_type(variable_name, actual_value, expected_value, expected_type):
    print("\n---------------------------------")
    print(f"Checking {variable_name}")
    print()

    actual_type = main_annotations.get(variable_name)

    print(f"Expected value: {expected_value}")
    print(f"Actual value:   {actual_value}")
    print()

    assert actual_value == expected_value

    expected_name = expected_type.__name__
    actual_name = getattr(actual_type, "__name__", None)

    print(f"Expected type hint: {expected_name}")
    print(f"Actual type hint:   {actual_name}")
    print()

    assert actual_type is expected_type
