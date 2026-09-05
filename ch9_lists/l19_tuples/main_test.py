import pytest

from main import get_heroes

run_cases = [
    (
        [
            (
                "Glorfindel",
                2093,
                True,
            ),
            (
                "Gandalf",
                1054,
                False,
            ),
            (
                "Gimli",
                389,
                False,
            ),
            (
                "Aragorn",
                87,
                False,
            ),
        ]
    ),
]


@pytest.mark.parametrize("expected_output", run_cases)
def test_get_heroes(expected_output):
    print("\n---------------------------------")
    result = get_heroes()
    if not isinstance(result, list):
        print("Expected result to be a list")
    assert isinstance(result, list)

    passed = True
    for i, hero in enumerate(expected_output):
        print(f"Expected: {hero} at index {i}")
        if i >= len(result):
            print(f"Actual: None at index {i}")
            print("Fail")
            passed = False
            continue
        print(f"Actual: {result[i]} at index {i}")
        if hero != result[i]:
            print("Fail")
            passed = False
        else:
            print("Pass")
    assert passed
