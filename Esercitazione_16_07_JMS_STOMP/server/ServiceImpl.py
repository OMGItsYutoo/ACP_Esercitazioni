from server.ServiceSkeleton import ServiceSkeleton
from multiprocessing import Queue

class ServiceImpl(ServiceSkeleton):
    def __init__(self, ip, port, buf_size, queue_size):
        super().__init__(ip, port, buf_size)
        self.queue_size=queue_size
        
        self.q=Queue(self.queue_size)
        
    def deposita(self, art_id):
        self.q.put(art_id)
        
        print(f"[ServiceImpl] - Deposited {art_id} in the queue")
        
        return "deposited"
    
    def preleva(self):
        id=self.q.get()
        
        print(f"[ServiceImpl] - Got {id} from the queue")
        
        return id
        