from proto import magazzino_pb2, magazzino_pb2_grpc
from server.MagazzinoImpl import MagazzinoImpl
from concurrent import futures
from time import sleep
import grpc

QS=5

if __name__=="__main__":
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    magazzino_pb2_grpc.add_MagazzinoServicer_to_server(MagazzinoImpl(QS),server)
    port=server.add_insecure_port("localhost:0")
    server.start()
    
    print(f"Server is listening on port: {port}")
    
    sleep(120)
    
    server.wait_for_termination()
    
    