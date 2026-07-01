import logging
from logging.handlers import RotatingFileHandler
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

LOG_FILE = "logs/app.log"
print("LOG FILE PATH:", os.path.abspath(LOG_FILE))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        RotatingFileHandler(
            LOG_FILE,
            maxBytes=5 * 1024 * 1024,  # 5 MB
            backupCount=3
        ),
        logging.StreamHandler()  # still prints to terminal
    ],
)

logger = logging.getLogger("fastapi-app")
