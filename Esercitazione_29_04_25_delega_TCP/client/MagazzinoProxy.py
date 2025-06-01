from service.IMagazzino import IMagazzino
import socket

class MagazzinoProxy(IMagazzino):
    def __init__(self, ip, port, buf_size):
        self.ip=ip
        self.port=port
        self.buf_size=buf_size
        
    def deposita(self, articolo, id):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        
        message='-'.join(["deposita",articolo,str(id)])
        print(f"[Proxy] - Message to be sent: {message}")
        
        s.send(message.encode())
        resp=s.recv(self.buf_size).decode()
        
        print(f"[Proxy] - Response received: {resp}")
        
        return bool(resp) #il servizio ritorna "False" oppure "True" (la conversione bool --> str avviene per la comunicazione)
    
    def preleva(self, articolo):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        
        message='-'.join(["preleva",articolo])
        print(f"[Proxy] - Message to be sent: {message}")
        
        s.send(message.encode())
        resp=s.recv(self.buf_size).decode()
        
        print(f"[Proxy] - Response received: {resp}")
        
        return resp #il servizio ritorna l'id dell'articolo   