from service.IMagazzino import IMagazzino
from .SkeletonThread import SkeletonThread
import socket

class MagazzinoSkeleton(IMagazzino):
    
    def __init__(self,ip,port,delegate):
        self.ip=ip
        self.port=port
        self.delegate=delegate
        self.buf_size=1024
        
    def deposita(self, articolo, id):
        return self.delegate.deposita(articolo,id)
    
    def preleva(self, articolo):
        return self.delegate.preleva(articolo)
    
    def runSkeleton(self):
        
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.bind((self.ip,self.port))
        
        print("[MAGAZZINO SKELETON] Ready on port:", s.getsockname()[1])
        
        i=0
        
        while True:
            
            msg,addr=s.recvfrom(self.buf_size)
            
            i=i+1
            
            t=SkeletonThread(s,msg,addr,"SKELETON THREAD-"+str(i),self)
            t.start()
            
        s.close()

        
        

        