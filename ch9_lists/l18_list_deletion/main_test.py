import pytest

from main import trim_strongholds

run_cases = [
    (
        [
            "Rivendale",
            "The Morgoth Mountains",
            "The Lonely Island",
            "Mordia",
            "Mordane",
            "Gondolin",
        ],
        [
            "The Morgoth Mountains",
            "The Lonely Island",
            "Mordia",
        ],
    ),
]

submit_cases = [
    (
        [
            "Pogsmeade",
            "Dogwarts",
            "The Leaky Pot",
            "The Screaming Hut",
        ],
        [
            "Dogwarts",
        ],
    ),
    (
        [
            "Midgard",
            "Cosmo Canyon",
            "Nibelheim",
            "Costa del Sol",
            "Pallet Town",
            "Viridian City",
            "Salamandastron",
            "Redwall Abbey",
            "Fisherman's Horizon",
            "Waterdeep",
            "Elturel",
            "Candlekeep",
            "Chult",
            "Eorzea",
            "Ratchet",
            "Orgrimmar",
            "Stormwind",
            "Shattrath",
            "Dalaran",
        ],
        [
            "Cosmo Canyon",
            "Nibelheim",
            "Costa del Sol",
            "Pallet Town",
            "Viridian City",
            "Salamandastron",
            "Redwall Abbey",
            "Fisherman's Horizon",
            "Waterdeep",
            "Elturel",
            "Candlekeep",
            "Chult",
            "Eorzea",
            "Ratchet",
            "Orgrimmar",
            "Stormwind",
        ],
    ),
]

submit_cases = [pytest.param(*case, marks=pytest.mark.submit) for case in submit_cases]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_trim_strongholds(input1, expected_output):
    print("\n---------------------------------")
    print(f"    Input: {input1}")
    trim_strongholds(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {input1}")
    assert input1 == expected_output
