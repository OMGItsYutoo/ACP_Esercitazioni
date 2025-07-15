from threading import Thread
from random import choice, randint
from proto import service_pb2

class UserThread(Thread):
    def __init__(self, name, stub, operations):
        super().__init__(name=name)
        self.stub=stub
        self.operations=operations
        
    def run(self):
        operation=choice(self.operations)
        
        if operation=="buy":
            response=self.stub.buy(service_pb2.Empty())
        elif operation=="sell":
            serial_number=randint(1,100)
            response=self.stub.sell(service_pb2.Item(serial_number=serial_number))  
        else:
            print(f"[{self.name}] - An error occurred")
            
        print(f"[{self.name}] - Received: {response}")