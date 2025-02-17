from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    raw_data_dir: Path
    data_dir : Path
    raw_data_file : str

@dataclass(frozen = True)
class DataValidationConfig:
    root_dir: Path
    data_dir : Path
    validation_file: str
    all_schema : dict

@dataclass(frozen = True)
class DataTransformationConfig:
    root_dir: Path
    data_dir: Path
    scaler_path : Path
    train_data_file : str
    test_data_file : str

@dataclass(frozen = True)
class ModelTrainingConfig:
    root_dir: Path
    train_data_file: str
    model_name : str
    output_column : str
    criterion : str
    max_features : str

@dataclass(frozen = True)
class ModelEvaluatonConfig:
    root_dir: Path
    test_data_file: str
    model_path : Path
    output_column: str
    metric_file : Path
