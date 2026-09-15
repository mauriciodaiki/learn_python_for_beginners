import pytest
from main import process_player_record

run_cases = [
    (0, {"name": "Slayer", "level": 128}),
    (1, {"name": "Dorgoth", "level": 300}),
    (3, "index is too high"),
    (-1, "negative ids not allowed"),
]

submit_cases = [
    pytest.param(2, {"name": "Saruman", "level": 4000}, marks=pytest.mark.submit),
    pytest.param(10, "index is too high", marks=pytest.mark.submit),
    pytest.param(-5, "negative ids not allowed", marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("player_id", "expected"), run_cases + submit_cases)
def test_process_player_record(player_id, expected):
    print("\n---------------------------------")
    print(f"Inputs: {player_id}")
    result = process_player_record(player_id)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    if isinstance(result, Exception):
        result = str(result)
    assert result == expected
