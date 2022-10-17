import logging
import os
from pathlib import Path


class Logger:
    def __init__(self, level, message, logger_name):

        levels = {'info', 'error', 'warning', 'debug', 'critical'}

        if level not in levels:
            logging.error(f'level should be one of those options: {levels}')
            return

        self.file_handler = logging.FileHandler(f'{Path(__file__).parent.parent}/logs/{level}.log')
        self.logger = logger_name
        self.formatter = logging.Formatter('%(levelname)s: %(asctime)s: %(name)s , line %(lineno)d : %(message)s ')
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

        if level == 'error':
            self.logger.setLevel(logging.ERROR)
            self.logger.error(message)

        elif level == 'info':
            self.logger.setLevel(logging.INFO)
            self.logger.info(message)

        elif level == 'warning':
            self.logger.setLevel(logging.WARNING)
            self.logger.warning(message)

        elif level == 'debug':
            self.logger.setLevel(logging.DEBUG)
            self.logger.debug(message)





