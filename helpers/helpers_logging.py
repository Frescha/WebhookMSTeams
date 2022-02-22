import logging
import os

class Logging:
    def __init__(self, log_path):
        self.log_path = log_path
        self.LOGLEVEL = os.environ.get('LOGLEVEL', 'DEBUG').upper()
        self.logger = logging.getLogger('webhook-msteams')
        self.logger.setLevel(self.LOGLEVEL)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.file_handler = logging.FileHandler(self.log_path)
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)
        self.logger.info('Logging initialized')
        
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