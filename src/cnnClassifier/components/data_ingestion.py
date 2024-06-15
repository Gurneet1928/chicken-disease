import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        Args:
            url: str
            Download the file from the given URL
        Returns:
            None (only logs the file download status)
        """
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} Downloaded!! With the Following Header: {header}")
        else:
            logger.info(f"File already exists of size: {get_size(self.config.local_data_file)}")

    def extract_zip_file(self):
        """
        Arg:
            zip_file_path: str
            Extracts the zip file into the data directoruy
        Returns:
            None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

