def summon_mount(has_mount: bool, distance: int) -> str | None:
    if not has_mount:
        return None

    if distance > 420:
        return None

    return "Battle Horse"
