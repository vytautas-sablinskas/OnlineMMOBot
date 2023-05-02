from Constants.FilePaths import FilePaths
from Handlers.TimeHandler import TimeHandler
from Handlers.FileHandler import FileHandler
from Handlers.TextHandler import TextHandler

class FileManager:
    def update_bot_current_action(status_text):
        file_path=FilePaths.CURRENT_BOT_ACTION.value
        current_datetime = TimeHandler.get_current_datetime()
        status = f"Bot status: {status_text}, Last Updated: {current_datetime}"
        FileHandler.write_into_file(file_path, status)

    def update_bot_status(status_text):
        file_path=FilePaths.BOT_STATUS.value
        FileHandler.write_into_file(file_path, status_text)

    def update_user_credentials(email, password):
        FileHandler.write_into_file(
            file_path=FilePaths.CREDENTIALS.value,
            data=f"{email}\n{password}"
        )

    def update_discord_credentials(discord_webhook_url, discord_token):
        FileHandler.write_into_file(
            file_path=FilePaths.DISCORD_CREDENTIALS.value,
            data=f"{discord_webhook_url}\n{discord_token}"
        )

    def update_chrome_arguments(chrome_arguments):
        FileHandler.write_into_file(
            file_path=FilePaths.CHROME_ARGUMENTS.value,
            data=chrome_arguments
        )

    def update_panel_bot_status(status):
        FileHandler.write_into_file(
            file_path=FilePaths.PANEL_BOT_STATUS.value, 
            data=status
        )

    def update_playtime_until_break(playtime):
        FileHandler.write_into_file(
            file_path=FilePaths.PLAYTIME_BEFORE_SLEEP.value,
            data=str(playtime)
        )

    def update_item_count(file_path, item_name, new_count):
        found_item = False
        lines = FileHandler.read_from_file_lines(file_path)
        for i in range(len(lines)):
            if item_name in lines[i]:
                lines[i] = f"{item_name}: {new_count}\n"
                found_item = True
                break

        if not found_item:
            lines.append(f"{item_name}: {new_count}\n")

        lines = [line.strip() for line in lines]
        FileHandler.write_into_file(file_path, lines)

    def get_bot_status():
        bot_status_in_array_of_lines = FileHandler.read_from_file_lines(
                FilePaths.BOT_STATUS.value
        )
        bot_status = TextHandler.get_bot_status(bot_status_in_array_of_lines)

        return bot_status
    
    def get_current_bot_action():
        current_action_message = FileHandler.read_from_file_lines(FilePaths.CURRENT_BOT_ACTION.value)
        current_action_message = ''.join(current_action_message)
        return current_action_message
    
    def get_action_tracking_logs():
        action_tracking_logs = FileHandler.read_from_file_lines(FilePaths.ACTION_TRACKING_LOGS.value)
        return action_tracking_logs

    def get_user_or_discord_credentials(user_credentials_path):
        credential_lines = FileHandler.read_from_file_lines(user_credentials_path)
        email, password = TextHandler.split_credentials(credential_lines)
        return email, password
    
    def get_session_summary():
        session_summary = FileHandler.read_from_file_lines(FilePaths.SESSION_ACTION_SUMMARY.value)
        return session_summary
    
    def get_playtime_before_sleep():
        playtime_before_sleep_minutes_list = FileHandler.read_from_file_lines(FilePaths.PLAYTIME_BEFORE_SLEEP.value)
        playtime_before_sleep_minutes = TextHandler.get_user_selected_timers(playtime_before_sleep_minutes_list)
        return playtime_before_sleep_minutes

    def log_text(file_path, message):
        FileHandler.write_into_file(file_path=file_path,
                                    data=message,
                                    append=True
        )

