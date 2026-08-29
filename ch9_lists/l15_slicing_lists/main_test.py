import pytest

from main import get_champion_slices

run_cases = [
    (
        ["Thrundar", "Morgate", "Gandolfo", "Thraine", "Norwad", "Gilforn"],
        (
            ["Gandolfo", "Thraine", "Norwad", "Gilforn"],
            ["Thrundar", "Morgate", "Gandolfo", "Thraine", "Norwad"],
            ["Thrundar", "Gandolfo", "Norwad"],
        ),
    ),
    (
        ["Frank", "Dennis", "Sweet Dee", "Mac", "Charlie"],
        (
            ["Sweet Dee", "Mac", "Charlie"],
            ["Frank", "Dennis", "Sweet Dee", "Mac"],
            ["Frank", "Sweet Dee", "Charlie"],
        ),
    ),
]

submit_cases = [
    (([]), ([], [], [])),
    (
        (["John", "Sydney", "Spencer", "Bill", "Matthew", "Brandon", "Tony"]),
        (
            ["Spencer", "Bill", "Matthew", "Brandon", "Tony"],
            ["John", "Sydney", "Spencer", "Bill", "Matthew", "Brandon"],
            ["John", "Spencer", "Matthew", "Tony"],
        ),
    ),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_get_champion_slices(input1, expected_output):
    print("\n" + "-" * 40)
    print(f"Input:\n{input1}")
    print(f"Expected:\n{expected_output}")
    try:
        slice_1, slice_2, slice_3 = get_champion_slices(input1)
        result = (slice_1, slice_2, slice_3)
    except Exception as e:
        print(f"Error: {e}")
        raise AssertionError from e
    print(f"Actual:\n{result}")
    assert result == expected_output
