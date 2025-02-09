import logging
import os
from pathlib import Path
from datetime import datetime

LOG_DIR = "logs"
PROJECT_PATH = str(Path(__file__).resolve().parents[3])
LOG_DIR = os.path.join(PROJECT_PATH, LOG_DIR)

os.makedirs(LOG_DIR, exist_ok=True)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"

log_file_path = os.path.join(LOG_DIR, file_name)

logging.basicConfig(filename=log_file_path,
                    filemode="w",
                    format = '%(asctime)s,%(msecs)03d - %(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO)