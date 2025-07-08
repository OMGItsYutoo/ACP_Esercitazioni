from abc import ABC, abstractmethod

class IPrinter(ABC):
    @abstractmethod
    def print(self, pathFile, tipo):
        pass