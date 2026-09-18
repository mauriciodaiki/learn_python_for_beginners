def number_sum(n: int) -> int:
    total = 0
    if n < 1:
        return 0
    for i in range (1, n + 1):
        total += i
        
    return total