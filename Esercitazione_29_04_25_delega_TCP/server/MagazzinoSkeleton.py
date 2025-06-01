from service.IMagazzino import IMagazzino
from server.SkeletonThread import SkeletonThread
import socket

class MagazzinoSkeleton(IMagazzino):
    def __init__(self, ip, port, bufsize, delegate:IMagazzino):
        self.ip=ip
        self.port=port
        self.bufsize=bufsize
        self.delegate=delegate
        
    def deposita(self, articolo, id):
        return self.delegate.deposita(articolo,id)
    
    def preleva(self, articolo):
        return self.delegate.preleva(articolo)
    
    def runSkeleton(self):
        
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.ip, self.port))
        s.listen()
        
        print(f"[ServerSkeleton] - Listening on {self.ip}:{self.port}")
        i=0
        while True:
            conn, _=s.accept()
            
            i=i+1
            
            th=SkeletonThread(conn, self.bufsize, f"Thread - {str(i)}", self)
            th.start()
            
        s.close()
            