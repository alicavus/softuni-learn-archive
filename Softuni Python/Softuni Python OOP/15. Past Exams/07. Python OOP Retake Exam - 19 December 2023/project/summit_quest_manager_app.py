from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak
from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber

class SummitQuestManagerApp:
    VALID_CLIMBERS = {
        "ArcticClimber": ArcticClimber,
        "SummitClimber": SummitClimber
    }
    VALID_PEAKS = {
        "ArcticPeak": ArcticPeak,
        "SummitPeak": SummitPeak
    }
    def __init__(self):
        self.climbers: list = []
        self.peaks: list = []
    
    def register_climber(self, climber_type: str, climber_name: str) -> str:
        cls = self.__class__.VALID_CLIMBERS.get(climber_type, None)
        
        if cls is None:
            return f"{climber_type} doesn't exist in our register."
        
        climber = self.get_item(self.climbers, "name", climber_name)

        if climber is not None:
            return f"{climber_name} has been already registered."
        
        self.climbers.append(cls(climber_name))
        return f"{climber_name} is successfully registered as a {climber_type}."
    
    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int) -> str:
        cls = self.__class__.VALID_PEAKS.get(peak_type, None)

        if cls is None:
            return f"{peak_type} is an unknown type of peak."
        
        self.peaks.append(cls(peak_name, peak_elevation))
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."
        
    def check_gear(self, climber_name: str, peak_name: str, gear: list[str]) -> str|None:
        peak = self.get_item(self.peaks, "name", peak_name)
        climber = self.get_item(self.climbers, "name", climber_name)

        if not peak or not climber:
            return
        
        required_gear = peak.get_recommended_gear()

        missing_gear = sorted([g for g in required_gear if g not in gear])

        if missing_gear:
            climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(missing_gear)}."

        return f"{climber_name} is prepared to climb {peak_name}."
    
    def perform_climbing(self, climber_name: str, peak_name: str) -> str:
        climber = self.get_item(self.climbers, "name", climber_name)
        peak = self.get_item(self.peaks, "name", peak_name)

        if climber is None:
            return f"Climber {climber_name} is not registered yet."
        
        if peak is None:
            return f"Peak {peak_name} is not part of the wish list."
        
        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."
        
        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        
        climber.climb(peak)
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.calculate_difficulty_level()}."
    
    def get_statistics(self):
        result = [f"Total climbed peaks: {sum(1 for p in self.peaks if p.is_conquered)}", "**Climber's statistics:**"]
        climbers = sorted((c for c in self.climbers if c.conquered_peaks != []), key=lambda x: (-(len(x.conquered_peaks)), x.name))

        result.extend(str(climber) for climber in climbers)

        return "\n".join(result)
    
    # helpers    
    @staticmethod
    def get_item(collection, attribute_name = None, attribute_value = None):
        if attribute_name is None:
            return next((item for item in collection), None)
        return next((item for item in collection if getattr(item, attribute_name, None) == attribute_value), None)
