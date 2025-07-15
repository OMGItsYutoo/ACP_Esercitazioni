from proto import service_pb2_grpc
from user.UserThread import UserThread
import grpc
import sys

OPERATIONS=["buy", "sell"]

if __name__=="__main__":
    try:
        port=int(sys.argv[1])
    except IndexError:
        print("Please specify the port the product manager is listening on.")
    
    channel=grpc.insecure_channel("localhost:"+str(port))
    stub=service_pb2_grpc.ServiceStub(channel)
    
    ths=[]
    for i in range(10):
        t=UserThread(f"UserThread-{i+1}", stub, OPERATIONS)
        t.start()
        ths.append(t)
        
    for t in ths:
        t.join()