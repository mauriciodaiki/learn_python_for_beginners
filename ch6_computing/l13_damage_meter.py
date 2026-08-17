def main():
    calculate_dps(8_000_000, 45)
    calculate_dps(10_000_000, 49)


# Don't edit below this line


def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps}")
    print("=====================================")


main()
