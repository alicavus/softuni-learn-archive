from project.influencers.base_influencer import BaseInfluencer

class StandardInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.45

    @property
    def _data(self):
        return {
            "HighBudgetCampaign": 1.2,
            "LowBudgetCampaign": 0.9
        }

    def __str__(self):
        return "PremiumInfluencer"


