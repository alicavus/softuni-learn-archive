from project.campaigns.base_campaign import BaseCampaign

class LowBudgetCampaign(BaseCampaign):
    @property
    def _data(self):
        return {
            "required percent": 0.9,
            "budget": 2_500.00
        }
    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self._data["budget"], required_engagement)

    def __str__(self):
        return "LowBudgetCampaign"


