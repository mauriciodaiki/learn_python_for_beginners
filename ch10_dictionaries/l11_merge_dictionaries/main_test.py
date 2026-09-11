import pytest

from main import merge

run_cases = [
    (
        {"Goku": 8000, "Vegeta": 7500},
        {"Piccolo": 3500, "Gohan": 2800},
        {
            "Goku": 8000,
            "Vegeta": 7500,
            "Piccolo": 3500,
            "Gohan": 2800,
        },
    ),
    (
        {"Frieza": 120000, "Cell": 900000},
        {"Majin_Buu": 1100000, "Broly": 10000},
        {
            "Frieza": 120000,
            "Cell": 900000,
            "Majin_Buu": 1100000,
            "Broly": 10000,
        },
    ),
]

submit_cases = [
    ({}, {}, {}),
    (
        {
            "Android_17": 30000,
            "Android_18": 30000,
            "Future_Trunks": 9000,
            "Kid_Trunks": 7000,
        },
        {
            "Android_17": 40000,
            "Dr_Gero": 10000,
            "Goten": 6500,
            "Future_Gohan": 8000,
        },
        {
            "Android_17": 40000,
            "Android_18": 30000,
            "Dr_Gero": 10000,
            "Future_Trunks": 9000,
            "Kid_Trunks": 7000,
            "Goten": 6500,
            "Future_Gohan": 8000,
        },
    ),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(
    ("input1", "input2", "expected_output"), run_cases + submit_cases
)
def test_merge(input1, input2, expected_output):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * first_half:  {input1}")
    print(f" * second_half: {input2}")
    original_input1 = input1.copy()
    result = merge(input1, input2)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if input1 != original_input1:
        print("Fail")
        print("The first input dictionary should not be modified")
    assert input1 == original_input1
    assert result == expected_output
