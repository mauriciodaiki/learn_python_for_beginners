from main import sum_of_numbers

run_cases = [(0, 5, 10), (0, 10, 45), (10, 20, 145)]

submit_cases = run_cases + [
    (1, 100, 4950),
    (5, 50, 1215),
    (20, 30, 245),
    (50, 60, 545),
    (100, 110, 1045),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print("Inputs:")
    print(f" * start: {input1}")
    print(f" * end: {input2}")
    result = sum_of_numbers(input1, input2)
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
