from multiprocessing import Process
from dispatcher.MagazzinoProxy import MagazzinoProxy

import stomp

class DispatcherProcess(Process):
    def __init__(self, name, ip, port, buf_size, msg):
        super().__init__(name=name)
        self.ip=ip
        self.port=port
        self.buf_size=buf_size
        self.msg:str=msg
        
    def run(self):
        stub=MagazzinoProxy(self.ip, self.port, self.buf_size)
        
        conn=stomp.Connection([("localhost",61613)])
        conn.connect(wait=True)
        
        msg_split=self.msg.split('-')
        
        request=msg_split[0]
        
        if request=="deposita":
            res=stub.deposita(msg_split[1])
        elif request=="preleva":
            res=stub.preleva()
        else: 
            print(f"[{self.name}] - Couldn't recognize the request")
            
        print(f"[{self.name}] - Sending response: {str(res)}")
        
        conn.send("/queue/response", str(res)) 
        conn.disconnect()