class Error (Exception):
    """
    Base class for other exceptions
    """
    def __init__(self, message):
        self.message = message
