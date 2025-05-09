from src.data_science import logger
from src.data_science.components.model_trainer import ModelTrainer
from src.data_science.config.configuration import ConfigurationManager

STAGE_NAME = "Model Trainer"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
