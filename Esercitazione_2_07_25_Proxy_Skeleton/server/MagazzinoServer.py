from server.MagazzinoImpl import MagazzinoImpl

IP='localhost'
PORT=0
QUEUE_SIZE=50
BUF_SIZE=1024

if __name__=="__main__":
    print("Server running...")
    magazzinoImpl=MagazzinoImpl(IP, PORT, BUF_SIZE, QUEUE_SIZE)
    magazzinoImpl.runSkeleton()