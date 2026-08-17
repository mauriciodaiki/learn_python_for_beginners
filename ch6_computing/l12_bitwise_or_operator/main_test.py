from main import calculate_guild_perms

run_cases = [
    (0b0001, 0b0010, 0b0001, 0b1011, 0b1011),
]

submit_cases = run_cases + [
    (0b0000, 0b0000, 0b0000, 0b1011, 0b1011),
    (0b1001, 0b0010, 0b1101, 0b1011, 0b1111),
]


def test(input1, input2, input3, input4, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}, {input4}")
    result = calculate_guild_perms(input1, input2, input3, input4)
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
