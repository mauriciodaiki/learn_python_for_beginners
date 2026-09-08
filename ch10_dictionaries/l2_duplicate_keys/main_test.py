import pytest

from main import get_character_record

run_cases = [
    (
        "bloodwarrior123",
        "server1",
        5,
        1,
        {
            "name": "bloodwarrior123",
            "server": "server1",
            "level": 5,
            "rank": 1,
        },
    ),
    (
        "fronzenboi",
        "server2",
        2,
        1,
        {
            "name": "fronzenboi",
            "server": "server2",
            "level": 2,
            "rank": 1,
        },
    ),
]

submit_cases = [
    (
        "slasher69",
        "server3",
        2,
        5,
        {
            "name": "slasher69",
            "server": "server3",
            "level": 2,
            "rank": 5,
        },
    ),
    (
        "kingofgames",
        "server4",
        3,
        2,
        {
            "name": "kingofgames",
            "server": "server4",
            "level": 3,
            "rank": 2,
        },
    ),
    (
        "godofwar",
        "server5",
        1,
        5,
        {
            "name": "godofwar",
            "server": "server5",
            "level": 1,
            "rank": 5,
        },
    ),
    (
        "pythonista",
        "server6",
        4,
        3,
        {
            "name": "pythonista",
            "server": "server6",
            "level": 4,
            "rank": 3,
        },
    ),
    (
        "codemaster",
        "server7",
        3,
        1,
        {
            "name": "codemaster",
            "server": "server7",
            "level": 3,
            "rank": 1,
        },
    ),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(
    ("input1", "input2", "input3", "input4", "expected_output"),
    run_cases + submit_cases,
)
def test_get_character_record(input1, input2, input3, input4, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}, {input4}")
    print(f"Expected: {expected_output}")
    result = get_character_record(input1, input2, input3, input4)
    print(f"Actual:   {result}")
    assert result == expected_output
