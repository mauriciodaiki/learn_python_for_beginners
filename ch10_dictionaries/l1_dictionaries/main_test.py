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
            "id": "bloodwarrior123#server1",
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
            "id": "fronzenboi#server2",
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
            "id": "slasher69#server3",
        },
    ),
    (
        "icequeen",
        "server4",
        3,
        2,
        {
            "name": "icequeen",
            "server": "server4",
            "level": 3,
            "rank": 2,
            "id": "icequeen#server4",
        },
    ),
    (
        "shadowmaster",
        "server5",
        4,
        3,
        {
            "name": "shadowmaster",
            "server": "server5",
            "level": 4,
            "rank": 3,
            "id": "shadowmaster#server5",
        },
    ),
    (
        "silentslasher",
        "server6",
        5,
        4,
        {
            "name": "silentslasher",
            "server": "server6",
            "level": 5,
            "rank": 4,
            "id": "silentslasher#server6",
        },
    ),
    (
        "hypershadow",
        "server7",
        3,
        5,
        {
            "name": "hypershadow",
            "server": "server7",
            "level": 3,
            "rank": 5,
            "id": "hypershadow#server7",
        },
    ),
]

run_cases = [(index, *case) for index, case in enumerate(run_cases, 1)]
submit_cases = [
    pytest.param(index, *case, marks=pytest.mark.submit)
    for index, case in enumerate(submit_cases, len(run_cases) + 1)
]


@pytest.mark.parametrize(
    ("index", "name", "server", "level", "rank", "expected_output"),
    run_cases + submit_cases,
)
def test_get_character_record(index, name, server, level, rank, expected_output):
    print("\n---------------------------------")
    print(f"Test Case #{index}\n")
    failed = False
    try:
        result = get_character_record(name, server, level, rank)
        for key, value in expected_output.items():
            print(f"Expected: {key}: {value}")
            print(f"Actual:   {key}: {result[key]}\n")
            if result[key] != value:
                if type(result[key]) is not type(value):
                    print(f"'{key}' values are different types!")
                    print(
                        f"Expected '{key}' to be of type {type(value).__name__}, but got {type(result[key]).__name__}"
                    )
                print("Fail")
                failed = True
                break
        if not failed and result != expected_output:
            print("Result object is incorrect:")
            for key, value in result.items():
                print(f" * {key}: {value}")
            print("Fail")
            failed = True
        if not failed:
            print("Pass")
    except Exception as e:
        print(f"Exception: {e!s}")
        print("Fail")
        failed = True
    assert not failed
