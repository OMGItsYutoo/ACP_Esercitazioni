from server.MagazzinoSkeleton import MagazzinoSkeleton
from multiprocessing import Queue

class MagazzinoImpl(MagazzinoSkeleton):
    
    def __init__(self, ip, port, buf_size, queue_size):
        super().__init__(ip, port, buf_size)
        self.q=Queue(queue_size)
        
    def deposita(self, id_art):
        self.q.put(id_art)
        print(f"[MagazzinoImpl] - Added {id_art} to the queue")
        
        return "deposited"
        
    def preleva(self):
        item=self.q.get()
        print(f"[MagazzinoImpl] - Got {item} from the queue")
        
        return item