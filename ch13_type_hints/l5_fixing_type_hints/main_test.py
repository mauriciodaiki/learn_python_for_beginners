import pytest
from main import get_greeting

run_cases = [
    ("Gandalf", "Welcome to Fantasy Quest, Gandalf!"),
    ("Frodo", "Welcome to Fantasy Quest, Frodo!"),
]

submit_cases = [
    pytest.param(
        "Aragorn",
        "Welcome to Fantasy Quest, Aragorn!",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("player_name", "expected_greeting"), run_cases + submit_cases)
def test_get_greeting(player_name, expected_greeting):
    print("\n---------------------------------")
    print(f"Input: {player_name}")
    print()

    actual_greeting = get_greeting(player_name)

    print(f"Expected greeting: {expected_greeting}")
    print(f"Actual greeting:   {actual_greeting}")
    print()

    assert actual_greeting == expected_greeting

    expected_type = str
    actual_type = get_greeting.__annotations__.get("return")

    print(f"Expected return type hint: {expected_type.__name__}")
    print(f"Actual return type hint:   {getattr(actual_type, '__name__', None)}")
    print()

    assert actual_type is expected_type
