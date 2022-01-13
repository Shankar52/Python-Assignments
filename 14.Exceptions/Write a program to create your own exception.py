class DemoException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
message = "Exception Triggered! Something went wrong."
raise DemoException(message)
