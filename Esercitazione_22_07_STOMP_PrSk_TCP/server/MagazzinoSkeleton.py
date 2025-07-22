from service.IMagazzino import IMagazzino
from server.SkeletonProcess import SkeletonProcess
import socket

class MagazzinoSkeleton(IMagazzino):

    def __init__(self, ip, port, buf_size):
        self.ip=ip
        self.port=port
        self.buf_size=buf_size
    
    def runSkeleton(self):
        
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.ip, self.port))
        sock.listen(5)
        
        print(f"[MagazzinoSkeleton] - ServerSkeleton listening on port: {sock.getsockname()[1]}")
        
        while True:
            
            conn, addr=sock.accept()
            
            th=SkeletonProcess(f"SkeletonProcess", conn, self.buf_size, self)
            th.start()
            
        sock.close()