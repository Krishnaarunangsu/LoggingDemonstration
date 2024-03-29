import logging
import logging.config
from sample.othermod import add
from sample.othermod import mult

# logging.config.fileConfig('logging.conf')
logging.config.fileConfig(disable_existing_loggers=False, fname='../resources/logging3.conf')

# create logger
logger = logging.getLogger(__name__)


def gtg() -> object:
    """
    The main entry point of the application
    :rtype: object
    """
    # logging.basicConfig(filename="mySnake21.log", level=logging.INFO)
    logger.info("Program started")
    result = add(7, 8)
    logger.info("Done! {}".format(result))
    result1 = mult(7, 8)
    logger.info("Done! {}".format(result1))
    logger.debug( "********************Done! {}".format ( result1 ) )


gtg()

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

