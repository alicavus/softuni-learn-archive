from project.artifacts import BaseArtifact, ContemporaryArtifact, RenaissanceArtifact
from project.collectors import BaseCollector, Museum, PrivateCollector

class AuctionHouseManagerApp:
    VALID_ARTIRACTS = {
        "RenaissanceArtifact": RenaissanceArtifact,
        "ContemporaryArtifact": ContemporaryArtifact
    }
    VALID_COLLECTORS = {
        "Museum": Museum,
        "PrivateCollector": PrivateCollector
    }
    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []

    
    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int) -> str:
        self.register_items(self.artifacts, "artifact", self.VALID_ARTIRACTS, artifact_type, "name", artifact_name, artifact_price, artifact_space)
        # if artifact_type not in self.VALID_ARTIRACTS:
        #     raise ValueError("Unknown artifact type!")
        # if next(self.get_items(self.artifacts, "name", artifact_name)):
        #     raise ValueError(f"{artifact_name} has been already registered!")
        # artifact = self.VALID_ARTIRACTS[artifact_type](artifact_name, artifact_price, artifact_space)
        # self.artifacts.append(artifact)

        return f"{artifact_name} is successfully added to the auction as {artifact_type}."
    
    def register_collector(self, collector_type: str, collector_name: str) -> str:
        self.register_items(self.collectors, "collector", self.VALID_COLLECTORS, collector_type, "name", collector_name)
        # if collector_type not in self.VALID_COLLECTORS:
        #     raise ValueError("Unknown collector type!")
        # if next(self.get_items(self.collectors, "name", collector_name)):
        #     raise ValueError(f"{collector_name} has been already registered!")
        
        # collector = self.VALID_COLLECTORS[collector_type](collector_name)

        # self.collectors.append(collector)  

        return f"{collector_name} is successfully registered as a {collector_type}."
    
    def perform_purchase(self, collector_name: str, artifact_name: str) -> str:
        collector: BaseCollector = next(self.get_items(self.collectors, "name", collector_name), None)
        artifact: BaseArtifact = next(self.get_items(self.artifacts, "name", artifact_name), None)

        if collector is None:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")
        
        if artifact is None:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")
        
        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."
        
        self.artifacts.remove(artifact)

        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required

        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."
    
    def remove_artifact(self, artifact_name: str) -> str:
        artifact: BaseArtifact = next(self.get_items(self.artifacts, "name", artifact_name), None)

        if artifact is None:
            return "No such artifact."
        
        self.artifacts.remove(artifact)

        return f"Removed {artifact.artifact_information()}"
    
    def fundraising_campaigns(self, max_money: float) -> str:
        fundraised_collectors = [collector.increase_money() for collector in self.collectors if collector.available_money <= max_money]
        return f"{len(fundraised_collectors)} collector/s increased their available money."
    
    def get_auction_report(self) -> str:
        collectors = sorted(self.collectors, key=lambda collector: (-len(collector.purchased_artifacts), collector.name))
        result = [
            "**Auction statistics**",
            f"Total number of sold artifacts: {sum([len(collector.purchased_artifacts) for collector in self.collectors]) if self.collectors else 0}",
            f"Available artifacts for sale: {len(self.artifacts)}",
            "***"
        ]
        result.extend([collector.__str__() for collector in collectors])

        return "\n".join(result)

    #helpers
    @staticmethod
    def get_items(collection: list, attribute: str, value):
        return (item for item in collection if getattr(item, attribute, None) == value)
    
    @staticmethod
    def register_items(collection: list, collection_type: str,  valid_dict: dict, attribute_type: str, attribute_name: str, attribute_value, *args):
        if attribute_type not in valid_dict:
            raise ValueError(f"Unknown {collection_type} type!")
        if next(__class__.get_items(collection, attribute_name, attribute_value), None) is not None:
            raise ValueError(f"{attribute_value} has been already registered!")
        
        new_item = valid_dict[attribute_type](attribute_value, *args)

        collection.append(new_item)

