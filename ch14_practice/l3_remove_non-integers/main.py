def remove_nonints(nums: list[object]) -> list[int]:
    ints = []
    for i in nums:
        if type(i) is int:
            ints.append(i)
    return ints
