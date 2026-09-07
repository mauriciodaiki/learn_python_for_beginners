import pytest

from main import filter_messages

TestCase = tuple[list[str], list[str], list[int]]

run_cases: list[TestCase] = [
    (
        ["darn it", "this dang thing won't work", "lets fight one on one"],
        ["darn it", "this thing won't work", "lets fight one on one"],
        [0, 1, 0],
    ),
]

submit_cases: list[TestCase] = [
    (
        [
            "well dang it",
            "dang dang the whole dang thing",
            "kill that knight, dang it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the dang baddies",
        ],
        [
            "well it",
            "the whole thing",
            "kill that knight, it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the baddies",
        ],
        [1, 3, 1, 0, 0, 0, 1],
    ),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(
    ("input", "expected_filtered", "expected_dangs"), run_cases + submit_cases
)
def test_filter_messages(
    input: list[str], expected_filtered: list[str], expected_dangs: list[int]
) -> None:
    print("\n---------------------------------")
    print("Input:")
    print(f" * messages: {input}")
    print("Expected:")
    print(f" * filtered messages: {expected_filtered}")
    print(f" * words removed: {expected_dangs}")
    print("Actual:")
    try:
        result = filter_messages(input)
        print(f" * filtered messages: {result[0]}")
        print(f" * words removed: {result[1]}")
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        raise AssertionError from e

    assert result == (expected_filtered, expected_dangs)
