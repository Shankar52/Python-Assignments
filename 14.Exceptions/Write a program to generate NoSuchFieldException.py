class NoSuchFieldException(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

try:
   raise NoSuchFieldException('field not found!')
except NoSuchFieldException as instance:
   print('NoSuchFieldException: ' + instance.parameter)
