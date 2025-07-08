from time import sleep
from client.PrinterServerProxy import PrinterServerProxy
import random
import sys

TIPO=["gs","bw","color"]
EXT=["doc","txt"]

if __name__=="__main__":
    try: 
        port=int(sys.argv[1])
    except IndexError:
        print("Please specify the port the server is listening on")
        
    proxy=PrinterServerProxy("localhost", port, 1024)
    
    for _ in range(10):
        type=random.choice(TIPO)
        num=random.randint(0,100)
        ext=random.choice(EXT)
        
        f_path=f"/user/file_{num}.{ext}"
        print(f"[Client] - Invocating print({f_path}, {type})")
        proxy.print(f_path, type)
        sleep(1)