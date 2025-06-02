from server.ServerImpl import ServerImpl
from concurrent import futures
from proto import service_pb2_grpc
import grpc
import time

QUEUE_SIZE=5

def main():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ServiceServicer_to_server(ServerImpl(QUEUE_SIZE),server)
    port=server.add_insecure_port("localhost:"+str(0))
    
    server.start()
    print('Starting server. Listening on port ' + str(port))

    time.sleep(60)
    
    server.wait_for_termination()

if __name__=="__main__":
    main()