class DVD:
    def __init__(self, name: str, dvd_id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name: str = name
        self.id: int = dvd_id
        self.creation_year: int = creation_year
        self.creation_month: str = creation_month
        self.age_restriction: int = age_restriction
        self.is_rented = False
    

    @classmethod
    def from_date(cls, dvd_id: int, name: str, date: str, age_restriction: int):
        MONTHS = ["January", "February", "March", "April", "May", "June",
                           "July", "August", "September", "October", "November", "December" ]
        _, creation_month, creation_year = map(int, date.split("."))
        return cls(name, dvd_id, creation_year, MONTHS[creation_month-1], age_restriction)
    
    def __repr__(self) -> str:
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {'' if self.is_rented else 'not '}rented"



