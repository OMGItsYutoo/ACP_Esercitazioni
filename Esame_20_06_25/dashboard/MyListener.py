import stomp

class MyListener(stomp.ConnectionListener):
    def __init__(self):
        file=open("./dashboard/alerts.txt",'a')
        file.truncate(0)
        file.close()
    
    def on_message(self, frame):
        print(f"[Dashboard] - Received {frame.body}")
        
        with open("./dashboard/alerts.txt", "a") as f:
            f.write(str(frame.body)+'\n')
        