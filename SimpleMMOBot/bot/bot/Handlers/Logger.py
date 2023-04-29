import logging
from Constants.FilePaths import FilePaths

class Logger:
    def __init__(self, file_name=FilePaths.LOGS.value):
        logging.basicConfig(filename=file_name, level=logging.DEBUG,
                            format='%(message)s')
        self.logger = logging.getLogger()

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_debug(self, message):
        self.logger.debug(message)