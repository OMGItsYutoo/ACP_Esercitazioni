from threading import Thread, current_thread

class SkeletonThread(Thread):
    def __init__(self, conn, buf_size, thread_name, delegate):
        super().__init__(name=thread_name)
        self.conn=conn
        self.buf_size=buf_size
        self.delegate=delegate
        
    def run(self):
        data=self.conn.recv(self.buf_size)
        msg_split=data.decode().split('-')
        
        service=msg_split[0]
        articolo=msg_split[1]
        
        print(f"[{current_thread().name}] - Received: {data.decode()}")

        result=None
        if service=="deposita":
            id=msg_split[2]
            result=self.delegate.deposita(articolo,id)
        elif service=="preleva":
            result=self.delegate.preleva(articolo)
        else:
            print(f"[{current_thread().name}] Servizio {service} non riconosciuto")
            
        resp=str(result)
        self.conn.send(resp.encode())
        
        self.conn.close()