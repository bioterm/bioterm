import logging
import os
from logging.config import dictConfig

import yaml
from colorama import Fore
from colorama import init
from colorama import Style

# logging.basicConfig(level=logging.DEBUG)

# Initialize colorama
init(autoreset=True)


class ColoredFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": Fore.CYAN,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.MAGENTA,
    }

    def format(self, record):
        log_message = super().format(record)
        color = self.COLORS.get(record.levelname, "")
        return f"{color}{log_message}{Style.RESET_ALL}"


# Load YAML configuration
def load_logging_config():
    # Get the directory of the current file (logger_config.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Build the path to the configuration file
    config_path = os.path.join(current_dir, "logger_conf.yaml")

    with open(config_path, "r") as f:
        config = yaml.safe_load(f.read())

    config["formatters"]["colored"] = {
        "()": ColoredFormatter,
        "format": "%(asctime)s [%(name)-12s] <%(levelname)-8s> %(message)s",
    }

    dictConfig(config)


load_logging_config()


def get_module_logger(mod_name):
    """
    To use this, do logger = get_module_logger(__name__)
    """
    level_name = os.getenv("BIOTERM_LOGGING_LEVEL", "INFO").upper()
    if hasattr(logging, level_name):
        level = getattr(logging, level_name)
    else:
        print(f"Warning: Invalid logging level '{level_name}'. Defaulting to INFO.")
        level = logging.INFO
    logger = logging.getLogger(mod_name)
    logger.setLevel(level)
    return logger


if __name__ == "__main__":
    logger = get_module_logger(__name__)
    logger.debug("This is a debug log entry")
    logger.info("This is an info log entry")
    logger.warning("This is a warning log entry")
    logger.error("This is an error log entry")
    logger.critical("This is a critical log entry")
