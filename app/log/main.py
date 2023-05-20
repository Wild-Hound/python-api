import logging

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("service")

file_handler_error = logging.FileHandler("errorLog.log")
file_handler_error.setLevel(logging.ERROR)

file_handler_info = logging.FileHandler("infoLog.log")
file_handler_info.setLevel(logging.DEBUG)

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
