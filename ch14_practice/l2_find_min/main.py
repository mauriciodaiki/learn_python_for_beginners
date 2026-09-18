def find_min(nums: list[int]) -> int | float:
    smallest_so_far = float("inf")
    for i in nums:
        if i < smallest_so_far:
            smallest_so_far = i
    return smallest_so_far
