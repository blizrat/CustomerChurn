from pathlib import Path

# data location
ROOT_DIR_KEY = str(Path(__file__).resolve().parents[3])
DATA_DIR = "Data"
DATA_DIR_KEY = "data.csv"

# Artifacts dir
ARTIFACTS_DIR_KEY = "Artifacts"

# Data Ingestion variables
DATA_INGESTION_KEY = "data_ingestion"
DATA_INGESTION_RAW_DATA_DIR = "raw_data_dir"
DATA_INGESTION_INGESTED_DATA_DIR_KEY = "ingested_dir"
RAW_DATA_DIR_KEY = "raw.csv"
TRAIN_DATA_DIR_KEY = "train.csv"
TEST_DATA_DIR_KEY = "test.csv"