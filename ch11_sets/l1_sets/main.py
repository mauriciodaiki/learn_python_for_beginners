def remove_duplicates(spells):
    # First solution:
    # spells_seen = set()
    # unique_spells = []
    # for spell in spells:
    #     if spell not in spells_seen:
    #         spells_seen.add(spell)
    #         unique_spells.append(spell)
    # return unique_spells

    # Second solution:
    unique_spells = set(spells)
    spells = list(unique_spells)
    return spells
