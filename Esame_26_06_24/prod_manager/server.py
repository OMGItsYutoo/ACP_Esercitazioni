from proto import service_pb2_grpc
from time import sleep
from concurrent import futures
from prod_manager.ProductManager import ProductManager

import grpc

QS=5
BASE_URL="http://localhost:5000"

if __name__=="__main__":
    
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ServiceServicer_to_server(ProductManager(QS, BASE_URL),server)
    port=server.add_insecure_port("localhost:0")
    server.start()
    
    print(f"Server is listening on port: {port}")
    
    sleep(60)
    
    server.wait_for_termination()
    