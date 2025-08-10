class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name: str = name
        self.hp: int = hp
        self.mp: int = mp
        self.skills: dict[str, int] = {}
        self.guild: str = "Unaffiliated"
    
    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"
    
    def player_info(self) -> str:
        result: list[str] = [f"Name: {self.name}", f"Guild: {self.guild}", f"HP: {self.hp}", f"MP: {self.mp}"]
        result.extend([f"==={skill} - {self.skills[skill]}" for skill in self.skills])
        return "\n".join(result)
