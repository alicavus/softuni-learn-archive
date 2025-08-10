from project.peaks.base_peak import BasePeak

class ArcticPeak(BasePeak):
    @property
    def _data(self) -> dict:
        return {
            "recommended gear": ["Ice axe", "Crampons", "Insulated clothing", "Helmet"],
            "difficulty level": (2_000, 3_000)
        }