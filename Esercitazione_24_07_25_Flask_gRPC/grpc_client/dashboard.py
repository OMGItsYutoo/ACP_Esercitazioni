from proto import statistics_pb2, statistics_pb2_grpc
import grpc
import sys

if __name__=="__main__":
    
    try:
        port=int(sys.argv[1])
    except IndexError:
        print("Please insert the port the server is listening on.")
    
    channel=grpc.insecure_channel("localhost:"+str(port))
    stub=statistics_pb2_grpc.StatisticsStub(channel)
    
    sensors=stub.getSensors(statistics_pb2.Empty())
    
    for s in sensors:
        sensor_id=s.sensor_id
        data_type=s.data_type
        
        print(f"[Dashboard] - Sending mean request for sensor: {sensor_id}, {data_type}")
        
        res=stub.getMean(statistics_pb2.MeanRequest(sensor_id=sensor_id, data_type=data_type))
        
        print(f"[Dashboard] - Mean for sensor {sensor_id} is {res.mean}")
        