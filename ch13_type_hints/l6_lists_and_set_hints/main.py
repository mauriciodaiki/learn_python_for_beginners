def get_unique_items(inventory: list[str]) -> set[str]:
    unique_items = set()

    for item in inventory:
        unique_items.add(item)

    return unique_items
