import logging
import os
from datetime import datetime
from shared.ports.logger_abs import LoggerAbs


class Logger(LoggerAbs):
    def __init__(self, name="app", log_level=logging.INFO, log_file=None):
        """
        Initialize a logger for the application.

        Args:
            name (str): Logger name
            log_level (int): Logging level (e.g., logging.INFO)
            log_file (str): Path to log file. If None, logs to console only.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # Create file handler if log_file is specified
        if log_file:
            # Create logs directory if it doesn't exist
            log_dir = os.path.dirname(log_file)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir)

            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
