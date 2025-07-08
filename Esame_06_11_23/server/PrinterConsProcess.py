from multiprocessing import Process, Queue
import socket
import stomp

class PrinterConsProcess(Process):
    def __init__(self, name, queue: Queue):
        super().__init__(name=name)
        self.queue=queue
        
    def run(self):
        print(f"[{self.name}] - Running")
        
        sconn=stomp.Connection([("localhost",61613)])
        sconn.connect(wait=True)
            
        while True:
            msg=self.queue.get()
            
            print(f"[{self.name}] - Got {msg} from the queue")
           
            msg_split=msg.split('-')
            
            if msg_split[1]=="bw":
                sconn.send("/queue/bwqueue", msg_split[0])           
            elif msg_split[1]=="color":
                sconn.send("/queue/colorqueue", msg_split[0])
            elif msg_split[1]=="gs":
                sconn.send("/queue/bwqueue", msg_split[0])
            else:
                print(f"[{self.name}] - Couldn't recognized the printing service")
            
        sconn.disconnect()