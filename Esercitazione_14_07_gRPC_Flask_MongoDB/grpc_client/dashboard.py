from proto import statistics_pb2, statistics_pb2_grpc
import grpc
import sys

if __name__=="__main__":
    try:
        port=sys.argv[1]
    except IndexError:
        print("Please insert the port the server is listening on.")
    
    channel=grpc.insecure_channel("localhost:"+str(port))
    stub=statistics_pb2_grpc.StatisticsStub(channel)
    
    results=stub.getSensors(statistics_pb2.Empty())
    sensors=[]
    
    for res in results:
        print(f"[Dashboard] - Received sensor_id: {res.sensor_id}, data_type: {res.data_type}")
        sensors.append(res)
        
    for sensor in sensors:
        print(f"[Dashboard] - Sending mean request for sensor_id: {sensor.sensor_id}, data_type: {sensor.data_type}")
        response=stub.getMean(statistics_pb2.MeanRequest(sensor_id=sensor.sensor_id,data_type=sensor.data_type))
        print(f'[Dashboard] - Mean: {response.response}')
    