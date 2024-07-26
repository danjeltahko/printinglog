import datetime
import inspect

COLORS = {
    "black": "\033[0;30m",
    "red": "\033[0;31m",
    "green": "\033[0;32m",
    "yellow": "\033[0;33m",
    "blue": "\033[0;34m",
    "magneta": "\033[0;35m",
    "cyan": "\033[0;36m",
    "white": "\033[0;37m",
    "nc": "\033[0m",
}

default_colors = {
    "info": "green",
    "error": "red",
    "warning": "yellow",
    "debug": "blue",
}


class Logger:
    """
    A simple Logger class to print formatted and colored log messages.

    Logging options available: INFO, ERROR, WARNING, DEBUG.

    The logging format and colors can be customized.

    Available formats:
        - simple: Prints log with only the type of log (e.g., INFO, ERROR) along with the message.
        - logging: Prints log with datetime, type of log along with the message.
        - detailed: Prints log with datetime, filename, type of log along with the message.
        - long: Prints log with datetime, filename, function, type of log along with the message.

    Args:
        format (str): One of "simple", "logging", "detailed", or "long". Default is "simple".
        colorscheme (dict[str, str]): A dictionary mapping log types (info, error, warning, debug) to colors.
            Default is the `default_colors` dictionary.

            default_colors = {
                "info": "green",
                "error": "red",
                "warning": "yellow",
                "debug": "blue",
            }
    """

    def __init__(
        self,
        format: str = "simple",
        colorscheme: dict[str, str] = default_colors,
    ) -> None:
        self.format = format
        self.colorscheme = colorscheme

    def info(self, msg: str):
        """
        Prints out the message with colored 'INFO:' prefix.

        Args:
            msg (str): The message to log.
        """
        log = self.__set_output("info")
        if isinstance(msg, str):
            print(log, msg)

    def error(self, msg: str):
        """
        Prints out the message with colored 'ERROR:' prefix.

        Args:
            msg (str): The message to log.
        """
        log = self.__set_output("error")
        if isinstance(msg, str):
            print(log, msg)

    def debug(self, msg: str):
        """
        Prints out the message with colored 'DEBUG:' prefix.

        Args:
            msg (str): The message to log.
        """
        log = self.__set_output("debug")
        if isinstance(msg, str):
            print(log, msg)

    def warning(self, msg: str):
        """
        Prints out the message with colored 'WARNING:' prefix.

        Args:
            msg (str): The message to log.
        """
        log = self.__set_output("warning")
        if isinstance(msg, str):
            print(log, msg)

    def __set_output(self, typeof: str):
        """
        Sets the logging output according to the configuration options.

        Args:
            typeof (str): The type of log (info, error, warning, debug).

        Returns:
            str: The formatted log string.
        """
        if self.format == "simple":
            text = self.__get_color(typeof)
            return f"{text}"

        elif self.format == "logging":
            # get the time
            time = self.__get_date()
            # set color to log
            text = self.__get_color(typeof)
            return f"{time} - {text}"

        elif self.format == "detailed":
            # get the time
            time = self.__get_date()
            # set color to log
            text = self.__get_color(typeof)
            # get the stack
            stack = inspect.stack()[2]
            # set the file name
            file = inspect.getmodulename(stack.filename)
            return f"{time} @{file} - {text}"

        elif self.format == "long":
            # get the time
            time = self.__get_date()
            # set color to log
            text = self.__get_color(typeof)
            # get the stack
            stack = inspect.stack()[2]
            # set the function name
            function = stack.function if stack.function != "<module>" else ""
            # set the file name
            file = inspect.getmodulename(stack.filename)
            return f"{time} @{file}<{function}> - {text}"

    def __get_color(self, typeof: str):
        """
        Gets the color code for the log type.

        Args:
            typeof (str): The type of log (info, error, warning, debug).

        Returns:
            str: The colored log type string.
        """
        _color_setting = self.colorscheme[typeof]
        _color = COLORS[_color_setting]
        _nc = COLORS["nc"]
        _capital_type = typeof.upper()
        return f"{_color}{_capital_type}:{_nc}"

    def __get_date(self):
        """
        Gets the current date and time.

        Returns:
            str: The formatted current date and time.
        """
        now = datetime.datetime.today()
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_now
