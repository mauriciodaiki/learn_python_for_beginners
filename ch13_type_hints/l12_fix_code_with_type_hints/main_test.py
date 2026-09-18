import pytest
from main import summarize_quest_rewards

run_cases = [
    (
        ["Defeat the Goblin King", "Rescue the Blacksmith"],
        {"Defeat the Goblin King": 500, "Rescue the Blacksmith": 250},
        [("Defeat the Goblin King", 500), ("Rescue the Blacksmith", 250)],
    ),
    (
        ["Find the Lost Tome", "Unknown Quest"],
        {"Find the Lost Tome": 300},
        [("Find the Lost Tome", 300)],
    ),
]

submit_cases = [
    pytest.param(
        ["Light the Beacon", "Seal the Rift", "Feed the Cat"],
        {"Light the Beacon": 150, "Seal the Rift": 800},
        [("Light the Beacon", 150), ("Seal the Rift", 800)],
        marks=pytest.mark.submit,
    ),
]

expected_annotations = {
    "completed_quests": list[str],
    "quest_rewards": dict[str, int],
    "return": list[tuple[str, int]],
}


@pytest.mark.parametrize(
    ("completed_quests", "quest_rewards", "expected_summary"),
    run_cases + submit_cases,
)
def test_summarize_quest_rewards(completed_quests, quest_rewards, expected_summary):
    print("\n---------------------------------")
    print(f"Completed quests: {completed_quests}")
    print(f"Quest rewards: {quest_rewards}")
    print()

    actual_summary = summarize_quest_rewards(completed_quests, quest_rewards)

    print(f"Expected summary: {expected_summary}")
    print(f"Actual summary:   {actual_summary}")
    print()

    assert actual_summary == expected_summary

    for annotation_name, expected_type in expected_annotations.items():
        actual_type = summarize_quest_rewards.__annotations__.get(annotation_name)

        print(f"{annotation_name}: expected {expected_type}")
        print(f"{annotation_name}: actual {actual_type}")
        print()

        assert actual_type == expected_type
