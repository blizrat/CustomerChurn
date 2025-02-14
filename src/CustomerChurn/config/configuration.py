from CustomerChurn.constants import *
from CustomerChurn.utils.common import read_yaml, create_directories
from CustomerChurn.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, \
    ModelTrainingConfig, ModelEvaluatonConfig


class ConfigurationManager:
    def __init__(self,
                 config_filepath : CONFIG_FILE_PATH,
                 schema_filepath : SCHEMA_FILE_PATH,
                 params_filepath : PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.schema = read_yaml(schema_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        data_ingestion_config = self.config.data_ingestion

        create_directories([data_ingestion_config.root_dir])

        data_ingestion_config_obj = DataIngestionConfig(root_dir= data_ingestion_config.root_dir,
                                                        source_url= data_ingestion_config.source_url,
                                                        raw_data_dir= data_ingestion_config.raw_data_dir,
                                                        data_dir = data_ingestion_config.data_dir,
                                                        raw_data_file= data_ingestion_config.raw_data_file)

        return data_ingestion_config_obj

    def get_data_validation_config(self) -> DataValidationConfig:
        data_validation_config = self.config.data_validation
        data_validation_schema = self.schema.COLUMNS

        create_directories([data_validation_config.root_dir])

        data_validation_obj = DataValidationConfig(root_dir = data_validation_config.root_dir,
                                             data_dir = data_validation_config.data_dir,
                                             validation_file = data_validation_config.validation_file,
                                             all_schema = data_validation_schema)

        return data_validation_obj

    def get_data_transformation_config(self) -> DataTransformationConfig:
        data_transformation_config = self.config.data_transformation

        create_directories([data_transformation_config.root_dir])

        data_transformation_obj = DataTransformationConfig(root_dir = data_transformation_config.root_dir,
                                                           data_dir = data_transformation_config.data_dir,
                                                           test_data_file= data_transformation_config.test_data_file,
                                                           train_data_file= data_transformation_config.train_data_file)

        return data_transformation_obj

    def get_model_training_config(self) -> ModelTrainingConfig:
        model_training_config = self.config.model_training
        model_training_output = self.schema.OUTPUT
        model_training_params = self.params.RandomForestClassifier

        create_directories([model_training_config.root_dir])

        model_training_obj = ModelTrainingConfig(root_dir = model_training_config.root_dir,
                                                 train_data_file= model_training_config.train_data_file,
                                                 model_name = model_training_config.model_name,
                                                 output_column= model_training_output.name,
                                                 criterion= model_training_params.criterion,
                                                 max_features= model_training_params.max_features)

        return model_training_obj

    def get_model_evaluation_config(self) -> ModelEvaluatonConfig:
        model_evaluation_config = self.config.model_evaluation
        model_evaluation_output =  self.schema.OUTPUT

        create_directories([model_evaluation_config.root_dir])
        model_evaluation_obj = ModelEvaluatonConfig(root_dir = model_evaluation_config.root_dir,
                                                    test_data_file= model_evaluation_config.test_data_file,
                                                    output_column= model_evaluation_output.name,
                                                    model_path=model_evaluation_config.model_path,
                                                    metric_file= model_evaluation_config.metric_file)

        return model_evaluation_obj

