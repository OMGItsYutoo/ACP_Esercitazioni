from MagazzinoSkeleton import MagazzinoSkeleton
from threading import Lock, Condition

class MagazzinoImpl(MagazzinoSkeleton):
    
    def __init__(self, ip, port, queue_size=5):
        super.__init__(ip, port)
        
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
                self.laptop_producer_cv.wait_for(self.a_space_is_available(self.laptop_queue))
                
                self.laptop_queue.append(id)
                
                self.laptop_consumer_cv.notify()
        
        elif articolo=="smartphone":
            
            with self.smartphone_producer_cv:
                self.smartphone_producer_cv.wait_for(self.a_space_is_available(self.smartphone_queue))
            
                self.smartphone_queue.append(id)
                
                self.smartphone_consumer_cv.notify()
                
        else:
            print("[MAGAZZINO IMPL] Articolo non riconosciuto")
            success=False
            
        return success
        
    def preleva(self, articolo):
        id_item=-1
        
        if articolo=="laptop":
            
            with self.laptop_consumer_cv:
                self.laptop_producer_cv.wait_for(self.an_item_is_available(self.laptop_queue))
            
                id_item=self.laptop_queue.pop()
                
                self.laptop_producer_cv.notify()
                
        elif articolo=="smartphone":
            
            with self.smartphone_consumer_cv:
                self.smartphone_producer_cv.wait_for(self.an_item_is_available(self.laptop_queue))
                
                id_item=self.smartphone_queue.pop()
                
                self.smartphone_producer_cv.notify()
                
                

    def a_space_is_available(self, queue):
        return not (len(queue) == self.queue_size)
    
    def an_item_is_available(self, queue):
        return not (len(queue) == 0)