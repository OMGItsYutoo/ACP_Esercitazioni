from multiprocessing import Process
from proto import service_pb2

import stomp

class DispatcherProcess(Process):
    def __init__(self, name, stub, msg:str):
        super().__init__(name=name)
        self.stub=stub
        self.msg=msg
        
    def run(self):
        
        conn=stomp.Connection([('localhost',61613)])
        conn.connect(wait=True)
        
        msg=self.msg.split("-")
        
        request=msg[0]
        
        if request=="deposita":
            id_article=msg[1]  
            product=msg[2]
            
            result=self.stub.deposita(service_pb2.Item(id=int(id_article), product=product))
            conn.send("/queue/responses", result.response)
        elif request=="preleva":
            result=self.stub.preleva(service_pb2.Empty())
            conn.send("/queue/responses", str(result.id)+'-'+result.product)
        elif request=="svuota":
            result=self.stub.svuota(service_pb2.Empty())
            for res in result:
                conn.send('/queue/responses', str(res.id)+"-"+res.product)
                
        conn.disconnect()
        
        