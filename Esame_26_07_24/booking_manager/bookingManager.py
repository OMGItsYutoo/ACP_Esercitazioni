from time import sleep
from booking_manager.MyListener import MyListener

import stomp

BASE_URL="http://localhost:5000"

if __name__=="__main__":
    conn=stomp.Connection([("localhost",61613)])
    conn.set_listener("", MyListener(BASE_URL, conn))
    
    conn.connect(wait=True)
    
    conn.subscribe("/topic/requests", id=1)
    
    while True:
        sleep(120)
        
    conn.disconnect()
    
    