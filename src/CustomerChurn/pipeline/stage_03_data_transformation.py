from CustomerChurn.components.data_transformation import  *
from CustomerChurn.constants import *
from CustomerChurn.config.configuration import ConfigurationManager

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager(config_filepath= CONFIG_FILE_PATH,
                                      schema_filepath= SCHEMA_FILE_PATH,
                                      params_filepath= PARAMS_FILE_PATH)
        data_transformation_obj = DataTransformation(config.get_data_transformation_config())
        data_transformation_obj.transform_data()