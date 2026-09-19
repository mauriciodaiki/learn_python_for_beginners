def divide_list(nums: list[int], divisor: int) -> list[float]:
    divided_list = []
    for num in nums:
        divided = num / divisor
        divided_list.append(divided)
    return divided_list
