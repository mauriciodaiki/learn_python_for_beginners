from main import max_players_on_server

run_cases = [
    (1.024e18, 1.024e19, 1.024e20),
]

submit_cases = run_cases


def test(expected1, expected2, expected3):
    print("---------------------------------")
    result = max_players_on_server()
    print(f"Expected: {(expected1, expected2, expected3)}")
    print(f"Actual:   {result}")
    if result == (expected1, expected2, expected3):
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
