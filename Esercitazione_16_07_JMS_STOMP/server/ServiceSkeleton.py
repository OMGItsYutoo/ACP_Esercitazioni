from service.IService import IService
from server.SkeletonProcess import SkeletonProcess
import socket

class ServiceSkeleton(IService):
    
    def __init__(self, ip, port, buf_size):
        self.ip=ip
        self.port=port
        self.buf_size=buf_size
    
    def deposita(self, art_id):
        pass

    def preleva(self):
        pass
    
    def runSkeleton(self):
        
        print("[Server] - Server is listening on port 12312")
        
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.ip, self.port))
        sock.listen(10)
        
        i=0
        while True:
            
            conn, addr=sock.accept()
            
            p=SkeletonProcess(f"SkeletonProcess-{i}", conn, self.buf_size, self)
            p.start()
            
            i+=1
        
        sock.close()