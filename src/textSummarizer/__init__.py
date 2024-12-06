from datetime import datetime
import logging
import os

# setting name to log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# print(f"LOG_FILE = {LOG_FILE}")

# log path where file will be saved
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# print(f"log_path = {log_path}")

# if log folder does not exists create one
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# print(f"LOG_FILE_PATH = {LOG_FILE_PATH}")

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)