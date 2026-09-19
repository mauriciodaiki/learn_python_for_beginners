import pytest
from main import join_strings

run_cases = [
    (["hello", "world"], "hello,world"),
    (["this", "list", "is", "so", "important"], "this,list,is,so,important"),
]

submit_cases = [
    pytest.param([], "", marks=pytest.mark.submit),
    pytest.param(
        ["zuck", "satya", "cook", "bezos"],
        "zuck,satya,cook,bezos",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        ["dota", "sc2", "overwatch", "diablo", "mtg"],
        "dota,sc2,overwatch,diablo,mtg",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("input_list", "expected"), run_cases + submit_cases)
def test_join_strings(input_list, expected):
    print("\n---------------------------------")
    print(f"Input: {input_list}")
    print()
    result = join_strings(input_list)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    assert result == expected
