from main import check_high_score

run_cases = [
    ("ash ketchum", "ash ketchum", "brock", "high"),
    ("brock", "ash ketchum", "brock", "low"),
]

submit_cases = run_cases + [
    ("misty", "brock", "ash ketchum", "neither"),
    ("red", "red", "blue", "high"),
    ("blue", "red", "blue", "low"),
    ("green", "red", "blue", "neither"),
]


def test(
    player_name, high_scoring_player_name, low_scoring_player_name, expected_output
):
    print("---------------------------------")
    print(
        f"Player Name: {player_name}, High Scoring Player: {high_scoring_player_name}, Low Scoring Player: {low_scoring_player_name}"
    )
    result = check_high_score(
        player_name, high_scoring_player_name, low_scoring_player_name
    )
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
