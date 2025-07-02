from proto import service_pb2_grpc
from time import sleep
from dispatcher.DispatcherProcess import DispatcherProcess
import grpc
import sys
import stomp

class MyListener(stomp.ConnectionListener):
    def __init__(self, stub):
        self.stub=stub
    
    def on_message(self, frame):
        print(f"[Dispatcher] - Received {frame.body}")
        
        p=DispatcherProcess("DispatcherProcess", self.stub, frame.body)
        p.start()
        

if __name__=="__main__":
    try:
        port=int(sys.argv[1])
    except IndexError:
        print("Please, insert the port the server is listening on")
        
    channel=grpc.insecure_channel("localhost:"+str(port))
    stub=service_pb2_grpc.ServiceStub(channel)
    
    conn=stomp.Connection([("localhost", 61613)])
    conn.set_listener("",MyListener(stub))
    conn.connect(wait=True)
    
    conn.subscribe("/queue/requests",id=1)
    
    while True:
        sleep(60)
        
    conn.disconnect()