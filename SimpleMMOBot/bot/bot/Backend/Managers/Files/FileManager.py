from Constants.FilePaths import FilePaths
from Handlers.TimeHandler import TimeHandler
from Handlers.FileHandler import FileHandler
from Handlers.TextHandler import TextHandler

class FileManager:
    def update_bot_current_action(status_text, file_path=FilePaths.CURRENT_BOT_ACTION.value):
        current_datetime = TimeHandler.get_current_datetime()
        status = f"Bot status: {status_text}, Last Updated: {current_datetime}"
        FileHandler.write_into_file(file_path, status)

    def update_bot_status(status_text, file_path=FilePaths.BOT_STATUS.value):
        FileHandler.write_into_file(file_path, status_text)

    def log_text(file_path, message):
        FileHandler.write_into_file(file_path=file_path,
                                    data=message,
                                    append=True
        )

    def get_user_or_discord_credentials(user_credentials_path):
        credential_lines = FileHandler.read_from_file_lines(user_credentials_path)
        email, password = TextHandler.split_credentials(credential_lines)
        return email, password