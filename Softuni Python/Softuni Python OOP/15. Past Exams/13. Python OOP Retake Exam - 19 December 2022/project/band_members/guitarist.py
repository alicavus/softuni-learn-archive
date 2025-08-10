from project.band_members.musician import Musician

class Guitarist(Musician):
    @property
    def _data(self) -> dict:
        return {
            "skills set": [
                "play metal",
                "play rock",
                "play jazz"
            ]
        }