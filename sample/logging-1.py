import argparse
import datetime
import errno
import logging
import os
import re
import sys
import yaml
#from xlrd import open_workbook
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
#from safetypy import safetypy as sp

# Possible values here are DEBUG, INFO, WARN, ERROR and CRITICAL
LOG_LEVEL = logging.DEBUG

DEFAULT_CONFIG_FILENAME = 'config.yaml'


def configure_logging(path_to_log_directory):
    """
    Configure logger
    :param path_to_log_directory:  path to directory to write log file in
    :return:
    """
    log_filename = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
    importer_logger = logging.getLogger('importer_logger')
    importer_logger.setLevel(LOG_LEVEL)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')

    fh = logging.FileHandler(filename=os.path.join(path_to_log_directory, log_filename))
    fh.setLevel(LOG_LEVEL)
    fh.setFormatter(formatter)
    importer_logger.addHandler(fh)

    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(LOG_LEVEL)
    sh.setFormatter(formatter)
    importer_logger.addHandler(sh)


def log_critical_error(logger, ex, message):
    """
    Logs the exception at 'CRITICAL' log level
    :param logger:  the logger
    :param ex:      exception to log
    :param message: descriptive message to log details of where/why ex occurred
    """
    if logger is not None:
        logger.critical(message)
        logger.critical(ex)


def create_directory_if_not_exists(logger, path):
    """
    Creates 'path' if it does not exist
    If creation fails, an exception will be thrown
    :param logger:  the logger
    :param path:    the path to ensure it exists
    """
    try:
        os.makedirs(path)
    except OSError as ex:
        if ex.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            log_critical_error(logger, ex, 'An error happened trying to create ' + path)
            raise


def configure_logger():
    """
    Declare and validate existence of log directory; create and configure logger object
    :return:  instance of configured logger object
    """
    log_dir = os.path.join(os.getcwd(), 'log')
    create_directory_if_not_exists(None, log_dir)
    configure_logging(log_dir)
    logger = logging.getLogger('importer_logger')
    return logger





def main():
    """
    Load local response_set data, get remote response_set data, compare and reconcile
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True)
    parser.add_argument('-t', '--token', required=True)
    args = parser.parse_args()
    file_path = args.file
    api_token = args.token

    logger = configure_logger()





if __name__ == '__main__':
    main()
