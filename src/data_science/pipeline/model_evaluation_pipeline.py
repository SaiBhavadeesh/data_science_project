from src.data_science import logger
from src.data_science.config.configuration import ConfigurationManager
from src.data_science.components.model_evaluation import ModelEvaluation

STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()

if __name__ == "__main__":
    try:
        config = ConfigurationManager()
        model_evaluation_pipeline = ModelEvaluationPipeline(config=config)
        model_evaluation_pipeline.initiate_model_evaluation()
    except Exception as e:
        raise e
