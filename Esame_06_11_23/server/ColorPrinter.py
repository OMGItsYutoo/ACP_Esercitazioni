from time import sleep
import sys
import stomp

class ColorListener(stomp.ConnectionListener):

    def on_message(self, frame):
        print(f"[ColorListener] - Received {frame.body}")
        
        with open("./server/color.txt",'a') as f:
            f.write(f"{frame.body}\n")

if __name__=="__main__":
    try:
        type=sys.argv[1]
    except IndexError:
        print("Please insert printer type")
        
    if type!="doc" and type!="txt":
        print("Not supported type")
        raise Exception()
    
    conn=stomp.Connection()
    conn.set_listener("", ColorListener())
    conn.connect(wait=True)
    
    conn.subscribe("/queue/colorqueue", id=1)
    
    while True:
        sleep(60)
        
    conn.disconnect()
        