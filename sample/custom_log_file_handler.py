import logging
import logging.config
import sample.othermod as om
from sample.othermod import add
from sample.othermod import mult

# logging.config.fileConfig('logging.conf')
# logging.config.fileConfig(disable_existing_loggers=False, fname='resources/logging.conf')
logging.config.fileConfig(disable_existing_loggers=False, fname='../resources/fileh.conf')
# logging.config.fileConfig(disable_existing_loggers=False, fname='/Users/arunangsusahunarayan7/LogConfiguration/logging.conf')
# D:\Python_Projects\LogBestPracticesPython\resources\fileh.conf
# create logger
logger = logging.getLogger(__name__)


def do_calculation() -> object:
    """
    The main entry point of the application
    :rtype: object
    """
    # logging.basicConfig(filename="mySnake21.log", level=logging.INFO)
    logger.info("Program started")
    result = add(7, 8)
    logger.info("**********Done!**********  {}".format(result))
    result1 = mult(7, 8)
    logger.info("Done! {}".format(result1))
    logger.debug("**********Done!********** {}".format(result1))
    result2 = om.sub(9, 3)
    logger.debug("*********Done!*********** {}".format(result2))


do_calculation()

# 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')

