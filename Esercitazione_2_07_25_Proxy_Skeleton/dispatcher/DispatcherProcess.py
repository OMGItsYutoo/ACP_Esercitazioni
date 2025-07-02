from multiprocess import Process
import stomp

class DispatcherProcess(Process):
    def __init__(self, name, proxy, msg:str):
        super().__init__(name=name)
        self.proxy=proxy
        self.msg=msg        
        
    def run(self):
        
        print(f"[{self.name}] - Running")
        
        #connection for every process should be more robust
        conn=stomp.Connection([("localhost",61613)])
        conn.connect(wait=True)
        
        msg=self.msg.split('-')
        request=msg[0]
        articolo=int(msg[1])
        
        if request=="deposita":
            result=self.proxy.deposita(articolo)
        elif request=="preleva":
            result=self.proxy.preleva(articolo)
        else:
            print(f"[{self.name}] - Request non recognized")
        
        conn.send("/queue/responses", result)
        conn.disconnect()
        