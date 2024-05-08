import os
import sys
import logging

logging_str = "['%(asctime)s - %(name)s - %(message)s']"

log_dir = "logs"

log_filepath = os.path.join(log_dir, "app.log")
os.makedirs(log_dir, exist_ok=True)

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter(logging_str)

# Create file handler and set formatter
file_handler = logging.FileHandler(log_filepath)
file_handler.setFormatter(formatter)

# Create stream handler and set formatter
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
