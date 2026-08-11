def take_magic_damage(health, resist, amp, spell_power):
    total_damage = spell_power * amp
    actual_damage = total_damage - resist
    new_health = health - actual_damage
    return new_health
