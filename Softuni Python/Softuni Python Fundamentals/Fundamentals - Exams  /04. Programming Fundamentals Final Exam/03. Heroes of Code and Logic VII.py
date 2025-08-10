class Hero:
    __max_mana_points = 200
    __max_hit_points = 100
    __is_alive = True

    def __init__(self, name: str, mana_points: int, hit_points: int):
        self.name = name
        self.mana_points = mana_points if mana_points <= self.__max_mana_points else self.__max_mana_points
        self.hit_points = hit_points if hit_points <= self.__max_hit_points else self.__max_hit_points
    
    def __str__(self):
        if self.__is_alive:
            return f'{self.name}\n  HP: {self.hit_points}\n  MP: {self.mana_points}'
        #return None
    
    def cast_spell(self, needed_mana_points: int, spell: str):
        if self.mana_points >= needed_mana_points:
            self.mana_points -= needed_mana_points
            print(f"{self.name} has successfully cast {spell} and now has {self.mana_points} MP!")
        else:
            print(f"{self.name} does not have enough MP to cast {spell}!")
    
    def take_damage(self, damage: int, attacker: str):
        self.hit_points -= damage

        if self.hit_points <= 0 :
            self.__is_alive = False
            print(f"{self.name} has been killed by {attacker}!")
            del heroes[self.name]
        else:
            print(f"{self.name} was hit for {damage} HP by {attacker} and now has {self.hit_points} HP left!")
    
    def heal(self, amount: int):
        if self.hit_points + amount > self.__max_hit_points:
            amount = self.__max_hit_points - self.hit_points
        self.hit_points += amount
        print(f"{self.name} healed for {amount} HP!")
    
    def recharge(self, amount: int):
        if self.mana_points + amount > self.__max_mana_points:
            amount = self.__max_mana_points - self.mana_points
        self.mana_points += amount
        print(f"{self.name} recharged for {amount} MP!")


class Party:
    def __init__(self):
        self.members = {}
    
    def add_hero(self, hero: Hero):
        pass



heroes = {}

for _ in range(int(input())):
    hero_data = input().split()
    heroes[hero_data[0]] = Hero(name=hero_data[0], hit_points=int(hero_data[1]),mana_points=int(hero_data[2]))

while True:
    action_data = input()
    if action_data == "End":
        break
    actions = action_data.split(" - ")

    match actions[0]:
        case "CastSpell":
            name, mana_needed, spell = actions[1:]
            heroes[name].cast_spell(needed_mana_points=int(mana_needed), spell=spell)
        case "TakeDamage":
            name, damage, attacker = actions[1:]
            heroes[name].take_damage(damage=int(damage), attacker=attacker)
        case "Recharge":
            name, amount = actions[1:]
            heroes[name].recharge(amount=int(amount))
        case "Heal":
            name, amount = actions[1:]
            heroes[name].heal(amount=int(amount))

for hero in heroes:
    if heroes[hero] is not None:
        print(heroes[hero])





