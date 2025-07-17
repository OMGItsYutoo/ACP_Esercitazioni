import stomp
import requests

class MyListener(stomp.ConnectionListener):
    def __init__(self, base_url, conn:stomp.Connection):
        self.base_url=base_url
        self.conn=conn
    
    def on_message(self, frame):
        print(f"[BookingManagerListener] - Received: {frame.body}")
        
        msg_split=str(frame.body).split('-')
        request=msg_split[0]
        
        if request=="CREATE":
            create_data={
                "client":msg_split[1],
                "hotel":msg_split[2],
                "operator":msg_split[3],
                "nights":msg_split[4],
                "people":msg_split[5],
                "cost":msg_split[6],
            }
            
            req=requests.post(self.base_url+"/booking", json=create_data)

            try:
                req.raise_for_status()
            except requests.HTTPError as e:
                print(f"[BookingManagerListener] - An Exception has occurred: {e}")
                
        elif request=="UPDATE":
            update_data={
                "operator":msg_split[2],
                "nights":msg_split[3],
                "discount":msg_split[1],
            }
            
            req=requests.put(self.base_url+"/booking", json=update_data)
            
            try:
                req.raise_for_status()
            except requests.HTTPError as e:
                print(f"[BookingManagerListener] - An Exception has occurred: {e}")
        else:
            print(f"[BookingManagerListener] - Couldn't recognized request: {request}")
            
        self.conn.send("/topic/responses",req.text)