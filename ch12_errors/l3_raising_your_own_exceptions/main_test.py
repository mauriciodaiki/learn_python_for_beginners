import pytest

from main import get_player_record

valid_cases = [
    pytest.param(1, {"name": "Slayer", "level": 128}, id="slayer"),
    pytest.param(3, {"name": "Saruman", "level": 4000}, id="saruman"),
    pytest.param(
        2,
        {"name": "Dorgoth", "level": 300},
        marks=pytest.mark.submit,
        id="dorgoth",
    ),
]

missing_player_cases = [
    pytest.param(4, id="missing-player"),
    pytest.param(5, marks=pytest.mark.submit, id="above-range"),
    pytest.param(0, marks=pytest.mark.submit, id="below-range"),
]


@pytest.mark.parametrize(("player_id", "expected"), valid_cases)
def test_get_player_record(player_id, expected):
    print("\n---------------------------------")
    print(f"Input: {player_id}")
    result = get_player_record(player_id)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    assert result == expected


@pytest.mark.parametrize("player_id", missing_player_cases)
def test_get_missing_player_record(player_id):
    print("\n---------------------------------")
    print(f"Input: {player_id}")
    expected = "player id not found"
    try:
        result = get_player_record(player_id)
    except Exception as error:
        result = error
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    assert isinstance(result, Exception)
    assert str(result) == expected
