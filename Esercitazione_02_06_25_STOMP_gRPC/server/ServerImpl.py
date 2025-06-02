from proto import service_pb2_grpc, service_pb2
from threading import Lock, Condition

#Service Implementation
class ServerImpl(service_pb2_grpc.ServiceServicer):
    def __init__(self,queue_size):
        self.queue=[]
        self.lock=Lock()
        self.prod_cv=Condition(self.lock)
        self.cons_cv=Condition(self.lock)
        self.queue_size=queue_size
        
    def deposita(self, request, context):
        
        with self.prod_cv:
            self.prod_cv.wait_for(lambda:self.a_space_is_available(self.queue))
            
            self.queue.append({'id':request.id,'product':request.product})
            print(f"[ServerImpl] - Added [{str(request.id)}, {request.product}]")
            
            self.cons_cv.notify()
        
        return service_pb2.ResponseString(response='deposited')
    
    def preleva(self, request, context):
        
        with self.cons_cv:
            self.cons_cv.wait_for(lambda:self.an_item_is_available(self.queue))
            
            res=self.queue.pop(0)
            print(f"[ServerImpl] - Got [{str(res['id'])}, {res['product']}]")
            
            self.prod_cv.notify()
            
        return service_pb2.Item(id=res['id'], product=res['product'])
    
    def svuota(self, request, context):
        print(f"[ServerImpl] - Svuota")
        
        with self.cons_cv:
            while self.an_item_is_available(self.queue):
                res=self.queue.pop(0)
                print(f"[ServerImpl] - Got [{str(res['id'])}, {res['product']}]")
                
                yield service_pb2.Item(id=res['id'], product=res['product'])
            else: 
                print("[ServerImpl] - Queue is empty")
                
            self.prod_cv.notify()

    def a_space_is_available(self, queue):
        return len(queue)<self.queue_size
    
    def an_item_is_available(self, queue):
        return len(queue)>0