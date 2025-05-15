import ordermanagement_pb2_grpc
import ordermanagement_pb2


import grpc
import time
import sys
import multiprocess as mp

def run(port):
    channel=grpc.insecure_channel("localhost:"+str(port))
    
    stub=ordermanagement_pb2_grpc.OrderManagementStub(channel)
    
    orders=[]
    orders.append(ordermanagement_pb2.Order(items=['A','B','A','B'], price=2000.00, description='La madonna è una brava donna',destination="RRRRRROOOOOMAAAAA"))
    orders.append(ordermanagement_pb2.Order(items=['A','B','ACCIPICCHIA','B'], price=1000.00, description='La malonna è una brava donna',destination="NAAAAAAAAPL"))
    
    
    for order in orders:
        response=stub.addOrder(order)
        print("addOrder invocation...... response:", response)
        order = stub.getOrder(response)
        print("getOrder() invoked. Response: ", order)


    
    
if __name__=="__main__":
    try:
        port=sys.argv[1]
    except:
        print("Ma si strunz, c manc o port")
        
    run(port)