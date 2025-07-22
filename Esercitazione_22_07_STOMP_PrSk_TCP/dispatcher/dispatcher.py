from dispatcher.DispatcherProcess import DispatcherProcess
from time import sleep
import stomp
import sys

IP="localhost"
BUF_SIZE=1024

class DispatcherListener(stomp.ConnectionListener):
    
    def __init__(self, ip, port, buf_size):
        self.ip=ip
        self.port=port
        self.buf_size=buf_size
    
    def on_message(self, frame):
        print(f"[DispatcherListener] - Received {frame.body}")
        
        dp=DispatcherProcess("DispatcherProcess",self.ip, self.port, self.buf_size, frame.body)
        dp.start()

if __name__=="__main__":
    
    try:
        port=int(sys.argv[1])
    except IndexError:
        print("Please specify the port the server is listening on.")
    
    conn=stomp.Connection([("localhost",61613)])
    conn.set_listener("", DispatcherListener(IP, port, BUF_SIZE))
    
    conn.connect(wait=True)
    
    print("[Dispatcher] - Waiting for requests to dispatch")
    
    conn.subscribe("/queue/request",id=1)
    
    while True:
        sleep(60)
    
    conn.disconnect()