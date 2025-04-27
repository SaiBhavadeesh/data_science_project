import os
import zipfile
import urllib.request as requests
from src.data_science import logger
from src.data_science.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # Downloading the zip file from the source URL
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = requests.urlretrieve(
                self.config.source_URL, self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: {headers}")
        else:
            logger.info(f"File already exists at {self.config.local_data_file}")

    def extract_zip_file(self):
        """
        zip_file_path = str
        Extract the zip file into the data directory
        Function returns None
        """
        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_dir)
            logger.info(f"Extracted all the files in {unzip_dir}")

    def __repr__(self) -> str:
        return f"DataIngestion({self.config})"
