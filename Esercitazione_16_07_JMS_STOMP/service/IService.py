from abc import ABC, abstractmethod

class IService(ABC):
    @abstractmethod
    def deposita(self, art_id):
        pass
    
    @abstractmethod
    def preleva(self):
        pass