from abc import ABC, abstractmethod

class LoggerAbs(ABC):
    """
    Abstract base class for logger implementations.
    """
    @abstractmethod
    def debug(self, message):
        pass

    @abstractmethod
    def info(self, message):
        pass

    @abstractmethod
    def warning(self, message):
        pass

    @abstractmethod
    def error(self, message):
        pass

    @abstractmethod
    def critical(self, message):
        pass
