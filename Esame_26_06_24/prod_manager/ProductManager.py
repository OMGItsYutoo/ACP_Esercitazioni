from proto import service_pb2, service_pb2_grpc
from threading import Lock, Condition
import requests

class ProductManager(service_pb2_grpc.ServiceServicer):
    def __init__(self, queue_size, base_url):
        self.laptop_queue=[]
        self.queue_size=queue_size
        
        self.lock=Lock()
        self.prod_cv=Condition(self.lock)
        self.cons_cv=Condition(self.lock)
        
        self.base_url=base_url
    
    def buy(self, request, context):
        with self.cons_cv:
            self.cons_cv.wait_for(lambda: self.an_item_is_avlbl(self.laptop_queue))
            
            serial_number=self.laptop_queue.pop()
            print(f"[ProductManager] - Got {serial_number} from the queue")

            self.prod_cv.notify()
            
        data={
            "operation":"buy",
            "serial_number":serial_number
        }
        
        req=requests.post(self.base_url+"/update_history", json=data)
        
        try:
            req.raise_for_status()
        except requests.HTTPError:
            print("[ProductManager] - An error occurred while posting record to server")
            return service_pb2.Item(serial_number=-1)
                    
        return service_pb2.Item(serial_number=serial_number)
    
    def sell(self, request, context):
        with self.prod_cv:
            self.prod_cv.wait_for(lambda: self.a_space_is_avlbl(self.laptop_queue))
            
            self.laptop_queue.append(request.serial_number)
            print(f"[ProductManager] - Added {request.serial_number} from the queue")

            self.cons_cv.notify()
            
        data={
            "operation":"sell",
            "serial_number":request.serial_number
        }
        
        req=requests.post(self.base_url+"/update_history", json=data)
        
        try:
            req.raise_for_status()
        except requests.HTTPError:
            print("[ProductManager] - An error occurred while posting record to server")
            ack=False
            
        ack=True
        
        return service_pb2.Ack(ack=ack)
        
    def a_space_is_avlbl(self, queue):
        return len(queue)<self.queue_size
    
    def an_item_is_avlbl(self, queue):
        return len(queue)>0