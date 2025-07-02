from dispatcher.MagazzinoProxy import MagazzinoProxy
from dispatcher.DispatcherProcess import DispatcherProcess

import sys
import stomp
import time

class MyListener(stomp.ConnectionListener):
    def __init__(self, ip, port, buf_size):
        self.ip=ip
        self.port=port
        self.buf_size=buf_size
        
    def on_message(self, frame):
        
        print(hex(id(frame)))
        print(f'[Dispatcher] Request received: "{frame.body}"')
        
        proxy=MagazzinoProxy(self.ip, self.port, self.buf_size)
        
        p=DispatcherProcess("ProxyProcess",proxy, frame.body)
        p.start()

IP='localhost'
BUF_SIZE=1024

if __name__=="__main__":
    try:
        PORT=int(sys.argv[1])
    except IndexError:
        print("Please, specify PORT of the server waiting of dispatcher requests")
        
    conn=stomp.Connection([("localhost",61613)])
    conn.set_listener("",MyListener(IP, PORT, BUF_SIZE))
    
    conn.connect(wait=True)
    conn.subscribe("/queue/requests", id=1)
    
    print("[Dispatcher] - Waiting for requests ... ")
    
    #keeping the listener active
    while True:
        time.sleep(60)
        
    conn.disconnect()
    
