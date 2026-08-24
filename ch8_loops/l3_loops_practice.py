def print_numbers_from_five_to(end):
    for i in range(5, end):
        print(i)


# Don't edit below this line


def test(end):
    print(f"Using input end: {end}")
    print(f"Printing numbers from 5 to {end - 1}:")
    print_numbers_from_five_to(end)
    print("=====================================")


def main():
    test(16)
    test(6)
    test(11)


main()
