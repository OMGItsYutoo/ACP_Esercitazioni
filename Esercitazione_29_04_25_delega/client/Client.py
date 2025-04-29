from threading import Thread,current_thread
from client.MagazzinoProxy import MagazzinoProxy
import sys, random, time

NUM_THREADS = 5
NUM_REQS_THREADS = 3
IP = 'localhost'

def thread_fun(service, ip, port, num_reqs):
    waiting_time = random.randint(2, 4)
    time.sleep(waiting_time)
    
    proxy=MagazzinoProxy(ip,port)
    
    for i in range(num_reqs):
    
        # Genero in maniera casuale l'articolo
        choice = random.randint(0, 1)
        
        if choice == 0:
            articolo = "smartphone"
        else:
            articolo = "laptop"
            
        if service=="deposita":
            id_item = random.randint(1, 100)

            print(f"[{current_thread().name}] Sending request {service}, {articolo}, {id_item}")
            
            result=proxy.deposita(articolo,id_item)
            
            if not result:
                print(f"[{current_thread().name}] Request {service}, {articolo}, {id_item} failed!")
            else:
                print(f"[{current_thread().name}] Request {service}, {articolo}, {id_item} succeded!")
                
        elif service=="preleva":
            print(f"[{current_thread().name}] Sending request {service}, {articolo}")
            
            result=proxy.preleva(articolo)
            
            if result==-1:
                print(f"[{current_thread().name}] Request {service}, {articolo} failed!")
            else:
                print(f"[{current_thread().name}] Request {service}, {articolo} succeded!")
    
    proxy.s.close()
                
def main():
    try:
        service=sys.argv[1]
        port=int(sys.argv[2])
        
    except IndexError:
        print("[CLIENT] Missing service name and/or server port parameter/s")
        sys.exit(-1)
        
    threads=[]
    
    for i in range(NUM_THREADS):
        t=Thread(target=thread_fun, args=(service, IP, port, NUM_REQS_THREADS), name="CLIENT THREAD-"+str(i))
        threads.append(t)
        t.start()

    for i in range(NUM_THREADS):
        threads.pop().join()
        
    print("[CLIENT] Client terminato")

    
if __name__=="__main__":
    main()