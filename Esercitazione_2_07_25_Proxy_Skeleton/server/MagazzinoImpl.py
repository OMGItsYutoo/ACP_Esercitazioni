from server.MagazzinoSkeleton import MagazzinoSkeleton
from threading import Lock, Condition

#proxy-skeleton per ereditarietà 
class MagazzinoImpl(MagazzinoSkeleton):
    def __init__(self, ip, port, buf_size, queue_size):
        self.ip=ip
        self.port=port
        self.buf_size=buf_size
        self.queue_size=queue_size
        
        #implementazione con lista
        self.q=[]
        self.lock=Lock()
        self.prod_cv=Condition(self.lock)
        self.cons_cv=Condition(self.lock)
        
    def deposita(self, articolo):
        
        with self.prod_cv:
            self.prod_cv.wait_for(lambda:self.a_space_is_avlbl(self.q))
            
            self.q.append(articolo)
            print(f"[MagazzinoImpl] - Added {articolo} to the queue")
            
            self.cons_cv.notify()
        
        return "deposited"
            
    def preleva(self, articolo):
        item=-1
        
        with self.cons_cv:
            self.cons_cv.wait_for(lambda: self.an_item_is_avlbl(self.q))
            
            try:   
                i=self.q.index(articolo)
                item=self.q.pop(i)
                
                print(f"[MagazzinoImpl] - Got {item} from the queue")
                
                self.prod_cv.notify()
            except ValueError as ve:
                print(f"[ServerImpl] - There's no articolo {articolo} in the queue")
            
        return item
                
    def a_space_is_avlbl(self, queue):
        return len(queue)<self.queue_size
    
    def an_item_is_avlbl(self, queue):
        return len(queue)>0