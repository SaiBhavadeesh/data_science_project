import os
import pandas as pd
from src.data_science import logger
from sklearn.model_selection import train_test_split
from src.data_science.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        train_set, test_set = train_test_split(data)
        train_set.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test_set.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        logger.info("Splitting data into train and test sets")
        logger.info(train_set.shape)
        logger.info(test_set.shape)