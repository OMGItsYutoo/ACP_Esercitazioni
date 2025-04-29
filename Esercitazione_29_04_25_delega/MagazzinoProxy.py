from IMagazzino import IMagazzino
import socket

class MagazzinoProxy(IMagazzino):
    
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port
        self.buf_size=1024
        
        self.s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        
    def deposita(self, articolo, id):
                
        msg='-'.join(["deposita",articolo,str(id)])
        print("[MAGAZZINOPROXY] Sending req:", msg)
        
        self.s.sendto(msg.encode(),(self.ip,self.port))
        
        data, addr=self.s.recvfrom(self.buf_size)
        
        res=data.decode()
                
        return bool(res)
    
    def preleva(self, articolo):
                
        msg='-'.join(["preleva",articolo])
        print("[MAGAZZINOPROXY] Sending req:", msg)
        
        self.s.sendto(msg.encode(),(self.ip,self.port))
        
        data, addr=self.s.recvfrom(self.buf_size)
            
        res=data.decode()
                
        return int(res)
        