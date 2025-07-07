from concurrent import futures
from proto import service_pb2,service_pb2_grpc
from checker.CheckerImpl import CheckerImpl
from time import sleep
import grpc
import sys

QS=5

if __name__=="__main__":
    try:
        th=int(sys.argv[1])
    except IndexError:
        print("Please insert threshold value")
    
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ServiceServicer_to_server(CheckerImpl(QS, th),server)
    port=server.add_insecure_port("localhost:"+str(0))
    
    server.start()
    
    print("Checker listening on port: "+str(port))

    sleep(10)    
    
    server.wait_for_termination()