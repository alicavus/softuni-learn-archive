from project.influencers.base_influencer import BaseInfluencer

class PremiumInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.85

    @property
    def _data(self):
        return {
            "HighBudgetCampaign": 1.5,
            "LowBudgetCampaign": 0.8
        }

    def __str__(self):
        return "PremiumInfluencer"





