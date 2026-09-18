def factorial(num: int) -> int:
    product = 1
    for i in range(num, 0, -1):
        product *= i        
    return product
    