from threading import Thread, current_thread
from client.MagazzinoProxy import MagazzinoProxy
import time, random
import argparse

NUM_THREADS = 20
NUM_REQS_THREADS = 30
IP = 'localhost'
BUF_SIZE=1024

SMARTPHONE = [
    "iPhone 15 Pro",
    "Samsung Galaxy S24",
    "Google Pixel 8",
    "OnePlus 12",
    "Xiaomi 14",
    "Sony Xperia 1 V"
]

# Lista di modelli di laptop
LAPTOP = [
    "MacBook Air M3",
    "Dell XPS 15",
    "HP Spectre x360",
    "Lenovo ThinkPad X1 Carbon",
    "ASUS ROG Zephyrus G14",
    "Microsoft Surface Laptop 6"
]

def thread_fun(service, ip, port, buf_size, num_req):
    
    waiting_time = random.randint(2, 4)
    time.sleep(waiting_time)
    
    proxy=MagazzinoProxy(ip, port, buf_size)
    
    for _ in range(num_req):
        
        choice=random.randint(0,1)
        if choice==0: articolo="smartphone"
        else: articolo="laptop"
        
        ids=[]

        if service=="deposita":
            
            if articolo=="smartphone": id_item=random.choice(SMARTPHONE)
            else: id_item=random.choice(LAPTOP)
            
            print(f"[{current_thread().name}] - Sending request {service}, {articolo}, {id_item}")
            
            result=proxy.deposita(articolo,id_item)
            
            if not result: #if result==None
                print(f"[{current_thread().name}] Request {service}, {articolo}, {id_item} failed!")
            else:
                print(f"[{current_thread().name}] Request {service}, {articolo}, {id_item} succeeded!")
        elif service=="preleva":
            
            print(f"[{current_thread().name}] - Sending request {service}, {articolo}")
            result=proxy.preleva(articolo)
            
            if result==-1:
                print(f"[{current_thread().name}] Request {service}, {articolo} failed!")
            else:
                print(f"[{current_thread().name}] Request {service}, {articolo} succeeded!")
                
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("service", help="Servizio da utilizzare")
    parser.add_argument("port", help="Port su cui è in ascolto il server")
    args=parser.parse_args()
    print(f"service: {args.service}, port: {args.port}")
    
    th=[]
    
    for i in range(NUM_THREADS):
        t=Thread(target=thread_fun, args=(args.service, IP, int(args.port), BUF_SIZE, NUM_REQS_THREADS), name=f"Client thread - {str(i)}")
        th.append(t)
        t.start()
        
    for _ in range(NUM_THREADS):
        th.pop().join()
    
if __name__=="__main__":
    main()