from multiprocessing import Process, Queue, current_process
from time import sleep
import stomp

def tickets_proc_fun(q:Queue, msg):
    q.put(msg)
    print(f"[{current_process().name}] - Added {msg} to the queue")
    
def stats_proc_fun(q:Queue):
    stats={}
    
    #filling stats dict
    while not q.empty():
        auth=q.get()
        print(f"[{current_process().name}] - Got {auth} from the queue")
        
        if auth in stats.keys():    
            stats[auth]+=1
        else:
            stats[auth]=1
            
    with open("./stats/stats.txt","a") as f:
        for key, value in stats.items():
            f.write(f"{key}: {value}\n")
    
    
class MyListener(stomp.ConnectionListener):
    def __init__(self, queue):
        self.queue=queue
    
    def on_message(self, frame):
        print(f"[StatsListener] - Received: {frame.body}")
        
        destination=frame.headers.get(('destination'))
        print(f"[StatsListener] - Destination: {destination}")
        
        if destination=='/topic/tickets':
            t=Process(name="TicketsThread", target=tickets_proc_fun, args=(self.queue, frame.body))
            t.start()
            
        elif destination=="/topic/stats":
            if "Sold" in frame.body:
                t=Process(name="StatsThread", target=stats_proc_fun, args=(self.queue,))
                t.start()

if __name__=="__main__":
    conn=stomp.Connection([("localhost",61613)], auto_content_length=False)
    conn.set_listener("", MyListener(Queue()))
    conn.connect(wait=True)
    
    print("[Stats] - Waiting for messages")
    
    conn.subscribe("/topic/stats", id=1)
    conn.subscribe("/topic/tickets", id=1)
    
    while True:
        sleep(60)
        
    conn.disconnect()