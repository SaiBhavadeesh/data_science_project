from pathlib import Path
from src.data_science import logger
from src.data_science.config.configuration import ConfigurationManager
from src.data_science.components.data_transformation import DataTransformation

STAGE_NAME = "Data Transformation"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as file:
                status = bool(file.read().split(" ")[-1])
            if status:
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Data scheme is not valid. Please check the data validation stage.")
        except Exception as e:
            raise e
