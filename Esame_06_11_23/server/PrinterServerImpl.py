from server.PrinterServerSkeleton import PrinterServerSkeleton
from server.PrinterProdProcess import PrinterProdProcess
from multiprocessing import Queue

class PrinterServerImpl(PrinterServerSkeleton):
    def __init__(self, ip, port, buf_size, queue):
        super().__init__(ip, port, buf_size)
        self.queue=queue
        
    def print(self, pathFile, tipo):
                
        msg='-'.join([pathFile, tipo])
        
        p=PrinterProdProcess("PrinterProdProcess", self.queue, msg)
        p.start()