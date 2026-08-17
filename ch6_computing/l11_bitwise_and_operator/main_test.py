import main as student

run_cases = [
    (student.get_create_bits, 0b1000, 0b1010, True),
    (student.get_review_bits, 0b0100, 0b1001, False),
    (student.get_delete_bits, 0b0010, 0b0110, True),
    (student.get_edit_bits, 0b0001, 0b1110, False),
]

submit_cases = run_cases + [
    (student.get_create_bits, 0b1000, 0b0111, False),
    (student.get_review_bits, 0b0100, 0b0110, True),
    (student.get_delete_bits, 0b0010, 0b1101, False),
    (student.get_edit_bits, 0b0001, 0b0011, True),
]


def test(func, perm_bit, user_permissions, expected_output):
    print("---------------------------------")
    print(f"Testing {func.__name__}")
    print(f"Inputs: {user_permissions:04b}")
    print(f"Expecting: {expected_output}")
    result = func(user_permissions) == perm_bit
    print(f"Actual:    {result}")
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
