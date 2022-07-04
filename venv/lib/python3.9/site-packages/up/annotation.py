import time


class Annotation(object):
    """
    A note that can be stored with the status output for later reference.
    """
    def __init__(self, message):
        self.message = message
        self.date = time.time()
