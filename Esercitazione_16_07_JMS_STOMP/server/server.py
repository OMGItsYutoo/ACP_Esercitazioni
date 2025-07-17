from server.ServiceImpl import ServiceImpl

IP="localhost"
PORT=12312
BUF_SIZE=1024
QUEUE_SIZE=5

if __name__=="__main__":
    serviceImpl=ServiceImpl(IP, PORT, BUF_SIZE, QUEUE_SIZE)
    serviceImpl.runSkeleton()