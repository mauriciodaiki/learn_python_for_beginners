import pytest

from main import count_vowels

run_cases = [
    (
        "Did someone say Thunderfury, Blessed Blade of the Windseeker?",
        (19, {"u", "o", "i", "e", "a"}),
    ),
    ("LF9M UBRS NEED ALL!!!!", (4, {"U", "E", "A"})),
]

submit_cases = [
    ("Leatherworker LFW Have all end game recipes!", (14, {"e", "i", "o", "a"})),
    ("", (0, set())),
    (
        "Can anyone spare 1g so I can train my new spells?",
        (13, {"o", "I", "i", "e", "a"}),
    ),
    ("no", (1, {"o"})),
    ("mages need a nerf", (6, {"e", "a"})),
    ("wtb port to Roshar", (4, {"o", "a"})),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_count_vowels(input1, expected_output):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * Text: {input1}")
    print(f"Expected: {expected_output}")
    result = count_vowels(input1)
    print(f"Actual:   {result}")
    assert result == expected_output
