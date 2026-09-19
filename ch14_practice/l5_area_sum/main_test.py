import pytest
from main import area_sum

run_cases = [
    ([{"height": 4, "width": 5}], 20),
    ([{"height": 4, "width": 5}, {"height": 4, "width": 9}], 56),
    ([{"height": 4, "width": 5}, {"height": 18, "width": 5}], 110),
]

submit_cases = [
    pytest.param(
        [{"height": 2, "width": 3}, {"height": 4, "width": 5}],
        26,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [{"height": 6, "width": 7}, {"height": 8, "width": 9}],
        114,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [{"height": 10, "width": 11}, {"height": 12, "width": 13}],
        266,
        marks=pytest.mark.submit,
    ),
    pytest.param([{"height": 0, "width": 0}], 0, marks=pytest.mark.submit),
    pytest.param([], 0, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("rectangles", "expected"), run_cases + submit_cases)
def test_area_sum(rectangles, expected):
    print("\n---------------------------------")
    print("Input:")
    for rect in rectangles:
        print(f" - {rect}")
    print()
    result = area_sum(rectangles)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    assert result == expected
