from CustomerChurn.constants import *
from CustomerChurn.components import model_evaluation
from CustomerChurn.config.configuration import  ConfigurationManager

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager(config_filepath= CONFIG_FILE_PATH,
                                      params_filepath= PARAMS_FILE_PATH,
                                      schema_filepath= SCHEMA_FILE_PATH)

        model_evaluation_obj = model_evaluation.ModelEvaluation(config.get_model_evaluation_config())
        model_evaluation_obj.eval_metrics()
