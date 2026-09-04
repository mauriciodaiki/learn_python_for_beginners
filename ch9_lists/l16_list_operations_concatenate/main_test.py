import pytest

from main import concatenate_favorites

run_cases = [
    (
        ["sword", "dagger"],
        ["bracers", "helmet"],
        ["feather", "iron bars"],
        (["sword", "dagger", "bracers", "helmet", "feather", "iron bars"]),
    ),
]

submit_cases = [
    (
        ["lance"],
        ["shield"],
        ["potions"],
        (["lance", "shield", "potions"]),
    ),
    (
        ["bow", "staff"],
        ["breastplate"],
        ["scrolls", "bedroll"],
        (["bow", "staff", "breastplate", "scrolls", "bedroll"]),
    ),
    ([], [], [], ([])),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(
    ("input1", "input2", "input3", "expected_output"), run_cases + submit_cases
)
def test_concatenate_favorites(input1, input2, input3, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    result = concatenate_favorites(input1, input2, input3)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
