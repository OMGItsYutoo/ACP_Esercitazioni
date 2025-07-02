from service.IMagazzino import IMagazzino
from server.ServerThread import ServerThread
import socket

class MagazzinoSkeleton(IMagazzino):
    def __init__(self, ip, port, buf_size):
        self.ip=ip
        self.port=port
        self.buf_size=buf_size
    
    def deposita(self, articolo):
        pass
    
    def preleva(self, articolo):
        pass
    
    def runSkeleton(self):
        
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.ip, self.port))
        sock.listen(30)
        
        print(f"[MagazzinoSkeleton] - Skeleton is listening on port: {sock.getsockname()[1]}")
        
        while True:
            conn, addr=sock.accept()
            
            print("[MagazzinoSkeleton] - Connection Accepted, starting SkeletonProcess")
            
            #multithread server
            p=ServerThread("SkeletonThread",conn, self.buf_size, self)
            p.start()
            
        sock.close()