from abc import ABC, abstractmethod

class IMagazzino(ABC):
    
    @abstractmethod
    def deposita(self, articolo):
        pass

    @abstractmethod
    def preleva(self, articolo):
        pass
