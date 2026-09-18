def summarize_quest_rewards(
    completed_quests: list[str], quest_rewards: dict[str, int]
) -> list[tuple[str, int]]:
    summary: list[tuple[str, int]] = []

    for quest_name in completed_quests:
        if quest_name in quest_rewards:
            quest_xp = quest_rewards[quest_name]
            summary.append((quest_name, quest_xp))

    return summary
