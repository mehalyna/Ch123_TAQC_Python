import logging
import os.path
import time
import datetime
import os



class LoggerConfig(object):
    def __init__(self, logger):
        """
        Specify the file path to save the log, log level, and call file
                        Save the log to the specified file and set level
        """
        #  Create a logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        if not os.path.isdir("folder_for_logs"):
            os.mkdir("folder_for_logs")

        #  Create a handler to write to the log file
        time_set = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))

        log_path = os.path.dirname(os.getcwd()) + '/tests/' + '/folder_for_logs/'
        log_name = log_path + time_set + '.log'
        log_handler = logging.FileHandler(log_name)
        log_handler.setLevel(logging.INFO)

        #  Define the output format of the handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_handler.setFormatter(formatter)

        #  Add handler to logger
        self.logger.addHandler(log_handler)

    def get_log(self):
        return self.logger



