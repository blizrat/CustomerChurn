from CustomerChurn.entity.config_entity import ModelTrainingConfig
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
import pandas as pd

class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_file)

        x_train = train_data.drop([self.config.output_column], axis = 1)
        y_train = train_data[self.config.output_column]

        model = RandomForestClassifier(criterion= self.config.criterion, max_features= self.config.max_features)
        model.fit(x_train, y_train)

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))