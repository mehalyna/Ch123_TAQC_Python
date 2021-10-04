import logging
import os.path
import time
import datetime
import os
import Logs


class LoggerConfig(object):
    def __init__(self, logger):
        """
        Specify the file path to save the log, log level, and call file
                        Save the log to the specified file
        """
        #  Create a logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #  Create a handler to write to the log file
        time_set = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = (os.path.dirname(os.getcwd())).join('/Logs/')
        log_name = (log_path).join(time_set).join('.log')
        log_handler = logging.FileHandler(log_name)
        log_handler.setLevel(logging.INFO)

        #  Create another handler for output to the console
        log_to_console = logging.StreamHandler()
        log_to_console.setLevel(logging.INFO)

        #  Define the output format of the handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_handler.setFormatter(formatter)
        log_to_console.setFormatter(formatter)

        #  Add handler to logger
        self.logger.addHandler(log_handler)
        self.logger.addHandler(log_to_console)

    def getlog(self):
        return self.logger

    def delete_log(self):
        for files in os.listdir("Logs"):
            year_of_log = int(files[:4])
            month_of_log = int(files[4:6])
            day_of_log = int(files[6:8])
            date_of_log = datetime.date(year_of_log, month_of_log, day_of_log)
            if datetime.date.today() - date_of_log >= 7:
                name_log = 'Logs/'.join(str(files))
                os.remove(name_log)
