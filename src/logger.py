import logging 
import os # used for file path operations
import sys # used for system-specific parameters and functions
from datetime import datetime # used for date and time operations
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # log file name with timestamp
logs_path=os.path.join(os.getcwd(),"logs") # directory path for logs
LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE) # full path to log file

os.makedirs(logs_path, exist_ok=True) # create logs directory if it doesn't exist

logging.basicConfig(
level=logging.INFO, 
filename=LOG_FILE_PATH, 
format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'
)
# logger = logging.getLogger(__name__)    
if __name__ == "__main__":
    logging.info("Logging has started")
    logging.warning("This is a warning message")
    logging.error("This is an error message")