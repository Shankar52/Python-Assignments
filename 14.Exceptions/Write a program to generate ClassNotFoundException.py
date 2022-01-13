class classnotfoundexception(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

try:
   raise classnotfoundexception('class not found!')
except classnotfoundexception as instance:
   print('ClassNotfoundException: ' + instance.parameter)
