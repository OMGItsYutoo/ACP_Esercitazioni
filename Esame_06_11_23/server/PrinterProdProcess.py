from multiprocessing import Process
import stomp

class PrinterProdProcess(Process):
    def __init__(self, name, queue, msg):
        super().__init__(name=name)
        self.queue=queue
        self.msg=msg
        
    def run(self):
        print(f"[{self.name}] - Running")
        print(f"[{self.name}] - Inserting {self.msg} in the queue")
        self.queue.put(self.msg)
        
        