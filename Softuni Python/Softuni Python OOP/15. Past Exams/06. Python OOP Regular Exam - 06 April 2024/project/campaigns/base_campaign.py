from abc import ABC, abstractmethod

class BaseCampaign(ABC):
    _unique_ids = set()
    def __init__(self, campaign_id: int, brand: str, budget: float, required_engagement: float):
        self.campaign_id: int = campaign_id
        self.brand: str = brand
        self.budget: float = budget
        self.required_engagement: float = required_engagement
        self.approved_influencers: list = []
    
    @property
    def campaign_id(self) -> int:
        return self._campaign_id
    
    @campaign_id.setter
    def campaign_id(self, value):
        if value <= 0:
            raise  ValueError("Campaign ID must be a positive integer greater than zero.")
        if value in self.__class__._unique_ids:
            raise ValueError(f"Campaign with ID {value} already exists. Campaign IDs must be unique.")
        self.__class__._unique_ids.add(value)
        self._campaign_id = value

    @property
    @abstractmethod
    def _data(self):
        pass

    def check_eligibility(self, engagement_rate: float) -> bool:
        return self.required_engagement * self._data["required percent"] <= engagement_rate

    @abstractmethod
    def __str__(self):
        pass
