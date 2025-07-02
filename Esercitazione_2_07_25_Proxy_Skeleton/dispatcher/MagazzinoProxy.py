from service.IMagazzino import IMagazzino
import socket

class MagazzinoProxy(IMagazzino):
    def __init__(self, ip, port, buf_size):
        self.ip=ip
        self.port=port
        self.buf_size=buf_size
        
    def deposita(self, articolo):
        
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, self.port))
        
        msg='-'.join(["deposita", str(articolo)])
        
        print(f"[MagazzinoProxy] - Sending request ({msg})")
        sock.send(msg.encode())
        
        result=sock.recv(self.buf_size).decode()
        
        sock.close()
        
        return result
    
    def preleva(self, articolo):
        
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, self.port))
        
        msg='-'.join(["preleva", str(articolo)])
        
        print(f"[MagazzinoProxy] - Sending request ({msg})")
        sock.send(msg.encode())
        
        result=sock.recv(self.buf_size).decode()
        
        sock.close()
        
        return result
        