import stomp
import sys
import time
import grpc
from multiprocess import Process
import service_pb2_grpc, service_pb2

def proc_req(port, mess):
    msg_split=mess.split('-')
    request = msg_split[0]

    # Create connection
    conn = stomp.Connection([('127.0.0.1', 61613)])

    # Connect and subscribe to the queue 'request'
    conn.connect(wait=True)
    
    channel=grpc.insecure_channel('localhost:' + str(port))
    stub=service_pb2_grpc.ServiceStub(channel)
    
    if request=="deposita":
        id=int(msg_split[1])
        prod=msg_split[2]
        result=stub.deposita(service_pb2.Item(id_articolo=id,product=prod))
        print("[DISPATCHER] Response:", result.deposited_string)
        conn.send("/queue/response",result.deposited_string)
    elif request=="preleva":
        result=stub.preleva(service_pb2.Empty())
        print("[DISPATCHER] Response:", result)
        conn.send("/queue/response",str(result.id_articolo)+'-'+result.product)
    else:
        results=stub.svuota(service_pb2.Empty())
        
        for result in results:
            print("[DISPATCHER] Response:", result)
            conn.send("/queue/response",str(result.id_articolo)+'-'+result.product)

# Listener
class MyListener(stomp.ConnectionListener):
    
    def __init__(self, port):
        self.port = port

    def on_message(self, frame):
        
        print('[DISPATCHER] Request received: "%s"' % frame.body)

        # Start a process to serve the request
        p = Process(target=proc_req, args=(self.port, frame.body))
        p.start()

def main():
    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Please, specify PORT arg")

    # Create connection
    conn = stomp.Connection([('127.0.0.1', 61613)])

    # Set the listener
    conn.set_listener('', MyListener(PORT))

    # Connect and subscribe to the queue 'request'
    conn.connect(wait=True)
    conn.subscribe(destination='/queue/request', id=1, ack='auto')
    
    print("[DISPATCHER] Waiting for request ... ")

    # Keep the listener active
    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()