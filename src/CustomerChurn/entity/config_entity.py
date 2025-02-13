from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    raw_data_dir: Path
    data_dir : Path

@dataclass(frozen = True)
class DataValidationConfig:
    root_dir: Path
    data_dir : Path
    validation_file: str
    all_schema : dict

