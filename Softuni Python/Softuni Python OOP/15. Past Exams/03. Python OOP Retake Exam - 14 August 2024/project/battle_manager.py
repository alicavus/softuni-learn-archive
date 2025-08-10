from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone

class BattleManager:
    ZONES = {
        "RoyalZone": RoyalZone,
        "PirateZone": PirateZone
    }
    SHIPS = {
        "RoyalBattleship": RoyalBattleship,
        "PirateBattleship": PirateBattleship
    }
    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in self.ZONES:
            raise Exception("Invalid zone type!")

        #zone = next((zone for zone in self.zones if zone.code == zone_code), None)
        zone = self.get_item(self.zones, "code", zone_code)
        if zone:
            raise Exception("Zone already exists!")

        self.zones.append(self.ZONES[zone_type](zone_code))
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in self.SHIPS:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        self.ships.append(self.SHIPS[ship_type](name, health, hit_strength))
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health == 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        ship.is_attacking = True if str(zone).split()[0] == str(ship).split()[0] else False
        ship.is_available = False
        zone.ships.append(ship)
        zone.volume -= 1

        return  f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        #ship = next((ship for ship in self.ships if ship.name == ship_name), None)
        ship = self.get_item(self.ships, "name", ship_name)
        if not ship:
            return "No ship with this name!"

        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        allies = list(self.get_items(zone.ships, "is_attacking", True))
        enemies = list(self.get_items(zone.ships, "is_attacking", False))

        if not allies or not enemies:
            return "Not enough participants. The battle is canceled."

        ally: BaseBattleship = sorted(allies, key=lambda ship: ship.hit_strength)[-1]
        enemy: BaseBattleship = sorted(enemies, key=lambda ship: ship.health)[-1]

        ally.attack()
        enemy.take_damage(ally)

        if enemy.health <= 0:
            zone.ships.remove(enemy)
            zone.volume += 1
            #self.remove_battleship(enemy.name)
            self.ships.remove(enemy)
            return f"{enemy.name} lost the battle and was sunk."

        if ally.ammunition <= 0:
            zone.ships.remove(ally)
            zone.volume += 1
            #self.remove_battleship(ally.name)
            self.ships.remove(ally)
            return f"{ally.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = list(self.get_items(self.ships, "is_available", True))
        result = [f"Available Battleships: {len(available_ships)}"]
        if available_ships:
            result.append(f"#{', '.join([ship.name for ship in available_ships])}#")

        result.extend(["***Zones Statistics:***", f"Total Zones: {len(self.zones)}"])
        for zone in sorted(self.zones, key=lambda z: z.code):
            result.append(zone.zone_info())

        return "\n".join(result)

    #helper methods
    @staticmethod
    def get_items(collection, attribute_name, attribute_value):
        return (item for item in collection if getattr(item, attribute_name) == attribute_value)

    @staticmethod
    def get_item(collection, attribute_name, attribute_value):
        return next((item for item in collection if getattr(item, attribute_name) == attribute_value), None)


