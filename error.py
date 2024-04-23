class LengthExceededError(Exception):
    def __init__(self, message):
        super().__init__(message)  # Call the constructor of the base class Exception
        self.message = message

class InvalidSubTypeError(Exception):
    def __init__(self, message):
        super().__init__(message)  # Call the constructor of the base class Exception
        self.message = message
