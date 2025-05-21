import stomp
import sys
import time
import grpc
from multiprocess import Process

def proc_req(port, mess):

    request = mess.split('-')[0]

    # Create connection
    conn = stomp.Connection([('127.0.0.1', 61613)])

    # Connect and subscribe to the queue 'request'
    conn.connect(wait=True)


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