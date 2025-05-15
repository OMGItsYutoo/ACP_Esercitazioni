import helloworld_pb2_grpc
import helloworld_pb2
import grpc
from concurrent import futures

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    
    def SayHello(self, request, context):
        print("[Server] It's me Mario")
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)
    
    
    def serve():
        server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        
        helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
        
        port=server.add_insecure_port("0.0.0.0:0")

        server.start()
        
        print(f"[Server] listening on localhost and port {port}")
        
        server.wait_for_termination()
        
if __name__=="__main__":
    Greeter.serve()