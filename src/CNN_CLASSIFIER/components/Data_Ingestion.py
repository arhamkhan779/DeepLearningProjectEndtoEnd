import os
import urllib.request as request
import zipfile
import gdown
from CNN_CLASSIFIER import logger
from CNN_CLASSIFIER.utils.common import get_size
from CNN_CLASSIFIER.entity.config_entity import DataIngstionConfig

class DataIngestion:
    def __init__(self,config:DataIngstionConfig):
        self.config=config

    def download_file(self) -> str:
        '''
        Fetch Data From URL
        '''
        try:
            dataset_url=self.config.source_url
            zip_download_dir=self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            logger.info(f"Downloading Data from {dataset_url} into {zip_download_dir}")

            file_id=dataset_url.split('/')[5]
            prefix="https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix+file_id,zip_download_dir)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        '''
        zip_file_path:str
        This funcion will be responsible 
        to unzip data directory
        '''
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)