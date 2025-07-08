from time import sleep
import sys
import stomp

class BwListener(stomp.ConnectionListener):
    
    def on_message(self, frame):
        print(f"[BwListener] - Received {frame.body}")
        
        with open("./server/bw.txt",'a') as f:
            f.write(f"{frame.body}\n")

if __name__=="__main__":
    try:
        type=sys.argv[1]
    except IndexError:
        print("Please insert printer type")
        
    if type!="bw" and type!="gs":
        print("Not supported type")
        raise Exception()
        
    conn=stomp.Connection()
    conn.set_listener("", BwListener())
    conn.connect(wait=True)
    
    conn.subscribe("/queue/bwqueue", id=1)
    
    while True:
        sleep(60)
        
    conn.disconnect()
        
        