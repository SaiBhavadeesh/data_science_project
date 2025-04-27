from src.data_science import logger
from src.data_science.pipeline.data_ingestion_pipeline import (
    DataIngestionTrainingPipeline,
)
from src.data_science.pipeline.data_validation_pipeline import (
    DataValidationPipeline,
)


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info("-------------------------------------------")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info("-------------------------------------------")
except Exception as e:
    logger.exception(e)
    raise e
