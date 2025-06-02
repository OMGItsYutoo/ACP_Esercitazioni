from service.IMagazzino import IMagazzino
from threading import Lock, Condition

class MagazzinoImpl(IMagazzino):
    def __init__(self, queue_size, db):
        self.laptop_queue=[]
        self.smartphone_queue=[]
        
        self.queue_size=queue_size
        
        cv_laptop_lock=Lock()
        cv_smartphone_lock=Lock()
        
        self.laptop_consumer_cv=Condition(cv_laptop_lock)
        self.laptop_producer_cv=Condition(cv_laptop_lock)
        
        self.smartphone_consumer_cv=Condition(cv_smartphone_lock)
        self.smartphone_producer_cv=Condition(cv_smartphone_lock)
        
        self.db=db
        
    def deposita(self, articolo, id):
        
        success=True
        
        if articolo=="laptop":
            with self.laptop_producer_cv:
                self.laptop_producer_cv.wait_for(lambda:self.a_space_is_available(self.laptop_queue))
                
                self.laptop_queue.append(id)
                print(f"[ServerImpl] - Added {id} to {articolo}")
                print(len(self.laptop_queue))
                
                self.laptop_consumer_cv.notify()    
        elif articolo=="smartphone":
            with self.smartphone_producer_cv:
                self.smartphone_producer_cv.wait_for(lambda:self.a_space_is_available(self.smartphone_queue))
                
                self.smartphone_queue.append(id)
                print(f"[ServerImpl] - Added {id} to {articolo}")
                print(len(self.laptop_queue))
                
                self.smartphone_consumer_cv.notify()
        else:
            print(f"[Server Impl] - Articolo not recognized")
            success=False
            
        return success
    
    def preleva(self, articolo):
        id_item=-1
        
        if articolo=="laptop":
            with self.laptop_consumer_cv:
                print(self.laptop_queue)
                self.laptop_consumer_cv.wait_for(lambda:self.an_item_is_available(self.laptop_queue))
                
                id_item=self.laptop_queue.pop(0)
                print(f"[ServerImpl] - Got {id_item} from {articolo}")
                
                '''                
                with open(self.laptop_file_name,'a') as f:
                    f.write(f"{str(id_item)}\n")
                '''
                try:
                    collection=self.db["laptop"]
                    item={
                        "model": f"{id_item}",
                    }
                    collection.insert_one(item)
                except Exception as e:
                    print(f"[ServerImpl] - Couldn't save {id_item} to DB")
                finally:
                    self.laptop_producer_cv.notify()
                
        elif articolo=="smartphone":
            with self.smartphone_consumer_cv:
                print(self.smartphone_queue)
                self.smartphone_consumer_cv.wait_for(lambda:self.an_item_is_available(self.smartphone_queue))
                
                id_item=self.smartphone_queue.pop(0)
                print(f"[ServerImpl] - Got {id_item} from {articolo}")
                
                try:
                    collection=self.db["smartphone"]
                    item={
                        "model": f"{id_item}",
                    }
                    collection.insert_one(item)
                except Exception as e:
                    print(f"Exception: {e}")
                self.smartphone_producer_cv.notify()
        else:        
            print(f"[Server Impl] - Articolo not recognized")
        
        return id_item
        
    
    def an_item_is_available(self, queue):
        return len(queue)!=0
    
    def a_space_is_available(self,queue):
        return len(queue)<self.queue_size