import pytest

from main import get_leather_scraps

run_cases = [
    ("Leather Scraps",),
]

submit_cases = [
    ("Leather Scraps",),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(("expected_output",), run_cases + submit_cases)
def test_get_leather_scraps(expected_output):
    print("\n---------------------------------")
    result = get_leather_scraps()
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
