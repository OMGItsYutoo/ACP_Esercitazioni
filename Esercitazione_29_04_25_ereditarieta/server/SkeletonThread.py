from threading import Thread, current_thread

class SkeletonThread(Thread):
    
    def __init__(self, conn, buf_size, thread_name, ref):
        super.__init__(name=thread_name)
        self.conn=conn
        self.ref=ref
        self.buf_size=buf_size
        
    def run(self):
        
        data=self.conn.recv(self.buf_size)
        message :str=data.decode()
        
        print(f"[{current_thread().name}] Received: {message}")
        
        msg_split=message.split("-")
        service=msg_split[0]
        article=msg_split[1]
        
        result=None
        
        if service=="preleva":
            result=self.ref.preleva(article)
        elif service=="deposita":
            id=msg_split[2]
            result=self.ref.deposita(article,id)
        else: print(f"[{current_thread().name}] Servizio {service} non riconosciuto")
        
        response=str(result)
        self.conn.send(response.encode())
        
        self.conn.close()   