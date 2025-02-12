from CustomerChurn.constants import *
from CustomerChurn.utils.common import read_yaml, create_directories
from CustomerChurn.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                 config_filepath : CONFIG_FILE_PATH,
                 schema_filepath : SCHEMA_FILE_PATH,
                 params_filepath : PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        #self.schema = read_yaml(schema_filepath)
        #self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        data_ingestion_config = self.config.data_ingestion

        create_directories([data_ingestion_config.root_dir])

        data_ingestion_config_obj = DataIngestionConfig(root_dir= data_ingestion_config.root_dir,
                                                        source_url= data_ingestion_config.source_url,
                                                        raw_data_dir= data_ingestion_config.raw_data_dir,
                                                        data_dir = data_ingestion_config.data_dir)
        return data_ingestion_config_obj

