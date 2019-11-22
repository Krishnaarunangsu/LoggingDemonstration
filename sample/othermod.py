import logging
import logging.config
# from Logging3 import logger
from logging import Logger

# logging.config.fileConfig(disable_existing_loggers = False, fname='logging.conf')
#logging.config.fileConfig(disable_existing_loggers=False, fname='logging1.conf')
logger = logging.getLogger(__name__)
# logger: Logger = logging.getLogger(__name__)


def add(x: int, y: int) -> object:
    """
    Add two numbers

    :rtype: object
    :type x: object
    :type y: object

    """
    # logger.info("added %s and %s to get %s" % (x, y, x + y))
    logger.info("added %s and %s to get %s" % (x, y, x + y))
    logger.warning('Learn More')
    return x + y


def sub(x: int, y: int) -> object:
    """
    Subtract two numbers
    
    :rtype: object
    :type x: object
    :type y: object

    """
    # logger.info("added %s and %s to get %s" % (x, y, x + y))
    logger.info("subtracted %s from %s to get %s" % (x, y, x - y))
    logger.warning('Learn More')
    return x - y


def mult(x: object, y: object) -> object:
    """
    Multiplies two numbers
    :rtype: object
    :type x: object
    :type y: object
    """
    # logger.info("added %s and %s to get %s" % (x, y, x + y))
    logger.info("multiplied %s and %s to get %s" % (x, y, x * y))
    logger.debug('Learn More:{}'.format(x * y))
    return x * y

# add(3, 6)
