import pytest

from main import generate_user_list

run_cases = [
    (5, list(range(5))),
    (10, list(range(10))),
]

submit_cases = [
    (0, []),
    (1, [0]),
    (100, list(range(100))),
    (25, list(range(25))),
    (50, list(range(50))),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_generate_user_list(input1, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}")
    result = generate_user_list(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
