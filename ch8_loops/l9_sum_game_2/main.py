def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
        print(i)
    return total
