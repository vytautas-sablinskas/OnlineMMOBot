class TextHandler:
    @staticmethod
    def split_credentials(credentials):
        email = credentials[0].strip()
        password = credentials[1].strip()
        return email, password

    @staticmethod
    def split_lines_to_array(lines):
        split_lines = []
        for line in lines:
            split_line = line.split()
            split_lines.append(split_line)
        return split_lines