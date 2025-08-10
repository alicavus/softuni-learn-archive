def draw_cards(*args, **kwargs) -> str:
    monsters = []
    spells = []

    for card_data in args:
        card_name, card_type = card_data
        collection = monsters if card_type == "monster" else spells
        collection += [card_name]

    for card_name, card_type in kwargs.items():
        collection = monsters if card_type == "monster" else spells
        collection += [card_name]

    result = []

    if monsters:
        result += ["Monster cards:"]
        for monster in sorted(monsters, reverse=True):
            result += [f"  ***{monster}"]

    if spells:
        result += ["Spell cards:"]
        for spell in sorted(spells):
            result += [f"  $$${spell}"]

    return "\n".join(result)

print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
