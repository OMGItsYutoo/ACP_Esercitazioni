from proto import service_pb2, service_pb2_grpc
from threading import Lock, Condition
from pymongo import MongoClient

def get_database():
    client=MongoClient('localhost',27017)
    return client["storage_data"] #the database name is storage_data


class ServerImpl(service_pb2_grpc.ServiceServicer):
    def __init__(self, queue_size):
        self.queue_size=queue_size
        
        self.items=0
        self.lock=Lock()
        self.prod_cv=Condition(self.lock)
        self.cons_cv=Condition(self.lock)
        
    def deposita(self, request, context):
        
        with self.prod_cv:
            self.prod_cv.wait_for(lambda:self.a_space_is_avlbl())
            
            
            db=get_database()
            collection=db["data"]
            
            try:
                item={'id_art':request.id, 'product': request.product}
                collection.insert_one(item)
                print(f"[ServerImpl] - Added {item}")
                
                self.items=self.items+1
                self.cons_cv.notify()
            except Exception as e:
                print("[ServerImpl] - Error while inserting into the db")
                return "scemo chi legge anche qui"
                
        return service_pb2.ResponseString(response="deposited")
                
    def preleva(self, request, context):
        item={"id":"scemo", "product":"chi legge"}
        
        with self.cons_cv:
            self.cons_cv.wait_for(lambda: self.an_item_is_avlbl())
            
            db=get_database()
            collection=db["data"]
            
            try:
                item=collection.find_one_and_delete()
                self.items=self.items-1
                self.cons_cv.notify()
                return service_pb2.Item(id=item["id_art"],product=item["product"])
                
            except Exception as e:
                print("[ServerImpl] - Error while popping from the db")
        print(f"[ServerImpl] - got {item}")
                
    
    def svuota(self, request, context):
        with self.cons_cv:
            
            db=get_database()
            collection=db["data"]
            
            while self.an_item_is_avlbl():
                try:
                    item=collection.find_one_and_delete({})
                    self.items=self.items-1
                    
                    yield service_pb2.Item(id=item["id_art"],product=item["product"])
                    
                except Exception as e:
                    print(f"[ServerImpl] - Error while popping from the db: {e}")
            
            self.cons_cv.notify()    
            
    def a_space_is_avlbl(self):
        return self.items<self.queue_size
    
    def an_item_is_avlbl(self):
        return self.items>0
        