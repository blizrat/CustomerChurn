from CustomerChurn.entity.config_entity import ModelEvaluatonConfig
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from CustomerChurn.utils.common import save_json
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config: ModelEvaluatonConfig):
        self.config = config

    def eval_metrics(self):
        test_data = pd.read_csv(self.config.test_data_file)
        test_x = test_data.drop([self.config.output_column], axis=1)
        test_y = test_data[self.config.output_column]

        model = joblib.load(self.config.model_path)
        predictions = model.predict(test_x)

        metrics = {
            "accuracy": accuracy_score(test_y, predictions),
            "precision": precision_score(test_y, predictions),
            "recall": recall_score(test_y, predictions),
            "f1_score": f1_score(test_y, predictions)
        }

        # Save metrics to JSON file
        save_json(path = Path(self.config.metric_file), data = metrics)