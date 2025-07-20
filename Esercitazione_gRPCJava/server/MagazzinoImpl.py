from proto import magazzino_pb2, magazzino_pb2_grpc
from threading import Lock, Condition

class MagazzinoImpl(magazzino_pb2_grpc.MagazzinoServicer):
    def __init__(self, queue_size):
        self.q=[]
        self.queue_size=queue_size
        
        self.lock=Lock()
        self.prod_cv=Condition(self.lock)
        self.cons_cv=Condition(self.lock)
    
    def deposita(self, request, context):
        with self.prod_cv:
            self.prod_cv.wait_for(lambda: self.a_is_avlb(self.q))
            
            self.q.append(request.value)
            print(f"[MagazzinoImpl] - Added {request.value} to the queue")
            
            self.cons_cv.notify()
            
        return magazzino_pb2.Empty()
            
    def preleva(self, request, context):
        with self.cons_cv:
            self.cons_cv.wait_for(lambda: self.an_itm_is_avlb(self.q))
            
            value=self.q.pop()
            print(f"[MagazzinoImpl] - Got {value} from the queue")
            
            self.prod_cv.notify()
            
        return magazzino_pb2.Item(value=value)
        
    def a_is_avlb(self, queue):
        return len(queue)<self.queue_size
    
    def an_itm_is_avlb(self, queue):
        return len(queue)>0