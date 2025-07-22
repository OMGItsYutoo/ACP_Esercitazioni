from multiprocessing import Process
import socket

class SkeletonProcess(Process):
    def __init__(self, name, conn:socket.socket, buf_size, ref):
        super().__init__(name=name)
        self.conn=conn
        self.buf_size=buf_size
        self.ref=ref
        
    def run(self):
        msg=self.conn.recv(self.buf_size).decode()
        
        msg_split=msg.split('-')
        
        request=msg_split[0]
        
        if request=="deposita":
            id=msg_split[1]
            
            print(f"[{self.name}] - Received deposita request, id_art: {id}")
            result=self.ref.deposita(id)
        elif request=="preleva":
            
            print(f"[{self.name}] - Received preleva request")
            result=self.ref.preleva()
            
        else:
            print(f"[{self.name}] - Coudn't recognize the request")
 
        self.conn.send(str(result).encode())
        
        self.conn.close()