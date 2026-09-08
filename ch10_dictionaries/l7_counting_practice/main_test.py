import pytest

from main import count_enemies

run_cases = [
    (["jackal", "kobold", "soldier"], {"jackal": 1, "kobold": 1, "soldier": 1}),
    (["jackal", "kobold", "jackal"], {"jackal": 2, "kobold": 1}),
]

submit_cases = [
    ([], {}),
    (["jackal"], {"jackal": 1}),
    (
        [
            "jackal",
            "kobold",
            "jackal",
            "kobold",
            "soldier",
            "kobold",
            "soldier",
            "soldier",
            "jackal",
            "jackal",
            "gremlin",
            "jackal",
            "jackal",
        ],
        {"jackal": 6, "kobold": 3, "soldier": 3, "gremlin": 1},
    ),
    (["jackal", "kobold", "gremlin"], {"jackal": 1, "kobold": 1, "gremlin": 1}),
    (["jackal", "jackal", "jackal"], {"jackal": 3}),
    (["gremlin", "gremlin", "gremlin"], {"gremlin": 3}),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_count_enemies(input1, expected_output):
    result = count_enemies(input1)
    print("\n---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
