from src.data_science import logger
from src.data_science.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(
        f"===================== Stage: {STAGE_NAME} started ====================="
    )
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initial_data_ingestion()
    logger.info(
        f"===================== Stage: {STAGE_NAME} completed ====================="
    )
except Exception as e:
    logger.exception(e)
    raise e
