import logging
import os

# Clear the log file at the start of the program
if os.path.exists("activity.log"):
    open("activity.log", "w").close()  # Clears the file

# Configure logging settings
logging.basicConfig(
    filename="activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log_event(event_type, message):
    logging.info(f"{event_type}: {message}")
