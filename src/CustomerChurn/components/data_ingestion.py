import os
from CustomerChurn.logger import logging
import pandas as pd
from CustomerChurn.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config : DataIngestionConfig):
        self.config = config

    def load_data(self):
        df = pd.read_csv(self.config.data_dir)

        os.makedirs(self.config.raw_data_dir, exist_ok= True)
        df.to_csv(os.path.join(self.config.raw_data_dir, "raw_data.csv"), index = False)
