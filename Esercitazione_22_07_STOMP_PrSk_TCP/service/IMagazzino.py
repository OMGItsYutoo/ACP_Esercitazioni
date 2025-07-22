from abc import ABC, abstractmethod

class IMagazzino(ABC):
    
    @abstractmethod
    def deposita(self, id_art):
        pass
    
    @abstractmethod
    def preleva(self):
        pass