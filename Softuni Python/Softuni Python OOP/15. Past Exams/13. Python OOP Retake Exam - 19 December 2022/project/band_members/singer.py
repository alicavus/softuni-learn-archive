from project.band_members.musician import Musician

class Singer(Musician):
    @property
    def _data(self) -> dict:
        return {
            "skills set": [
                "sing high pitch notes",
                "sing low pitch notes"
            ]
        }