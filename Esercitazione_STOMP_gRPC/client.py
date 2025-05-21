import stomp
import random
import time

class MyListener(stomp.ConnectionListener):
    
    def on_message(self, frame):
        print("[CLIENT] Response received %s" % frame.body)

def main():
    
    conn=stomp.Connection([('localhost',61613)])
    conn.set_listener("", MyListener())
    
    conn.connect(wait=True)
    
    conn.subscribe(destination='/queue/response', id=1, ack='auto')

    # Make the request
    products = ['smartphone', 'laptop']
    for i in range(15):
        if (i < 10):
                request = "deposita"
                id = random.randint(1,100)
                product = products[(i%2)]
                MSG = request + "-" + str(id) + "-" + product
        else:
            MSG = "preleva"

        # Send the request on the queue 'request'
        conn.send('/queue/request', MSG)

        print("[CLIENT] Request: ", MSG)
        
    # Make 'svuota' request
    MSG = "svuota"

    # Send the request on the queue 'request'
    conn.send('/queue/request', MSG)

    print("[CLIENT] Request: ", MSG)
    
    while True:
        time.sleep(60)
        
    conn.disconnect()

if __name__=="__main__":
    main()