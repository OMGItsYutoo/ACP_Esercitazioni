from abc import ABC, abstractmethod
from .IMagazzino import IMagazzino
from .SkeletonThread import SkeletonThread

import socket
        
class MagazzinoSkeleton(IMagazzino, ABC):
    
    def __init__(self, ip, port):
        self.ip=ip
        self.port=port
        self.buf_size=1024
    
    @abstractmethod    
    def deposita(self, articolo, id):
        pass
    
    @abstractmethod
    def preleva(self, articolo):
        pass
    
    def runSkeleton(self):
        
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.bind((self.ip,self.port))
        sock.listen(30)
        
        print("[MAGAZZINO SKELETON] Ready on port:", sock.getsockname()[1])
        
        i=0
        
        while True:
            conn, addr=sock.accept()
            
            i=i+1
            
            thread=SkeletonThread(conn,self.buf_size,"SKELETON THREAD-"+str(i),self)
            thread.start()
            
        sock.close()

