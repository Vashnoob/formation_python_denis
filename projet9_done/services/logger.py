
import logging
from pathlib import Path

log_path = Path(__file__).parent.parent / "logs" / "actions.log"
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
