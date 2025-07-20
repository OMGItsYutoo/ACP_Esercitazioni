from time import sleep
from random import choice, randint
import stomp

REQ=["preleva","deposita"]
N_MSG=10

class ClientListener(stomp.ConnectionListener):
    def __init__(self):
        pass
    
    def on_message(self, frame):
        print(f"[ClientListener] - Received {frame.body}")

if __name__=="__main__":
    conn=stomp.Connection([("localhost",61613)], auto_content_length=False)
    conn.set_listener("", ClientListener())
    conn.connect(wait=True)
    
    conn.subscribe("/queue/response", id=1)
    
    #sending req
    for i in range(N_MSG):
        if i<3: request=REQ[1]
        else: request=choice(REQ)
        
        if request=="deposita":
            id_art=randint(1,10)
        
            msg='-'.join([request, str(id_art)])
        else:
            msg=request
        
        conn.send("/queue/request",msg, headers={"reply-to":"/queue/response"})
        print(f"[Client] - Sent {msg} request")
        
    sleep(20)
    
    conn.disconnect()