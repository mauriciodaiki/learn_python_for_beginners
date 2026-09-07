import pytest

from main import get_even_and_odd_teams

run_cases = [
    (
        [
            "Harry",
            "Hermione",
            "Ron",
            "Ginny",
            "Fred",
            "Neville",
            "Draco",
            "Luna",
            "Cho",
            "Gregory",
            "Lee",
            "Michael",
            "Lavender",
            "Frank",
            "Anthony",
            "Allan",
        ],
        (
            ["Harry", "Ron", "Fred", "Draco", "Cho", "Lee", "Lavender", "Anthony"],
            [
                "Hermione",
                "Ginny",
                "Neville",
                "Luna",
                "Gregory",
                "Michael",
                "Frank",
                "Allan",
            ],
        ),
    ),
    (["Mike", "Walter", "Skyler", "Tuco"], (["Mike", "Skyler"], ["Walter", "Tuco"])),
]

submit_cases = [
    (["Alice", "Bob", "Charlie", "David"], (["Alice", "Charlie"], ["Bob", "David"])),
    ([], ([], [])),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_get_even_and_odd_teams(input1, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}")
    result = get_even_and_odd_teams(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
