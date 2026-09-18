def get_reward_summary(items: list[str], item_counts: dict[str, int]) -> tuple[str, int]:
    total_items = 0

    for count in item_counts.values():
        total_items += count

    first_item = items[0]
    return first_item, total_items
