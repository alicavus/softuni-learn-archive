from project.campaigns.base_campaign import BaseCampaign

class HighBudgetCampaign(BaseCampaign):
    @property
    def _data(self):
        return {
            "required percent": 1.2,
            "budget": 5_000.00
        }

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self._data["budget"], required_engagement)

    def __str__(self):
        return "HighBudgetCampaign"
