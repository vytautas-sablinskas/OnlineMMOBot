class TextHandler:
    @staticmethod
    def split_lines_to_array(lines, delimiter=' '):
        split_lines = []
        for line in lines:
            split_line = line.split(delimiter)
            split_lines.append(split_line)
        return split_lines

    @staticmethod
    def split_credentials(credentials):
        email = credentials[0].strip()
        password = credentials[1].strip()
        return email, password