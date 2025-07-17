from multiprocessing import Process
import socket

class SkeletonProcess(Process):
    def __init__(self, name, conn:socket.socket, buf_size, ref):
        super().__init__(name=name)
        self.conn=conn
        self.buf_size=buf_size
        self.ref=ref
        
    def run(self):
        print(f"[{self.name}] - Running")
        
        msg=self.conn.recv(self.buf_size).decode()
        msg_split=str(msg).split('-')
        
        request=msg_split[0]

        # NOTE: the operator "in" is used, since Java adds extra characters when sending String over socket, which prevents the exact match
        if "deposita" in request:
            id=msg_split[1]
            response=self.ref.deposita(id)
        elif "preleva" in request:
            response=str(self.ref.preleva())        
        else:
            print(f"[{self.name}] - Couldn't recognized the request")
            
        # Send the response
        # NOTE: It is required to add "\n" at the end of the String in order to allow Java application to receive the data
        string_to_send = (str(response)+"\n")
        self.conn.send(string_to_send.encode())
        
        self.conn.close()

        