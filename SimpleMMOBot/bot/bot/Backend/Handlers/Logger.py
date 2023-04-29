from Handlers.FileHandler import FileHandler
from Constants.FilePaths import FilePaths

class Logger:
    def __init__(self, file_path=FilePaths.LOGS.value):
        self.file_path = file_path

    def log_text(self, message):
        FileHandler.write_into_file(file_path=self.file_path, data=message, append=True)
        self.logger.info(message)