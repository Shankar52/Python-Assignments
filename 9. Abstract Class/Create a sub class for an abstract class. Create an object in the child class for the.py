import abc
import six
@six.add_metaclass(abc.ABCMeta)
class Base(object):
    @abc.abstractmethod
    def __whatever(self):
        raise NotImplementedError

class SubClass(Base):
    def __init__(self):
        super(Base, self).__init__()
        self._Base__whatever()
    def _Base__whatever(self):
        print("whatever")


a = SubClass()
