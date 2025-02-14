from CustomerChurn.logger import logging
from CustomerChurn.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from CustomerChurn.pipeline.stage_02_data_ingestion import DataValidationPipeline
from CustomerChurn.pipeline.stage_03_data_transformation import DataTransformationPipeline
from CustomerChurn.pipeline.stage_04_model_training import ModelTrainingPipeline
from CustomerChurn.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = DataIngestionPipeline()
   data_ingestion.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.info(e)
        raise e

STAGE_NAME = "Data Validation stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_validation = DataValidationPipeline()
   data_validation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.info(e)
        raise e

STAGE_NAME = "Data Transformation stage"
try :
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.info(e)
    raise e

STAGE_NAME = "Model Training stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.info(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.info(e)
    raise e
