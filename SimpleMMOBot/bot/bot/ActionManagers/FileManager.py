from Constants.FilePaths import FilePaths
from Handlers.TimeHandler import TimeHandler
from Handlers.FileHandler import FileHandler

class FileManager:
    def update_bot_current_action(status_text, file_path=FilePaths.CURRENT_BOT_ACTION.value):
        current_datetime = TimeHandler.get_current_datetime()
        status = f"Bot status: {status_text}, Last Updated: {current_datetime}"
        FileHandler.write_into_file(file_path, status)

    def update_bot_status(status_text, file_path=FilePaths.BOT_STATUS.value):
        FileHandler.write_into_file(file_path, status_text)