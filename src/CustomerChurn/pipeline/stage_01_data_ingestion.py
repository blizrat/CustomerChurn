from CustomerChurn.config.configuration import ConfigurationManager
from CustomerChurn.constants import *
from CustomerChurn.components.data_ingestion import  *


STAGE_NAME : "DATA INGESTION"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config_obj = ConfigurationManager(CONFIG_FILE_PATH, SCHEMA_FILE_PATH, PARAMS_FILE_PATH)
        components_obj = DataIngestion(config_obj.get_data_ingestion_config())
        components_obj.load_data()