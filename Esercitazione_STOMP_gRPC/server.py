import grpc
import service_pb2_grpc
import service_pb2
from concurrent import futures
from multiprocess import Queue
from threading import Lock

QUEUE_SIZE=5

class ServiceImpl(service_pb2_grpc.ServiceServicer):
    def __init__(self, queue: Queue, lock_d, lock_p):
        self.queue=queue
        self.lock_d=lock_d
        self.lock_p=lock_p
    
    def deposita(self, request, context):
        
        with self.lock_d:
            self.queue.put((request.id_articolo,request.product))
        
        print("[SERVER-IMPL] Depositato [" + str(request.id_articolo) + ", " + request.product + "]")
        return service_pb2.StringMessage(deposited_string="deposited")
    
    def preleva(self, request, context):
        
        with self.lock_p:
            item=self.queue.get()
        
        print("[SERVER-IMPL] Prelievo effettuato")

        return service_pb2.Item(id_articolo=item[0],product=item[1])
    
    def svuota(self, request, context):
        '''
        not thread safe only using multiprocessing.Queue
        '''
        
        self.lock_d.acquire()
        self.lock_p.acquire()
        
        while not self.queue.empty():
            item=self.queue.get()
            
            yield service_pb2.Item(id_articolo=item[0],product=item[1])
        
        self.lock_d.release()
        self.lock_p.release()
        
def serve():
    q=Queue(QUEUE_SIZE)
    lock_d=Lock()
    lock_p=Lock()
    
    # Creating gRPC Server - NOTE:  options=(('grpc.so_reuseport', 0) allows raising an exception if a port is already used
    # WARNING: Scegliere opportunamente il numero di Worker, se infatti tutti i worker restano bloccati su chiamate bloccanti, 
    # il server non riuscirà a gestire altre richieste
    
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=(('grpc.so_reuseport', 0),)) 
    service_pb2_grpc.add_ServiceServicer_to_server(ServiceImpl(q,lock_d,lock_p),server)
    
    port=server.add_insecure_port("[::]:0")
    
    server.start()
    print(f"server grpc in ascolto su port {port}")
    server.wait_for_termination()

if __name__=="__main__":
    serve()
