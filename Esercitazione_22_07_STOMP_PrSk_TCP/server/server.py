from server.MagazzinoImpl import MagazzinoImpl

IP="localhost"
PORT=0
BUF_SIZE=1024
QUEUE_SIZE=5

if __name__=="__main__":
    serverImpl=MagazzinoImpl(IP, PORT, BUF_SIZE, QUEUE_SIZE)
    serverImpl.runSkeleton()