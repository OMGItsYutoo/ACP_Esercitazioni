from time import sleep
from client.MyListener import MyListener
from random import randint, choice

import stomp

REQUESTS=["deposita", "preleva"]
N_MSG=10

if __name__=="__main__":
    conn=stomp.Connection([("localhost", 61613)], auto_content_length=False)
    conn.set_listener("", MyListener())
    
    conn.connect(wait=True)
    conn.subscribe("/queue/responses", id=1)
    
    for _ in range(N_MSG):
        request=choice(REQUESTS)
        
        if request=="deposita":
            id=randint(1,100)
            
            msg='-'.join([request,str(id)])
            
        else:
            msg=request

        conn.send("/queue/requests",msg, headers={"reply-to":"/queue/responses"})
        
        print(f"[Client] - Sent request: {msg}")
        
    
    sleep(20)
    
    conn.disconnect()    