from src.data_science.config.configuration import ConfigurationManager
from src.data_science.components.data_ingestion import DataIngestion
from src.data_science import logger

STAGE_NAME = "Data Ingestion"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
