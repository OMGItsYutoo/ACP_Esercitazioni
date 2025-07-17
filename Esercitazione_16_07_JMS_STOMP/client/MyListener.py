import stomp

class MyListener(stomp.ConnectionListener):
    def on_message(self, frame):
        print(f"[ClientListener] - Received message: {frame.body}")