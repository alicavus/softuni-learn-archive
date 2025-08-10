from project.guild_members.base_guild_member import BaseGuildMember

class Warrior(BaseGuildMember):
    @property
    def _data(self) -> dict:
        return {
            "skill level": 2,
            "practice skill gain": 2 
        }
    
    def __init__(self, tag: str, gold: int):
        super().__init__(tag, gold, self.__class__.__name__, self._data.get("skill level", 1))
    
    def practice(self):
        skill_level = self.skill_level + self._data.get("practice skill gain", 0)
        self.skill_level = min(10, skill_level)
    
