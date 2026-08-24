def countdown_to_start():
    for i in range (10, 0, -1):
        if i > 1:
            print(f"{i}...")
        else:
            print(f"{i}...Fight!")


# Don't edit below this line


def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()
