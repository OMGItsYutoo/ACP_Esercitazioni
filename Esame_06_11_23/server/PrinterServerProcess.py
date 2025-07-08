from multiprocessing import Process
import socket
import stomp

class PrinterServerProcess(Process):
    def __init__(self, name, conn:socket.socket, buf_size, ref):
        super().__init__(name=name)
        self.conn=conn
        self.buf_size=buf_size
        self.ref=ref
        
    def run(self):
        
        msg=self.conn.recv(self.buf_size).decode()
        msg_split=msg.split('-')
        
        if msg_split[0]=="print":
            print(f"[{self.name}] - Invocating {msg}")

            self.ref.print(msg_split[1], msg_split[2])
        else: 
            print("Error")