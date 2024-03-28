import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception


import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path # we use to create a system independent path

@dataclass
class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test_csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Started")
        try:
            data=pd.read_csv("C:\\Users\\aadit\\Downloads\\playground-series-s3e8\\train.csv")
            logging.info("Reading a dataframe")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)))
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Saved the raw data in artifacts folder")

            logging.info("Here I preform the train test split")

            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("Train test split completed")

            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info("Data ingestion part completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )


        except Exception as e:
            logging.info()
            raise customexception(e,sys)
        


if __name__=='__main__':
    obj=DataIngestion()

    obj.initiate_data_ingestion()