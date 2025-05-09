from src.data_science import logger
from src.data_science.config.configuration import ConfigurationManager
from src.data_science.components.data_validation import DataValidation

STAGE_NAME = "Data Validation"


class DataValidationPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
