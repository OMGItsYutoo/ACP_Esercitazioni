from time import sleep
from random import choice, randint

import stomp

N_MSG=10
REQUESTS=["deposita", "preleva"]

class ClientListener(stomp.ConnectionListener):
    def on_message(self, frame):
        print(f"[ClientListener] - Received: {frame.body}")

if __name__=="__main__":
    conn=stomp.Connection([("localhost",61613)])
    conn.set_listener("", ClientListener())
    
    conn.connect(wait=True)
    
    conn.subscribe("/queue/response", id=1)
    
    
    for i in range(N_MSG):
        
        if i<3: request="deposita"
        else: request=choice(REQUESTS)
        
        if request=="deposita":
            id_art=randint(1,10)
            msg='-'.join([request, str(id_art)])
        else:            
            msg="preleva"
        
        conn.send("/queue/request",msg)
    
    sleep(20)
    
    conn.disconnect()