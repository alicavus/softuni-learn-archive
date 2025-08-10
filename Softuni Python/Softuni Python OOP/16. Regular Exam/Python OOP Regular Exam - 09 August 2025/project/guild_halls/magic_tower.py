from project.guild_halls.base_guild_hall import BaseGuildHall

class MagicTower(BaseGuildHall):
    @property
    def _data(self) -> dict:
        return {
            "max member count": 4,
            "increase class": "Mage",
            "increase by": 2,
        }
    
    def increase_gold(self, min_skill_level_value: int):
        for member in self.members:
            if member.role == self._data.get("increase class", None):
                if member.skill_level >= min_skill_level_value:
                    member.gold *= self._data.get("increase by", 1)
        
    
    

















