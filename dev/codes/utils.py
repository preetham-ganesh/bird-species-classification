# authors_name = 'Preetham Ganesh'
# project_title = 'Comparison of Approaches towards Classification of Birds Species'
# email = 'preetham.ganesh2021@gmail.com'


import os
import logging
import warnings


os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
logging.getLogger("tensorflow").setLevel(logging.FATAL)
warnings.filterwarnings("ignore")


import json
import tensorflow as tf
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pandas as pd
import time

#from model import BirdSpeciesClassification


physical_devices = tf.config.list_physical_devices("GPU")
tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)


def check_directory_path_existence(home_directory_path: str, directory_path: str) -> str:
    """Creates the absolute path for the directory path given in argument if it does not already exist.

    Args:
        home_directory_path: A string which contains path for home directory.
        directory_path: A string which contains the directory path that needs to be created if it does not already
            exist.
    
    Returns:
        A string which contains the absolute directory path.
    """
    # Creates the following directory path if it does not exist.
    absolute_directory_path = "{}/{}".format(home_directory_path, directory_path)
    if not os.path.isdir(absolute_directory_path):
        os.makedirs(absolute_directory_path)
    return absolute_directory_path


def create_log(logger_directory_path: str, log_file_name: str) -> None:
    """Creates an object for logging terminal output.

    Args:
        logger_directory_path: A string which contains the location where the log file should be stored.
        log_file_name: A string which contains the name for the log file.
    
    Returns:
        None.
    """
    home_directory_path = os.path.dirname(os.getcwd())

    # Checks if the following path exists.
    logger_directory_path = check_directory_path_existence(home_directory_path, logger_directory_path)

    # Create and configure logger
    logging.basicConfig(
        filename='{}/{}'.format(logger_directory_path, log_file_name), format='%(asctime)s %(message)s', filemode='w'
    )
    global logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)


def log_information(log: str) -> None:
    """Saves current log information, and prints it in terminal.

    Args:
        log: A string which contains the information that needs to be printed in terminal and saved in log.
    
    Returns:
        None.
    
    Exception:
        NameError: When the logger is not defined, this exception is thrown.
    """
    try:
        logger.info(log)
        print(log)
    except NameError:
        _ = ''


def save_json_file(dictionary: dict, file_name: str, directory_path: str) -> None:
    """Converts a dictionary into a JSON file and saves it for future use.

    Args:
        dictionary: A dictionary which needs to be saved.
        file_name: A string which contains the name with which the file has to be saved.
        directory_path: A string which contains the path where the file needs to be saved.
    
    Returns:
        None.
    """
    # Creates the following directory path if it does not exist.
    directory_path = check_directory_path_existence(directory_path)

    # Saves the dictionary or list as a JSON file at the file path location.
    file_path = '{}/{}.json'.format(directory_path, file_name)
    with open(file_path, 'w') as out_file:
        json.dump(dictionary, out_file, indent=4)
    out_file.close()
    log_information('{} file saved successfully at {}.'.format(file_name, file_path))