import helloworld_pb2_grpc

class Greeter (helloworld_pb2_grpc.GreeterServicer):
    
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)