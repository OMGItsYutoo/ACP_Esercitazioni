from IMagazzino import IMagazzino
from multiprocessing import Lock,Condition

class MagazzinoImpl(IMagazzino):
    
    def __init__(self,queue_size):
        self.laptop_queue=[]
        self.smartphone_queue=[]
        self.queue_size=queue_size
        
        cv_laptop_lock=Lock()
        self.laptop_consumer_cv=Condition(lock=cv_laptop_lock)
        self.laptop_producer_cv=Condition(lock=cv_laptop_lock)
        
        cv_smartphone_lock=Lock()
        self.smartphone_consumer_cv=Condition(lock=cv_smartphone_lock)
        self.smartphone_producer_cv=Condition(lock=cv_smartphone_lock)
        
        self.laptop_file_name = "laptop.txt"
        self.smartphone_file_name = "smartphone.txt"
        
        laptop_file=open(self.laptop_file_name,'a')
        laptop_file.truncate(0)
        
        smartphone_file=open(self.smartphone_file_name,'a')
        smartphone_file.truncate(0) 
        
    def deposita(self, articolo, id):
        success=True
        if articolo=="laptop":
            
            with self.laptop_producer_cv:
                self.laptop_producer_cv.wait_for(lambda:self.theres_a_space(self.laptop_queue))
                
                self.laptop_queue.append(id)
                print(f"[MAGAZZINO IMPL] Added {id} in {articolo}")

                self.laptop_consumer_cv.notify()
            
        elif articolo=="smartphone":
            
            with self.smartphone_producer_cv:
                self.smartphone_producer_cv.wait_for(lambda:self.theres_a_space(self.smartphone_queue))
                
                self.smartphone_queue.append(id)
                print(f"[MAGAZZINO IMPL] Added {id} in {articolo}")

                self.smartphone_consumer_cv.notify()
                
        else:
            print("[MAGAZZINO IMPL] Articolo non riconosciuto")
            success=False
                
        return success
    
    def preleva(self, articolo):
        id_item=-1
        
        if articolo=="laptop":
            
            with self.laptop_consumer_cv:
                self.laptop_producer_cv.wait_for(lambda:self.theres_an_item(self.laptop_queue))
            
                id_item=self.laptop_queue.pop(0)
                print(f"[MAGAZZINO IMPL] Got {id_item} from {articolo}")

                with open(self.laptop_file_name,'a') as f:
                    f.write(f"Id: {id_item}\n")
                
                self.laptop_producer_cv.notify()
                
        elif articolo=="smartphone":
            
            with self.smartphone_consumer_cv:
                self.smartphone_producer_cv.wait_for(lambda:self.theres_an_item(self.smartphone_queue))
                
                id_item=self.smartphone_queue.pop(0)
                print(f"[MAGAZZINO IMPL] Got {id_item} from {articolo}")
                
                with open(self.smartphone_file_name,'a') as f:
                    f.write(f"Id: {id_item}\n")
                
                self.smartphone_producer_cv.notify()
            
        else:
            print("[MAGAZZINO IMPL] Articolo non riconosciuto")
        
        return id_item
    
    def theres_a_space(self,queue):
        return len(queue)!=self.queue_size
    
    def theres_an_item(self,queue):
        return len(queue)!=0