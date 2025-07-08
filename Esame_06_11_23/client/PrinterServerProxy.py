from service.IPrinter import IPrinter
import socket

class PrinterServerProxy(IPrinter):
    def __init__(self, ip, port, buf_size):
        self.ip=ip
        self.port=port
        self.buf_size=buf_size
    
    def print(self, pathFile, tipo):
        
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, self.port))
        
        msg='-'.join(["print",pathFile, tipo])
        
        sock.send(msg.encode())
        
        sock.close()