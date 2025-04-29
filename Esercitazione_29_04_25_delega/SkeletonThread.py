from threading import Thread, current_thread

class SkeletonThread(Thread):
    
    def __init__(self,sock,msg,addr,thr_name,ref):
        super().__init__(name=thr_name)
        self.msg=msg
        self.sock=sock
        self.addr=addr
        self.ref=ref
    
    def run(self):
        msg_split=self.msg.decode().split("-")
        
        service=msg_split[0]
        article=msg_split[1]
        
        result=None
        
        if service=="preleva":
            result=self.ref.preleva(article)
        elif service=="deposita":
            id=msg_split[2]
            result=self.ref.deposita(article,id)
        else: print(f"[{current_thread().name}] Servizio {service} non riconosciuto")
        
        res=str(result)
        self.sock.sendto(res.encode(),self.addr)
        print(f"[{current_thread().name}] Result sent")
        