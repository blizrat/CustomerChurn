from CustomerChurn.config.configuration import ConfigurationManager
from CustomerChurn.constants import *
from CustomerChurn.components.data_validation import  *


STAGE_NAME : "DATA VALIDATION"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config_obj = ConfigurationManager(CONFIG_FILE_PATH, SCHEMA_FILE_PATH, PARAMS_FILE_PATH)
        components_obj = DataValidation(config_obj.get_data_validation_config())
        components_obj.validate_data()