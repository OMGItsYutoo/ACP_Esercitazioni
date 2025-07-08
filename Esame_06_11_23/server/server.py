from server.PrinterServerImpl import PrinterServerImpl
from server.PrinterConsProcess import PrinterConsProcess
from multiprocessing import Queue, Value

IP='localhost'
PORT=0
QUEUE_SIZE=5
BUF_SIZE=1024

if __name__=="__main__":
    q=Queue(QUEUE_SIZE)
    server=PrinterServerImpl(IP, PORT, BUF_SIZE, q)
    p=PrinterConsProcess("PrinterConsProcess",q)
    p.start()
    server.runSkeleton()
    
    
    