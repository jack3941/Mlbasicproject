from src.MLproject.logger import logging 
from src.MLproject.exception import CustomException
from src.MLproject.components.data_ingestion  import DataIngestion
from src.MLproject.components.data_ingestion  import DataIngestionConfig
import sys 




if __name__ =="__main__":
    logging.info("execution started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
    