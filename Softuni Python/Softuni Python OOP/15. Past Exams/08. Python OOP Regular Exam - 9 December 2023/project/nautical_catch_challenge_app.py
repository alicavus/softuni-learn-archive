from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver

from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish

class NauticalCatchChallengeApp:
    VALID_DIVERS = {
        "FreeDiver": FreeDiver,
        "ScubaDiver": ScubaDiver
    }
    VALID_FISHES = {
        "DeepSeaFish": DeepSeaFish,
        "PredatoryFish": PredatoryFish
    }
    def __init__(self):
        self.divers: list[BaseDiver] = []
        self.fish_list: list[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str) -> str:
        cls = self.VALID_DIVERS.get(diver_type, None)
        diver: BaseDiver = self.get_item(self.divers, "name", diver_name)

        if cls is None:
            return f"{diver_type} is not allowed in our competition."

        if diver is not None:
            return f"{diver_name} is already a participant."

        self.divers.append(cls(diver_name))
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float) -> str:
        cls = self.VALID_FISHES.get(fish_type, None)
        fish: BaseFish = self.get_item(self.fish_list, "name", fish_name)

        if cls is None:
            return f"{fish_type} is forbidden for chasing in our competition."

        if fish is not None:
            return f"{fish_name} is already permitted."

        self.fish_list.append(cls(fish_name, points))
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver: BaseDiver = self.get_item(self.divers, "name", diver_name)
        fish: BaseFish = self.get_item(self.fish_list, "name", fish_name)

        if diver is None:
            return f"{diver_name} is not registered for the competition."

        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."

        diver.hit(fish)
        if diver.oxygen_level == 0:
            diver.update_health_status()
        return f"{diver_name} hits a {fish.points}pt. {fish_name}."
    
    def health_recovery(self):
        cnt = 0
        for diver in self.get_items(self.divers, "has_health_issue", True):
            diver.has_health_issue = False
            diver.renew_oxy()
            cnt += 1
        return f"Divers recovered: {cnt}"
    
    def diver_catch_report(self, diver_name: str):
        diver: BaseDiver = self.get_item(self.divers, "name", diver_name)

        if diver is None:
            return
        
        result = [f"**{diver_name} Catch Report**"]

        result.extend(fish.fish_details() for fish in self.get_items(diver.catch))
        
        return "\n".join(result)
    
    def competition_statistics(self):
        divers = sorted(
            self.get_items(self.divers, "has_health_issue", False),
            key=lambda diver: (-diver.competition_points, -len(diver.catch), diver.name)
        )

        result = ["**Nautical Catch Challenge Statistics**"]
        result.extend(str(diver) for diver in divers)

        return "\n".join(result)


    @staticmethod
    def get_items(collection, attribute_name = None, attribute_value = None):
        if attribute_name is None:
            return (item for item in collection)
        return (item for item in collection if getattr(item, attribute_name, None) == attribute_value)

    @staticmethod
    def get_item(collection, attribute_name = None, attribute_value = None):
        if attribute_name is None:
            return next((item for item in collection), None)
        return next((item for item in collection if getattr(item, attribute_name, None) == attribute_value), None)
