import stomp
from random import randint
from time import sleep

class MyListener(stomp.ConnectionListener):
    def on_message(self, frame):
        print(f"[Client] - Received response {frame.body}")

def main():
    conn=stomp.Connection([("localhost",61613)])
    conn.set_listener("",MyListener())
    
    conn.connect(wait=True)
    conn.subscribe('/queue/responses',id=1)
    
    products=["smarphone","laptop"]
    
    for i in range(15):
        if i<10:
            request="deposita"
            id=randint(1, 100)
            product = products[(i%2)]
            msg='-'.join([request,str(id),product])     
        else:
            msg="preleva"
            
        conn.send('/queue/requests',msg)
        print(f"[Client] Request: {msg}")
    
    sleep(5)
    msg="svuota"
    
    print(f"[Client] Request: {msg}")
    conn.send('/queue/requests',msg)
    
    #keeping the listener active
    sleep(10)
    
    conn.disconnect()
    
if __name__=="__main__":
    main()