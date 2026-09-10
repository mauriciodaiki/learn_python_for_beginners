import pytest

from main import get_most_common_enemy

run_cases = [
    ({"jackal": 4, "kobold": 3, "soldier": 10, "gremlin": 5}, "soldier"),
    ({"jackal": 1, "kobold": 3, "soldier": 2, "gremlin": 5}, "gremlin"),
]

submit_cases = [
    ({"jackal": 2, "gremlin": 7}, "gremlin"),
    ({"jackal": 3}, "jackal"),
    ({}, None),
    ({"kobold": 5, "soldier": 5, "gremlin": 5, "dragon": 5}, "kobold"),
    ({"jackal": 5, "kobold": 3, "soldier": 10, "gremlin": 5, "dragon": 20}, "dragon"),
    ({"jackal": 5, "kobold": 3, "soldier": 2, "gremlin": 10, "dragon": 1}, "gremlin"),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_get_most_common_enemy(input1, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expected: {expected_output}")
    result = get_most_common_enemy(input1)
    if result == "None":
        print('Actual: "None"')
    else:
        print(f"Actual: {result}")
    assert result == expected_output
