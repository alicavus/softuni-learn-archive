from abc import ABC, abstractmethod

class BaseInfluencer(ABC):
    def __init__(self, username: str, followers: int, engagement_rate: float):
        self.username: str = username
        self.followers: int = followers
        self.engagement_rate: float = engagement_rate
        self.campaigns_participated: list = []

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str):
        if not value.strip():
            raise ValueError("Username cannot be empty or consist only of whitespace!")
        self._username: str = value

    @property
    def followers(self) -> int:
        return self._followers

    @followers.setter
    def followers(self, value: int):
        if value < 0:
            raise ValueError("Followers must be a non-negative integer!")
        self._followers: int = value

    @property
    def engagement_rate(self) -> float:
        return self._engagement_rate

    @engagement_rate.setter
    def engagement_rate(self, value: float):
        ENGAGEMENT_MIN_VALUE = 0.0
        ENGAGEMENT_MAX_VALUE = 5.0

        def integerify(number: float) -> int|float:
            int_num = int(number)
            float_num = float(number)
            if int_num == float_num:
                return int_num
            return  float_num

        if not ENGAGEMENT_MIN_VALUE <= value <= ENGAGEMENT_MAX_VALUE:
            raise ValueError(f"Engagement rate should be between {integerify(ENGAGEMENT_MIN_VALUE)} and {integerify(ENGAGEMENT_MAX_VALUE)}.")

        self._engagement_rate: float = value

    def calculate_payment(self, campaign):
        return self.INITIAL_PAYMENT_PERCENTAGE * campaign.budget

    @property
    @abstractmethod
    def _data(self):
        pass

    def reached_followers(self, campaign_type: str):
        return int(self._data.get(campaign_type, 0) * self.followers * self.engagement_rate)

    def display_campaigns_participated(self):
        if not self.campaigns_participated:
            return f"{self.username} has not participated in any campaigns."
        result = [f"{str(self)} :) {self.username} :) participated in the following campaigns:"]
        result.extend([
            f"  - Campaign ID: {campaign.campaign_id}, Brand: {campaign.brand}, Reached followers: {self.reached_followers(str(campaign))}" for campaign in self.campaigns_participated
        ])

        return "\n".join(result)



    @abstractmethod
    def __str__(self):
        pass

