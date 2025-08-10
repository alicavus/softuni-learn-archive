from project.artifacts.base_artifact import BaseArtifact

class RenaissanceArtifact(BaseArtifact):
    def __init__(self, name: str, price: float, space_required: int):
        super().__init__(name, price, space_required)
    
    @property
    def _artifact_type(self) -> str:
        return "Renaissance Artifact"