from project.band_members.musician import Musician
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.band import Band
from project.concert import Concert

class ConcertTrackerApp:
    MUSICIAN_TYPES = {
        "Drummer": Drummer,
        "Guitarist": Guitarist,
        "Singer": Singer
    }
    CONCERT_TYPE_MUSICIAN_SKILLS_REQUIRED = {
        "Rock": {
            Drummer: ["play the drums with drumsticks"],
            Singer: ["sing high pitch notes"],
            Guitarist: ["play rock"]
        },
        "Metal": {
            Drummer: ["play the drums with drumsticks"],
            Singer: ["sing low pitch notes"],
            Guitarist: ["play metal"]
        },
        "Jazz": {
            Drummer: ["play the drums with drum brushes"],
            Singer: ["sing high pitch notes", "sing low pitch notes"],
            Guitarist: ["play jazz"]
        }
    }

    def __init__(self):
        self.bands: list[Band] = []
        self.musicians: list[Musician] = []
        self.concerts: list[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        cls = self.MUSICIAN_TYPES.get(musician_type, None)
        musician = self._get_item(self.musicians, name=name)
        if cls is None:
            raise ValueError("Invalid musician type!")

        if musician is not None:
            raise Exception(f"{name} is already a musician!")

        self.musicians.append(cls(name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = self._get_item(self.bands, name=name)

        if band is not None:
            raise Exception(f"{name} band is already created!")

        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self._get_item(self.concerts, place=place)

        if concert is not None:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician: Musician = self._get_item(self.musicians, name=musician_name)
        band: Band = self._get_item(self.bands, name=band_name)

        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")

        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band: Band = self._get_item(self.bands, name=band_name)

        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        musician: Musician = self._get_item(band.members, name=musician_name)

        if musician is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert: Concert = self._get_item(self.concerts, place=concert_place)
        band: Band = self._get_item(self.bands, name=band_name)

        if band.get_musician_types() != set(self.MUSICIAN_TYPES.keys()):
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        skills_required = self.CONCERT_TYPE_MUSICIAN_SKILLS_REQUIRED.get(concert.genre, None)

        if any(not member.is_skilled(skills_required.get(member.__class__, [])) for member in self._get_items(band.members)):
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        return f"{band_name} gained {concert.calculate_profit():.2f}$ from the {concert.genre} concert in {concert_place}."

    @staticmethod
    def _get_item(collection, **attributes):
        return next((item for item in collection if all((getattr(item, k, None) == v for k, v in attributes.items()) if attributes else [True])), None)

    @staticmethod
    def _get_items(collection, **attributes):
        return (item for item in collection if all((getattr(item, k, None) == v for k, v in attributes.items()) if attributes else [True]))
