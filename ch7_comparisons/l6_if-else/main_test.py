from main import player_status

run_cases = [
    (0, "dead"),
    (4, "injured"),
]

submit_cases = run_cases + [
    (6, "healthy"),
    (5, "injured"),
    (1, "injured"),
    (10, "healthy"),
    (-1, "dead"),
]


def test(health, expected_status):
    print("---------------------------------")
    print(f"Health: {health}")
    result = player_status(health)
    print(f"Expected: {expected_status}")
    print(f"Result:   {result}")
    if result == expected_status:
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
