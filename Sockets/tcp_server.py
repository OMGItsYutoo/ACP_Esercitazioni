import socket 

IP='0.0.0.0' #all interfaces on the local machine
PORT=0 #arbitrary port number
BUFFER_SIZE=1024

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((IP,PORT))

s.listen(1)

print(s.getsockname())
cur_port=s.getsockname()[1]

print(f"server tcp in ascolto su {IP}:{cur_port}")

while(1):
    conn,addr=s.accept()
    print("client info: ", str(addr))
    toClient="Fozza Naboli\n"
    
    data=conn.recv(BUFFER_SIZE)
    
    print(data.decode('utf-8'))
    
    conn.send(toClient.encode('utf-8'))
    conn.close()
