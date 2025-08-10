from project.room import Room

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.guests = 0
        self.rooms: list[Room] = []
    
    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")
    
    def add_room(self, room: Room):
        self.rooms.append(room)
    
    def find_room(self, room_number: int) -> Room:
        return next((room for room in self.rooms if room.number == room_number), None)
    
    def take_room(self, room_number: int, people: int):
        room = self.find_room(room_number)
        if room:
            room = room.take_room(people)
            if isinstance(room, Room):
                self.guests += room.guests
    
    def free_room(self, room_number: int):
        room = self.find_room(room_number)
        if room:
            cnt = room.guests
            room.free_room()
            if isinstance(room, Room):
                self.guests -= cnt
    
    def status(self) -> str:
        res = [f"Hotel {self.name} has {self.guests} total guests"]
        res += [f"Free rooms: {', '.join(map(str, [room.number for room in self.rooms if not room.is_taken]))}"]
        res += [f"Taken rooms: {', '.join(map(str, [room.number for room in self.rooms if room.is_taken]))}"]

        return "\n".join(res)