from threading import Thread
import socket

class ServerThread(Thread):
    def __init__(self, name, s: socket.socket, buf_size, ref):
        super().__init__(name=name)
        self.s=s
        self.buf_size=buf_size
        self.ref=ref
        
    def run(self):
        data=self.s.recv(self.buf_size).decode()
        
        msg=data.split('-')
        
        request=msg[0]
        articolo=int(msg[1])
        
        print(f"[{self.name}] - Received request: {request}, {articolo}")
        
        if request=="preleva":
            result=self.ref.preleva(articolo)
            if result==-1: result=f'No article {articolo} was found'
        elif request=="deposita":
            result=self.ref.deposita(articolo)
        else: print(f"[{self.name}] - Request non recognized")
        
        self.s.send(str(result).encode())
        
        self.s.close()
            
