from concurrent import futures
from proto import service_pb2_grpc
from server.ServerImpl import ServerImpl
from time import sleep
import grpc

PORT=0
QUEUE_SIZE=5

if __name__=="__main__":
    server=grpc.server(thread_pool=futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ServiceServicer_to_server(ServerImpl(QUEUE_SIZE), server)
    port=server.add_insecure_port("localhost:"+str(PORT))
    server.start()
    
    print(f"Server running on port {str(port)}")
    
    sleep(60)
    
    server.wait_for_termination()