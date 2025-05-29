from typing import Dict, Any
from .BaseModel import BaseModel
from .ModelWrapper import ModelWrapper

class ModelFactory:
    @staticmethod
    def build(config: Dict[str, Any]) -> BaseModel:
        return ModelWrapper(
            model_type=config["type"],
            features=config["features"],
            hyperparams=config.get("hyperparameters", {}),
            model_path=config["model_path"]
        )
