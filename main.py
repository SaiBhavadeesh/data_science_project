from src.data_science import logger
from src.data_science.pipeline.data_ingestion_pipeline import (
    DataIngestionTrainingPipeline,
)
from src.data_science.pipeline.data_validation_pipeline import (
    DataValidationPipeline,
)
from src.data_science.pipeline.data_transformation_pipeline import (
    DataTransformationPipeline,
)
from src.data_science.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.data_science.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info("-------------------------------------------")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info("-------------------------------------------")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    from src.data_science.pipeline.data_transformation_pipeline import (
        DataTransformationPipeline,
    )

    data_transformation = DataTransformationPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info("-------------------------------------------")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.initiate_model_training()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info("-------------------------------------------")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.initiate_model_evaluation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info("-------------------------------------------")
except Exception as e:
    logger.exception(e)
    raise e
