from CustomerChurn.config.configuration import ConfigurationManager
from CustomerChurn.components import model_training
from CustomerChurn.constants import *

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager(config_filepath= CONFIG_FILE_PATH,
                                      params_filepath= PARAMS_FILE_PATH,
                                      schema_filepath= SCHEMA_FILE_PATH)

        model_training_obj = model_training.ModelTraining(config.get_model_training_config())
        model_training_obj.train()

