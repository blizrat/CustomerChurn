from CustomerChurn.config.configuration import *
from CustomerChurn.logger import logging
from CustomerChurn.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path:str = RAW_FILE_PATH
    test_data_path: str = TEST_FILE_PATH
    train_data_path:str = TRAIN_FILE_PATH


class DataIngestion:
    def __init__(self):
        self.DataIngestionConfig = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv(DATASET_PATH)

            os.makedirs(os.path.dirname(self.DataIngestionConfig.raw_data_path), exist_ok=True)
            df.to_csv(self.DataIngestionConfig.raw_data_path, index=False)

            train_set, test_set = train_test_split(df, test_size= 20, random_state= 42)

            os.makedirs(os.path.dirname(self.DataIngestionConfig.train_data_path), exist_ok=True)
            train_set.to_csv(self.DataIngestionConfig.train_data_path, header= True)

            os.makedirs(os.path.dirname(self.DataIngestionConfig.test_data_path), exist_ok=True)
            test_set.to_csv(self.DataIngestionConfig.test_data_path, header= True)

            return(
                self.DataIngestionConfig.raw_data_path,
                self.DataIngestionConfig.train_data_path,
                self.DataIngestionConfig.test_data_path
            )

        except Exception as e:
           cust_exp = CustomException(e, sys)
           logging.info(cust_exp.error_message)

if __name__ == '__main__':
    obj = DataIngestion()
    raw_data, train_data, test_data = obj.initiate_data_ingestion()
