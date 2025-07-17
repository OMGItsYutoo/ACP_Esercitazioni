from threading import Thread
from random import choice, randint
from time import sleep
import stomp
import sys

CLIENTS=["Alessio", "Giggino", "Danilo", "Gainmarco", "Mattia", "Stefano"]
HOTELS=["Vesuvio", "Ipsoas", "HotelBello", "HotelMoltoBello", "HotelMoltoMoltoBello"]

def create_th_fun(operator):
    connc=stomp.Connection([("localhost",61613)])
    connc.connect(wait=True)
    
    client=choice(CLIENTS)
    hotel=choice(HOTELS)
    nights=randint(1,7)
    people=randint(1,5)
    cost=randint(50,300)
    
    msg='-'.join(["CREATE",client, hotel, operator, str(nights), str(people), str(cost)])

    connc.send("/topic/requests", msg)
    
    connc.disconnect()

def update_th_fun(operator):
    connu=stomp.Connection([("localhost",61613)])
    connu.connect(wait=True)

    discount=randint(50,100)    
    nights=randint(1,4)
    
    msg='-'.join(["UPDATE", str(discount), operator, str(nights)])
    
    connu.send("/topic/requests", msg)
    
    connu.disconnect()

class MyListener(stomp.ConnectionListener):
    def on_message(self, frame):
        print(f"[OperatorListener] - Received {frame.body}")

if __name__=="__main__":
    try:
        operator=sys.argv[1]  
    except IndexError:
        print("Please insert the operator identifier.")
        
    conn=stomp.Connection([("localhost",61613)])
    conn.set_listener("", MyListener())
    
    conn.connect(wait=True)
    
    conn.subscribe("/topic/responses", id=1)
    
    threads = []
    for i in range(6):
        if i < 4:
            t = Thread(target=create_th_fun, args=(operator,))
        else:
            t = Thread(target=update_th_fun, args=(operator,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        
    sleep(10)
        