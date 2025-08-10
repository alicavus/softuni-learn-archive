from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign

class InfluencerManagerApp:
    VALID_INFLUENCERS = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer
    }
    VALID_CAMPAIGNS = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign
    }
    def __init__(self):
        self.influencers: list = []
        self.campaigns: list = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCERS:
            return f"{influencer_type} is not an allowed influencer type."

        influencer = self.get_item(self.influencers, "username", username)

        if influencer is not None:
            return f"{username} is already registered."

        self.influencers.append(self.VALID_INFLUENCERS[influencer_type](username, followers, engagement_rate))

        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."

        campaign = self.get_item(self.campaigns, "campaign_id", campaign_id)

        if campaign is not None:
            return f"Campaign ID {campaign_id} has already been created."

        self.campaigns.append(self.VALID_CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement))
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = self.get_item(self.influencers, "username", influencer_username)
        campaign = self.get_item(self.campaigns, "campaign_id", campaign_id)

        if influencer is None:
            return f"Influencer '{influencer_username}' not found."

        elif campaign is None:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        influencer_payment = influencer.calculate_payment(campaign)
        if influencer_payment > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer_payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        result = {}
        for campaign in self.campaigns:
            if not campaign.approved_influencers:
                continue
            result[campaign] = sum(i.reached_followers(str(campaign)) for i in campaign.approved_influencers)
        return result

    #helpers
    @staticmethod
    def get_items(collection, attribute_name, attribute_value):
        return (item for item in collection if getattr(item, attribute_name, None) == attribute_value)

    @staticmethod
    def get_item(collection, attribute_name, attribute_value):
        return next((item for item in collection if getattr(item, attribute_name, None) == attribute_value), None)
