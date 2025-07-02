from time import sleep
import stomp
import random

NUM_MSGS=5
REQUESTS=["deposita", "svuota"]
PRODUCTS=["laptop","smartphone"]

class MyListener(stomp.ConnectionListener):
    def on_message(self, frame):
        print(f"[Client] - Received message: {frame.body}")

if __name__=="__main__":
    conn=stomp.Connection([('localhost',61613)])
    conn.set_listener("", MyListener())
    
    conn.connect(wait=True)
    conn.subscribe("/queue/responses", id=1)
    
    for _ in range(NUM_MSGS):
        request=random.choice(REQUESTS)
        if request=="deposita":
            product=random.choice(PRODUCTS)
            id_art=random.randint(0,10)
            msg='-'.join([request, str(id_art), product])
        else:
            msg=request
            
        print(f"[Client] - Sending: {msg}")
            
        conn.send("/queue/requests",msg)
    
    sleep(10)
    
    conn.disconnect()