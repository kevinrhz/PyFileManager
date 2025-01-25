import logging
from pathlib import Path


# Set up logging configuration
log_file = Path("file_manager.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_event(level, message):
    # Log an event with a given level and message
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    elif level == "debug":
        logging.debug(message)
    else:
        logging.info(f"Unknown log level: {message}")