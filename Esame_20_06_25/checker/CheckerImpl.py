from proto import service_pb2, service_pb2_grpc
from multiprocessing import Queue
import stomp

class CheckerImpl(service_pb2_grpc.ServiceServicer):
    def __init__(self, queue_size, threshold):
        self.q=Queue(queue_size)
        self.threshold=threshold
    
    def stream_temp(self, request, context):
        
        # data=request.value gives Exception because request, in this case, is an Iterator
        alert = False

        for req in request:
            data=req.value
            
            print(f"[CheckerImpl] - Received: {data}")
            self.q.put(data)
            
            if data>self.threshold:
                alert = True

                #stomp
                conn=stomp.Connection([('localhost',61613)])
                conn.connect(wait=True)
                
                conn.send("/topic/alert",str(data))
                
        if alert:
            return service_pb2.Message(stringmess="ALERT")
        else:
            return service_pb2.Message(stringmess="NORMAL")

    def get_average(self, request, context):
        data=[]
        
        while not self.q.empty():
            data.append(self.q.get())
            
        avg=sum(data)/len(data)
        
        return service_pb2.Average(mean=avg)