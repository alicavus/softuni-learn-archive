

class Route:
    def __init__(self, start_point: str, end_point: str, length: float, route_id: int):
        self.start_point: str = start_point
        self.end_point: str = end_point
        self.length: float = length
        self.route_id: int = route_id
        self.is_locked: bool = False

    @property
    def start_point(self) -> str:
        return self._start_point

    @start_point.setter
    def start_point(self, value: str):
        if not value.strip():
            raise ValueError("Start point cannot be empty!")
        self._start_point: str = value

    @property
    def end_point(self) -> str:
        return self._end_point

    @end_point.setter
    def end_point(self, value: str):
        if not value.strip():
            raise ValueError("End point cannot be empty!")
        self._end_point: str = value
    
    @property
    def length(self) -> float:
        return self._length
    
    @length.setter
    def length(self, value):
        LENGTH_MIN_VALUE = 1.0
        if value < LENGTH_MIN_VALUE:
            raise ValueError(f"Length cannot be less than {LENGTH_MIN_VALUE:.2f} kilometer!")
        self._length: float = value


