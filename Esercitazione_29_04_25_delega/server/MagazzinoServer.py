from .MagazzinoImpl import MagazzinoImpl
from .MagazzinoSkeleton import MagazzinoSkeleton

IP_ADDR='localhost'
PORT=12122
QUEUE_SIZE=5

magazzino=MagazzinoImpl(QUEUE_SIZE)
magazzino_skel=MagazzinoSkeleton(IP_ADDR,PORT,magazzino)
magazzino_skel.runSkeleton()