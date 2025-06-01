from server.MagazzinoImpl import MagazzinoImpl
from server.MagazzinoSkeleton import MagazzinoSkeleton
from pymongo import MongoClient

QUEUE_SIZE=20
IP='localhost'
PORT=12123

def get_database():
    client=MongoClient("localhost",27017)
    return client['Magazzino_TCP_delega']

def main():
    magazzino=MagazzinoImpl(QUEUE_SIZE,get_database())
    skeleton=MagazzinoSkeleton(IP,PORT,1024,magazzino)
    skeleton.runSkeleton()

    print("[MagazzinoServer] Started")
    
if __name__=="__main__":
    main()