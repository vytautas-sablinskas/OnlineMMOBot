from Handlers.TextHandler import TextHandler

class FileHandler:
    @staticmethod
    def read_from_file_lines(file_path):
        with open(file_path.value, 'r') as file:
            lines = file.readlines()
            return lines
        
    @staticmethod
    def get_array_from_file(file_path, delimiter):
        with open(file_path.value, 'r') as file:
            lines = file.readlines()
            array = TextHandler.split_lines_to_array(lines, delimiter)
            return array

    @staticmethod
    def write_into_file(file_path, data, append=False):
        mode = 'a' if append else 'w'
        with open(file_path.value, mode) as file:
            if not append:
                file.truncate(0)
            file.write(data)

    def get_webdriver_arguments():
        pass

    def write_updated_status_into_file(self, text, file_path=r"../Files/status.txt"):
        current_datetime = self.time_handler.get_current_datetime()
        status = f"Bot status: {text}, Last Updated: {current_datetime}"
        self.write_into_file(file_path, status)