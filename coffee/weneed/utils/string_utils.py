import string


class StringUtils:

    @staticmethod
    def print_graphic(text, width=49):
        border = '=' * width
        empty_space = ' ' * ((width - len(text) - 4) // 2)
        print(border)
        print('==', empty_space, text, empty_space, '==' if len(empty_space) * 2 + len(text) + 4 == width else '===')
        print(border)

    @staticmethod
    def get_ascii_chars():
        """
        Returns a set of ASCII characters.
        """
        return set(string.ascii_letters + string.digits + string.punctuation + string.whitespace)
