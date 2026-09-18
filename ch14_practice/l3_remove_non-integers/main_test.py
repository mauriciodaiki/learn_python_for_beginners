import pytest
from main import remove_nonints

run_cases = [
    (["200", 300, 2, False, "otherstring", 6], [300, 2, 6]),
    ([True, 300, 2, False, "otherstring", 76, 86, "morestrings"], [300, 2, 76, 86]),
]

submit_cases = [
    pytest.param(
        [300, 300, 2, False, "otherstring", 6, {}, 16],
        [300, 300, 2, 6, 16],
        marks=pytest.mark.submit,
    ),
    pytest.param(
        ["200", 300, 2, False, "something", 7, "something else"],
        [300, 2, 7],
        marks=pytest.mark.submit,
    ),
    pytest.param(["string", True, {}, []], [], marks=pytest.mark.submit),
    pytest.param([], [], marks=pytest.mark.submit),
    pytest.param([123, 456, 789], [123, 456, 789], marks=pytest.mark.submit),
    pytest.param(["123", "456", "789"], [], marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("input_list", "expected"), run_cases + submit_cases)
def test_remove_nonints(input_list, expected):
    print("\n---------------------------------")
    print(f"Input: {input_list}")
    print()
    result = remove_nonints(input_list)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    assert result == expected
