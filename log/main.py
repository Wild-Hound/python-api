import logging
from datetime import datetime

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("service")
formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")
today = datetime.today()

file_handler_error = logging.FileHandler(
    f"log/{today.day:02d}-{today.month:02d}-{today.year}-errorLog.log")
file_handler_error.setLevel(logging.ERROR)
file_handler_error.setFormatter(formatter)

file_handler_info = logging.FileHandler(
    f"log/{today.day:02d}-{today.month:02d}-{today.year}-infoLog.log")
file_handler_info.setLevel(logging.DEBUG)
file_handler_info.setFormatter(formatter)

logger.addHandler(file_handler_error)
logger.addHandler(file_handler_info)


def logDebug(message: str):
    logger.debug(message)


def logInfo(message: str):
    logger.info(message)


def logWarning(message: str):
    logger.warning(message)


def logError(message: str):
    logger.error(message)


def logCritical(message: str):
    logger.critical(message)
    exit()
