from dashboard.MyListener import MyListener
from time import sleep
import stomp


if __name__=="__main__":
    conn=stomp.Connection([('localhost',61613)])
    conn.set_listener("", MyListener())
    
    conn.connect(wait=True)
    
    conn.subscribe("/topic/alert",id=1)
    
    while True:
        sleep(60)
        
    conn.disconnect()