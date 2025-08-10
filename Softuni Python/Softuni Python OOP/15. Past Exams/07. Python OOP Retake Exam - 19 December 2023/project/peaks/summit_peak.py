from project.peaks.base_peak import BasePeak

class SummitPeak(BasePeak):
    @property
    def _data(self) -> dict:
        return {
            "recommended gear": ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"],
            "difficulty level": (1_500, 2_500)
        }