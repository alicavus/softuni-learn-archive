from project.guild_members.base_guild_member import BaseGuildMember
from project.guild_members.mage import Mage
from project.guild_members.warrior import Warrior

from project.guild_halls.base_guild_hall import BaseGuildHall
from project.guild_halls.combat_hall import CombatHall
from project.guild_halls.magic_tower import MagicTower

class GuildMaster:
    MEMBER_TYPES = {
        "Mage": Mage,
        "Warrior": Warrior
    }
    GUILD_HALLS = {
        "CombatHall": CombatHall,
        "MagicTower": MagicTower
    }

    def __init__(self):
        self.members: list[BaseGuildMember] = []
        self.guild_halls: list[BaseGuildHall] = []
    
    def add_member(self, member_type: str, member_tag: str, member_gold: int):
        cls = self.MEMBER_TYPES.get(member_type, None)
        member: BaseGuildMember = self._get_item(self.members, tag=member_tag)

        if cls is None:
            raise ValueError("Invalid member type!")
        
        if member is not None:
            raise ValueError(f"{member_tag} has already been added!")
        
        self.members.append(cls(member_tag, member_gold))
        return f"{member_tag} is successfully added as {member_type}."

    def add_guild_hall(self, guild_hall_type: str, guild_hall_alias: str):
        cls = self.GUILD_HALLS.get(guild_hall_type, None)
        hall: BaseGuildHall = self._get_item(self.guild_halls, alias=guild_hall_alias)

        if cls is None:
            raise ValueError("Invalid guild hall type!")
        
        if hall is not None:
            raise ValueError(f"{guild_hall_alias} has already been added!")
        
        self.guild_halls.append(cls(guild_hall_alias))
        return f"{guild_hall_alias} is successfully added as a {guild_hall_type}."

    def assign_member(self, guild_hall_alias: str, member_type: str):
        member: BaseGuildMember = self._get_item(self.members, role=member_type)
        hall: BaseGuildHall = self._get_item(self.guild_halls, alias=guild_hall_alias)

        if hall is None:
            raise ValueError(f"Guild hall {guild_hall_alias} does not exist!")
        
        if member is None:
            raise ValueError("No available members of the type!")
        
        if hall.max_member_count <= len(hall.members):
            return f"Maximum member count reached. Assignment is impossible."
        
        self.members.remove(member)
        hall.members.append(member)
        return f"{member.tag} was assigned to {guild_hall_alias}."

    def practice_members(self, guild_hall: BaseGuildHall, sessions_number: int):
        for _ in range(sessions_number):
            for member in guild_hall.members:
                member.practice()
        return f"{guild_hall.alias} members have {guild_hall.calculate_total_skill_level()} total skill level after {sessions_number} practice session/s."

    def unassign_member(self, guild_hall: BaseGuildHall, member_tag: str):
        member: BaseGuildMember = self._get_item(guild_hall.members, tag=member_tag)

        if member is None:
            return "The unassignment process was canceled."
        
        if member.skill_level == 10:
            return "The unassignment process was canceled."
        
        guild_hall.members.remove(member)
        self.members.append(member)
        return f"Unassigned member {member_tag}."
        

    def guild_update(self, min_skill_level_value: int):
        for hall in self.guild_halls:
            hall.increase_gold(min_skill_level_value)
        
        result = [
            "<<<Guild Updated Status>>>",
            f"Unassigned members count: {len(self.members)}",
            f"Guild halls count: {len(self.guild_halls)}"
        ]

        for hall in sorted(self.guild_halls, key=lambda hall: (-len(hall.members), hall.alias)):
            result.append(f">>>{hall.status()}")
        
        return "\n".join(result)


    @staticmethod
    def _get_item(collection, **attributes):
        if not attributes:
            return next((item for item in collection), None)
        return next((item for item in collection if all(getattr(item, k, None) == v for k, v in attributes.items())), None)

    @staticmethod
    def _get_items(collection, **attributes):
        if not attributes:
            return (item for item in collection)
        return (item for item in collection if all(getattr(item, k, None) == v for k, v in attributes.items()))