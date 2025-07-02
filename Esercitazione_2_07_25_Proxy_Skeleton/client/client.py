from time import sleep

import stomp
import random

IP='localhost'
NUM_MSGS=10
REQUESTS=["deposita", "preleva"]

class MyListener(stomp.ConnectionListener):
    
    def on_message(self, frame):
        print(f'[Client] - Received response: "{frame.body}"')

        
if __name__=="__main__":
    
    conn=stomp.Connection([(IP, 61613)])
    conn.set_listener("", MyListener())
    conn.connect(wait=True)
    
    conn.subscribe(destination='/queue/responses', id=1)
    
    for _ in range(NUM_MSGS):
        request=random.choice(REQUESTS)
        id_art = random.randint(1,10)
        msg='-'.join([request, str(id_art)])
        
        conn.send("/queue/requests", msg)
        
        print(f"[Client] - Request sent ({request})")
        
    sleep(10)
    
    conn.disconnect()
