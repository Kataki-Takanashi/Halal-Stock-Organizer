import threading

global_thread_lock = threading.Lock()

NAME_SEPARATOR = '/'


class colors:
    HEADER = '\033[4;37m'
    OK = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    EMPHSAS = '\033[4m'
    PARENTHETICAL = '\033[37m'
    END_EMPHSAS = '\033[24m'
    END = '\033[0m'
