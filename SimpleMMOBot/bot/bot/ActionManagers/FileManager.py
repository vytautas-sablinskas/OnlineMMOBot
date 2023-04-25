from Constants.FilePaths import FilePaths
from Handlers.TimeHandler import TimeHandler
from Handlers.FileHandler import FileHandler

class FileManager:
    def update_status(status_text, file_path=FilePaths.BOT_STATUS):
        current_datetime = TimeHandler.get_current_datetime()
        status = f"Bot status: {status_text}, Last Updated: {current_datetime}"
        FileHandler.write_into_file(file_path.value, status)