# app/log.py
import logging
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class ColorFormatter(logging.Formatter):
    def format(self, record):
        if record.levelname == "INFO":
            record.msg = f"{Fore.GREEN}{record.msg}{Style.RESET_ALL}"
        elif record.levelname == "ERROR":
            record.msg = f"{Fore.RED}{record.msg}{Style.RESET_ALL}"
        elif record.levelname == "WARNING":
            record.msg = f"{Fore.YELLOW}{record.msg}{Style.RESET_ALL}"
        elif record.levelname == "DEBUG":
            record.msg = f"{Fore.BLUE}{record.msg}{Style.RESET_ALL}"
        return super().format(record)

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(ColorFormatter("%(asctime)s - %(levelname)s - %(message)s"))
log.addHandler(handler)