def get_loot_drop(enemy_level: int) -> tuple[str, int]:
    if enemy_level > 10:
        return "Emerald Brome", 1

    return "Smokestone Chip", 3
