from typing import Any

import pytest

from main import get_quest_status

CharacterProgress = dict[str, Any]


TestCase = tuple[CharacterProgress, str]

run_cases: list[TestCase] = [
    (
        {
            "character_name": "Sir Galahad",
            "quests": {
                "bridge_run": {
                    "status": "In Progress",
                },
                "talk_to_syl": {
                    "status": "Completed",
                },
            },
        },
        "In Progress",
    ),
    (
        {
            "character_name": "Lady Gwen",
            "quests": {
                "bridge_run": {
                    "status": "Completed",
                },
                "talk_to_syl": {
                    "status": "In Progress",
                },
            },
        },
        "Completed",
    ),
]

submit_cases: list[TestCase] = [
    (
        {
            "character_name": "Archer Finn",
            "quests": {
                "bridge_run": {
                    "status": "Not Started",
                },
                "talk_to_syl": {
                    "status": "Completed",
                },
            },
        },
        "Not Started",
    ),
    (
        {
            "character_name": "Mage Elara",
            "quests": {
                "bridge_run": {
                    "status": "Failed",
                },
                "talk_to_syl": {
                    "status": "Completed",
                },
            },
        },
        "Failed",
    ),
    (
        {
            "character_name": "Rogue Talon",
            "quests": {
                "bridge_run": {
                    "status": "Completed",
                },
                "talk_to_syl": {
                    "status": "Not Started",
                },
            },
        },
        "Completed",
    ),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(("progress", "expected"), run_cases + submit_cases)
def test_get_quest_status(progress: CharacterProgress, expected: str) -> None:
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * Progress Dictionary: {progress}")
    print(f"Expected: {expected}")
    result = get_quest_status(progress)
    print(f"Actual:   {result}")
    assert result == expected
