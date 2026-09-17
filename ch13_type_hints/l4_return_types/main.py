def get_item_description(item_name: str, damage: int, is_magical: bool) -> str:
    description = f"{item_name} deals {damage} damage"

    if is_magical:
        description += " and glows with arcane power"
    else:
        description += " and has no magical properties"

    return description
