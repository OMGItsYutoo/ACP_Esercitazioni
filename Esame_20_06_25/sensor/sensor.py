from proto import service_pb2, service_pb2_grpc
import grpc
import sys
import random

NUM_REQ=5
NUM_TEMPSTRM=5

def generate_request():
    for _ in range(NUM_TEMPSTRM):
        data=random.randint(50,100)
        print(f"[Sensor] - Generated and sending: {data}")
        yield service_pb2.Data(value=data)
        
if __name__=="__main__":
    try:
        port=int(sys.argv[1])
    except IndexError:
        print("Please insert the port the checker is listening on")    
        
    channel=grpc.insecure_channel("localhost:"+str(port))
    stub=service_pb2_grpc.ServiceStub(channel)
    
    for _ in range(NUM_REQ):
        mess=stub.stream_temp(generate_request())
        print(f"[Sensor] - Message: {mess.stringmess}")
        
        avg=stub.get_average(service_pb2.Empty())
        print(f"[Sensor] - Average: {avg.mean}")
        
    
    