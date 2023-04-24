import TimeHandler
import TextHandler

class FileHandler:
    @staticmethod
    def read_from_file(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines

    @staticmethod
    def write_into_file(file_path, data, append=False):
        mode = 'a' if append else 'w'
        with open(file_path, mode) as file:
            if not append:
                file.truncate(0)
            file.write(data)

    def get_webdriver_arguments():
        pass

    def get_credentials(self, file_path=r"../Files/credentials.txt"):
        credential_lines = self.read_from_file(file_path)
        email, password = TextHandler.split_credentials(credential_lines)

        return email, password

    def write_updated_status_into_file(self, text, file_path=r"../Files/status.txt"):
        current_datetime = self.time_handler.get_current_datetime()
        status = f"Bot status: {text}, Last Updated: {current_datetime}"
        self.write_into_file(file_path, status)