from server.IMagazzino import IMagazzino
import socket

class MagazzinoProxy(IMagazzino):
    
    def __init__(self, ip, port):
        self.ip=ip
        self.port=port
        self.buf_size=1024
    
    def deposita(self, articolo, id):
        
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((self.ip,self.port))
        
        message='-'.join(["deposita",articolo,str(id)])
        print("[MAGAZZINO PROXY] Sending request:", message)
        
        sock.send(message.encode("utf-8"))
        response=sock.recv(self.buf_size)
        
        print("[MAGAZZINO PROXY] Response:",response.decode("utf-8"))
        
        # response=True --> Deposito avvenuto con successo
        # response=False --> Deposito non avvenuto
        return bool(response)
    
    def preleva(self, articolo):
        
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((self.ip,self.port))
        
        message="-".join(["preleva",articolo])
        print("[MAGAZZINO PROXY] Sending request:", message)
        
        sock.send(message.encode("utf-8"))
        response=sock.recv(self.buf_size)
        
        response_msg=response.decode()
        
        print("[MAGAZZINO PROXY] Response:",response_msg)
        
        return int(response_msg)