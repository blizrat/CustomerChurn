from CustomerChurn.entity.config_entity import DataTransformationConfig
from CustomerChurn.logger import logging
from CustomerChurn.exception import CustomException
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import sys

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transform_data(self):
        data = pd.read_csv(self.config.data_dir)

        #dropping irrelevant features
        data.drop(['RowNumber', 'CustomerId', 'Surname'], inplace=True, axis=1)

        #encoding remaining categorical features
        categorical_cols = ['Geography', 'Gender']
        encoded_df = pd.get_dummies(data[categorical_cols], drop_first=True, dtype=int)
        data = data.join(encoded_df)
        data.drop(categorical_cols, axis=1, inplace=True)

        #feature scaling numeric data with high deviation
        scaler = RobustScaler()
        columns_to_scale = ['EstimatedSalary', 'Balance', 'CreditScore']
        data[columns_to_scale] = scaler.fit_transform(data[columns_to_scale])

        #splitting data into train and test set
        train, test = train_test_split(data)

        #saving the train-test files
        train.to_csv(self.config.train_data_file, index=False)
        test.to_csv(self.config.test_data_file, index=False)
