from Handlers.TimeHandler import TimeHandler
import pandas as pd

class TextHandler:
    @staticmethod
    def split_lines_to_array(lines, delimiter):
        array = []
        for line in lines:
            line = line.strip()
            if line:
                split_line = line.split(delimiter)
                array.extend(split_line)
        return array

    @staticmethod
    def split_credentials(credentials):
        if len(credentials) < 2:
            return "", ""
        
        email_or_discord_webhook_url = credentials[0].strip()
        password_or_discord_token = credentials[1].strip()
        return email_or_discord_webhook_url, password_or_discord_token
    
    def get_user_selected_timers(time_in_list):
        playtime_in_minutes = int(time_in_list[0])
        return playtime_in_minutes

    def split_actions_summary(lines):
        actions = []
        values = []

        for line in lines:
            if line:
                action, value = line.split(": ")
                actions.append(action)
                values.append(int(value))

        df = pd.DataFrame({"Action": actions, "Count": values})
        return df

    @staticmethod
    def get_bot_status(lines):
        if len(lines) > 0 and lines[0].lower() == "continue":
            return "Continue"
        
        return "Pause"
    
    @staticmethod
    def get_current_action_in_text(next_action):
        max_width = len("Gather Materials")
        current_datetime = TimeHandler.get_current_datetime()
        return f"Action: {next_action.ljust(max_width)} | Time: {current_datetime}"

