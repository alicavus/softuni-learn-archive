from project.player import Player
from project.guild import Guild

player_one = Player("George", 50, 100)
print(player_one.add_skill("Shield Break", 20))
print(player_one.add_skill("Shield Break", 20))
print(player_one.add_skill("Telleport", 200))
print(player_one.player_info())

player_two = Player("Nina", 50, 100)
print(player_two.add_skill("Fire Ball", 20))
print(player_two.player_info())

player_tree = Player("Qogo", 50, 100)
print(player_tree.add_skill("Telekinesys", 20))
print(player_tree.add_skill("Mind read", 70))
print(player_tree.player_info())

guild_one = Guild("UGT")
print(guild_one.assign_player(player_one))
print(guild_one.guild_info())

guild_two = Guild("PALL")
print(guild_two.assign_player(player_one))
print(guild_two.assign_player(player_tree))
print(guild_two.assign_player(player_two))
print(guild_two.assign_player(player_two))
print(guild_two.kick_player(player_two.name))
print(guild_one.assign_player(player_two))
print(guild_two.kick_player(player_one.name))
print(guild_two.guild_info())