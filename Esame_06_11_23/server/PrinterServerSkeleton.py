from service.IPrinter import IPrinter
from server.PrinterServerProcess import PrinterServerProcess
import socket

class PrinterServerSkeleton(IPrinter):
    def __init__(self, ip, port, buf_size):
        self.ip=ip
        self.port=port
        self.buf_size=buf_size
    
    def print(self, pathFile, tipo):
        pass
    
    def runSkeleton(self):
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.ip, self.port))
        sock.listen(10)
        
        print(f"[PrinterServerSkeleton] - Listening on port: {sock.getsockname()[1]}")
        
        while True:
            conn, addr=sock.accept()
            
            p=PrinterServerProcess("PrinterServerProcess", conn, self.buf_size, self)
            p.start()
            
        sock.close()
            
            
            
        