def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    max_so_far_name = None
    for name in enemies_dict:
        count = enemies_dict[name]
        if count > max_so_far:
            max_so_far = count
            max_so_far_name = name
    return max_so_far_name
