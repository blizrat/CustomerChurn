from CustomerChurn.entity.config_entity import DataValidationConfig
from CustomerChurn.logger import logging
from CustomerChurn.exception import CustomException
import pandas as pd
import sys


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_data(self):
        try:
            logging.info("Starting data validation")
            data = pd.read_csv(self.config.data_dir)
            columns = list(data.columns)
            schema_columns = self.config.all_schema.keys()

            missing_columns = [col for col in schema_columns if col not in columns]
            extra_columns = [col for col in columns if col not in schema_columns]

            validation_status = "Success"
            if missing_columns or extra_columns:
                validation_status = "Failure"
                logging.info(f"Missing Columns: {missing_columns}")
                logging.info(f"Extra Columns: {extra_columns}")

            # Write validation status to file
            with open(self.config.validation_file, "w") as f:
                f.write(f"Validation Status: {validation_status}\n")
                if missing_columns:
                    f.write(f"Missing Columns: {missing_columns}\n")
                if extra_columns:
                    f.write(f"Extra Columns: {extra_columns}\n")

            logging.info(f"Data validation completed with status: {validation_status}")

        except Exception as e:
            logging.info(f"Error during data validation: {str(e)}")
            raise CustomException(e, sys)
