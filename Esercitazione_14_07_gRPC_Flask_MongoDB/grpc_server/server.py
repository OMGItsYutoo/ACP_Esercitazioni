from concurrent import futures
from proto import statistics_pb2_grpc
from grpc_server.StatisticsImpl import StatisticsImpl
from time import sleep
from pymongo import MongoClient

import grpc

def get_database():
    client=MongoClient("localhost", 27017)
    return client["sensors_data"]

if __name__=="__main__":
    
    db=get_database()
    
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    statistics_pb2_grpc.add_StatisticsServicer_to_server(StatisticsImpl(db),server)
    port=server.add_insecure_port("localhost:"+str(0))
    server.start()
    
    print(f"Server is listening on port: {port}")
    
    sleep(60)
    
    server.wait_for_termination()