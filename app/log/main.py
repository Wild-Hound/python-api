import logging

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

logging.basicConfig(level=logging.DEBUG)


def logDebug(message: str):
    logging.debug(message)


def logInfo(message: str):
    logging.info(message)


def logWarning(message: str):
    logging.warning(message)


def logError(message: str):
    logging.error(message)


def logCritical(message: str):
    logging.critical(message)
