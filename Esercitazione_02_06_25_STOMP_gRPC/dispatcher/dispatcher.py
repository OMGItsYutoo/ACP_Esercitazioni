from multiprocessing import Process
from proto import service_pb2_grpc, service_pb2
import time
import grpc
import stomp
import argparse

PORT=61613

def proc_fun(port, msg:str):
    msg_split=msg.split('-')
    
    #a connection for every process, more robust and scalable
    conn=stomp.Connection([("localhost",PORT)])
    conn.connect(wait=True)
    
    channel=grpc.insecure_channel("localhost:"+str(port))
    stub=service_pb2_grpc.ServiceStub(channel)
    
    if msg_split[0]=="deposita":
        
        id=msg_split[1]
        product=msg_split[2]
        result=stub.deposita(service_pb2.Item(id=int(id),product=product))
        print(f'[Dispatcher] - Response: {result.response}')
        conn.send('/queue/responses', result.response)
        
    elif msg_split[0]=="preleva":
        
        result=stub.preleva(service_pb2.Empty())
        print(f'[Dispatcher] - Response: {str(result)}')
        conn.send('/queue/responses',str(result.id)+'-'+result.product)
    
    elif msg_split[0]=="svuota":
        
        results=stub.svuota(service_pb2.Empty())
        for res in results:
            print("[DISPATCHER] Response:", str(res))
            conn.send('/queue/response', str(res.id) + "-" + res.product)

class MyListener(stomp.ConnectionListener):
    def __init__(self, port):
        self.port=port
    
    def on_message(self, frame):
        print(f'[Dispatcher] - Request received: {frame.body}')
        
        p=Process(target=proc_fun,args=(self.port,frame.body))
        p.start()

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("port",help="Porto su cui il server è in ascolto")
    args=parser.parse_args()
    
    conn=stomp.Connection([("localhost", PORT)])
    conn.set_listener("",MyListener(args.port))
    
    conn.connect(wait=True)
    conn.subscribe('/queue/requests',id=1, ack="auto")
    
    print("[Dispatcher] - Waiting for requests ... ")

    #keeping the listener active
    while True:
        time.sleep(60)
    
if __name__=="__main__":
    main()